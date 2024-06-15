# Smart ATS

Smart ATS is a web application designed to help users improve their resumes for better matching with job descriptions using advanced NLP techniques and AI. The application extracts text from uploaded resumes, compares it with the provided job description, and offers feedback on the match percentage, missing keywords, and a profile summary.

## Features

- Extracts text from PDF resumes
- Computes cosine similarity between resume and job description using BERT embeddings
- Uses Google Generative AI to provide feedback on resume matching
- User feedback mechanism for continuous improvement

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.7 or later
- pip (Python package installer)

### Install Dependencies

1. Clone the repository:

```sh
git clone https://github.com/yourusername/smart-ats.git
cd smart-ats
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

### Required Environment Variables

Create a `.env` file in the root directory of your project and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```

## Usage

Run the Streamlit application with the following command:

```sh
streamlit run app.py
```

### Uploading a Resume and Job Description

1. Paste the job description in the provided text area.
2. Upload your resume as a PDF file.
3. Click the "Submit" button to get feedback on your resume.

### Providing Feedback

After receiving the feedback, you can rate the usefulness of the feedback and provide additional comments or suggestions.

## Code Explanation

### Main Components

- **Google Generative AI Configuration**: Configures the Google Generative AI using the provided API key.
- **Transformer Model**: Loads the pre-trained BERT model for generating embeddings.
- **PDF Text Extraction**: Extracts text from uploaded PDF resumes.
- **Cosine Similarity Calculation**: Computes the similarity between resume and job description embeddings.
- **AI Response Generation**: Uses Google Generative AI to provide feedback on resume matching.
- **Streamlit UI**: Provides a user-friendly interface for uploading resumes, inputting job descriptions, and viewing feedback.

### Functions

- `get_embeddings(text)`: Generates embeddings for the given text using the BERT model.
- `cosine_similarity(emb1, emb2)`: Computes cosine similarity between two sets of embeddings.
- `get_gemini_response(input_text)`: Gets a response from Google Generative AI based on the provided prompt.
- `input_pdf_text(uploaded_file)`: Extracts text from the uploaded PDF file.
- `input_prompt`: Template for generating AI prompt with the job description and resume text.

### Streamlit Application Flow

1. Users input the job description and upload the resume.
2. The application extracts text from the resume.
3. It generates embeddings for both the resume and job description.
4. Computes the similarity score.
5. Prepares the AI prompt and fetches a response from Google Generative AI.
6. Displays the matching percentage, missing keywords, and profile summary.
7. Collects user feedback for continuous improvement.

## Feedback

We appreciate your feedback to help improve this application. Please use the feedback section in the app to rate its usefulness and provide any comments or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for the `transformers` library
- Google Generative AI for providing the AI content generation capabilities
- Streamlit for the easy-to-use web app framework

---

Feel free to customize this README file to better fit your specific needs or add more details as necessary.
App link:https://smart-ats-wc2iraxzubb4klygaucuaj.streamlit.app/

---

Feel free to contribute to this project by submitting issues or pull requests!
