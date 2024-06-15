import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from transformers import AutoTokenizer, AutoModel
import torch

load_dotenv()  # Load all environment variables

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load pre-trained transformer model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Function to get embeddings
def get_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

# Function to get cosine similarity
def cosine_similarity(emb1, emb2):
    return torch.nn.functional.cosine_similarity(emb1, emb2).item()

# Function to get AI response
def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and
the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"{percentage}%","MissingKeywords":["keyword1", "keyword2"],"Profile Summary":"summary"}}
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

if st.button("Submit"):
    if uploaded_file is not None and jd.strip():
        with st.spinner("Processing..."):
            text = input_pdf_text(uploaded_file)
            if text:
                # Generate embeddings for both the resume and job description
                resume_embeddings = get_embeddings(text)
                jd_embeddings = get_embeddings(jd)

                # Calculate cosine similarity
                similarity_score = cosine_similarity(resume_embeddings, jd_embeddings) * 100

                # Prepare the AI prompt
                prompt = input_prompt.format(text=text, jd=jd, percentage=round(similarity_score, 2))
                response = get_gemini_response(prompt)
                if response:
                    try:
                        result = json.loads(response)
                        st.subheader("Results")
                        st.write(f"**JD Match:** {result['JD Match']}")
                        st.write(f"**Missing Keywords:** {', '.join(result['MissingKeywords'])}")
                        st.write(f"**Profile Summary:** {result['Profile Summary']}")
                    except json.JSONDecodeError as json_error:
                        st.error(f"Error parsing the response from the AI: {json_error}")
                else:
                    st.error("Failed to get a response from the AI.")
            else:
                st.error("Failed to extract text from the uploaded PDF.")
    else:
        st.warning("Please provide both a job description and a resume.")

# Feedback Section
st.subheader("Feedback")
rating = st.radio("How useful was the feedback?", ["Very Useful", "Somewhat Useful", "Not Useful"])
comments = st.text_area("Any comments or suggestions?")

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
