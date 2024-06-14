import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load all environment variables

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get AI response
def get_gemini_response(input):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text
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
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
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
                prompt = input_prompt.format(text=text, jd=jd)
                response = get_gemini_response(prompt)
                if response:
                    try:
                        result = json.loads(response)
                        st.subheader("Results")
                        st.write(f"**JD Match:** {result['JD Match']}")
                        st.write(f"**Missing Keywords:** {', '.join(result['MissingKeywords'])}")
                        st.write(f"**Profile Summary:** {result['Profile Summary']}")
                    except json.JSONDecodeError:
                        st.error("Error parsing the response from the AI. Please try again.")
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