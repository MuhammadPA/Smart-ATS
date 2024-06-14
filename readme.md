# Smart ATS

## Overview
Smart ATS is a Streamlit web application designed to help job seekers improve their resumes to better match job descriptions. The app uses Google Generative AI to act as an Application Tracking System (ATS) with expertise in the tech field, software engineering, data science, data analysis, and big data engineering. The system evaluates resumes based on a provided job description and suggests improvements by identifying missing keywords and providing a match percentage.

## Features
- **Job Description Analysis**: Input a job description and get a detailed analysis of your resume's match to the job requirements.
- **Resume Upload**: Upload your resume in PDF format.
- **AI-Powered Feedback**: Receive AI-generated feedback on how to improve your resume, including a match percentage and missing keywords.
- **User Feedback**: Provide feedback on the usefulness of the AI-generated suggestions.

## Technologies Used
- **Streamlit**: A web framework for creating interactive web applications in Python.
- **Google Generative AI**: Used for generating content and providing analysis of resumes.
- **PyPDF2**: A Python library for reading and extracting text from PDF files.
- **dotenv**: For loading environment variables.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Google Generative AI API key

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-ats.git
   cd smart-ats
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory of the project.
   - Add your Google API key to the `.env` file:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open the web app**
   - The app will open in your default web browser, or you can navigate to `http://localhost:8501`.

3. **Input job description and upload resume**
   - Paste the job description in the provided text area.
   - Upload your resume in PDF format.
   - Click the "Submit" button to receive feedback.

## Acknowledgements
- Streamlit for the interactive web framework.
- Google Generative AI for the powerful content generation and analysis capabilities.
- PyPDF2 for PDF text extraction.

App link:https://smart-ats-wc2iraxzubb4klygaucuaj.streamlit.app/

---

Feel free to contribute to this project by submitting issues or pull requests!
