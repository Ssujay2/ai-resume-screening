AI Resume Screening

This project is a simple AI-based resume screening application that checks how closely a resume matches a given job description.

I built this project using Python and basic Natural Language Processing techniques. The application reads the text from a PDF resume, compares it with the job description, calculates a match score, and identifies the skills that match or are missing.

The application is built with Streamlit so that the resume can be uploaded and the results can be viewed through a simple web interface.

What I Used

- Python
- Streamlit
- PyPDF
- Scikit-learn
- TF-IDF
- Cosine Similarity

How It Works

1. Upload a resume in PDF format.
2. The application extracts the text from the resume.
3. Enter the job description.
4. TF-IDF converts the resume and job description into numerical features.
5. Cosine Similarity calculates the resume-to-job match score.
6. The application identifies matching and missing skills.
7. A final screening result is displayed.

Features

- Resume PDF upload
- Job description input
- Resume match percentage
- Matching skills
- Missing skills
- Strong, Moderate, or Low Match result
- Simple Streamlit interface

Project Structure

```text
ai-resume-screening/
│
├── src/
│   └── resume_screening.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
