import streamlit as st
from src.resume_screening import extract_resume_text, screen_resume


st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="centered"
)


st.title("📄 AI Resume Screening")

st.write(
    "Upload a resume and enter a job description to check "
    "how well the resume matches the job."
)

st.divider()


# Resume upload
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# Job description
job_description = st.text_area(
    "Job Description",
    height=200,
    placeholder="Paste the job description here..."
)


st.write("")


if st.button(
    "🔍 Screen Resume",
    use_container_width=True
):

    if resume_file is None:

        st.warning("Please upload a resume PDF.")

    elif not job_description.strip():

        st.warning("Please enter a job description.")

    else:

        with st.spinner("Analyzing resume..."):

            resume_text = extract_resume_text(
                resume_file
            )

            result = screen_resume(
                resume_text,
                job_description
            )


        st.divider()

        st.subheader("Screening Result")


        # Match score
        st.metric(
            "Resume Match Score",
            f"{result['score']:.2f}%"
        )


        # Result
        if result["result"] == "Strong Match":

            st.success(
                f"Result: {result['result']}"
            )

        elif result["result"] == "Moderate Match":

            st.warning(
                f"Result: {result['result']}"
            )

        else:

            st.error(
                f"Result: {result['result']}"
            )


        st.divider()


        # Skills
        col1, col2 = st.columns(2)


        with col1:

            st.subheader("✅ Matching Skills")

            if result["matching_skills"]:

                for skill in result["matching_skills"]:
                    st.write(f"• {skill}")

            else:

                st.write("No matching skills found.")


        with col2:

            st.subheader("❌ Missing Skills")

            if result["missing_skills"]:

                for skill in result["missing_skills"]:
                    st.write(f"• {skill}")

            else:

                st.write("No major missing skills found.")


st.divider()


st.caption(
    "AI Resume Screening • TF-IDF • Cosine Similarity • Streamlit"
)

st.caption(
    "This tool is intended for educational and demonstration purposes."
)