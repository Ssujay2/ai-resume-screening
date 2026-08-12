import re
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_skills(text):
    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "streamlit",
        "fastapi",
        "flask",
        "django",
        "react",
        "javascript",
        "html",
        "css",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "gcp",
        "langchain",
        "openai",
        "generative ai",
        "natural language processing",
        "nlp"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return found_skills


def calculate_match_score(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def screen_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matching_skills = sorted(
        set(resume_skills) & set(job_skills)
    )

    missing_skills = sorted(
        set(job_skills) - set(resume_skills)
    )

    score = calculate_match_score(
        resume_text,
        job_description
    )

    if score >= 70:
        result = "Strong Match"
    elif score >= 50:
        result = "Moderate Match"
    else:
        result = "Low Match"

    return {
        "score": score,
        "result": result,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }