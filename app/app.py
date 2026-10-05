import sys
import os
import streamlit as st

# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# IMPORT PROJECT MODULES
# ============================================================

from src.job_analyzer import analyze_job
from src.interview_questions import generate_questions
from src.interview_evaluator import evaluate_answer


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "scores" not in st.session_state:
    st.session_state.scores = []

if "evaluations" not in st.session_state:
    st.session_state.evaluations = []

if "job_result" not in st.session_state:
    st.session_state.job_result = None


# ============================================================
# TITLE
# ============================================================

st.title("🎯 AI Interview Assistant")

st.write(
    "Prepare for your interview with AI-powered job analysis, "
    "skill-gap detection and interview practice."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🎯 AI Interview Assistant")

    st.write(
        "This application helps candidates "
        "prepare for interviews."
    )

    st.divider()

    st.subheader("Features")

    st.write("✅ Job Description Analysis")
    st.write("✅ Skill Matching")
    st.write("✅ Missing Skill Detection")
    st.write("✅ Interview Question Generation")
    st.write("✅ Answer Evaluation")
    st.write("✅ Question-wise Scoring")
    st.write("✅ Final Performance Report")


# ============================================================
# JOB DESCRIPTION
# ============================================================

st.subheader("📄 Job Description")

job_description = st.text_area(
    "Paste the job description here:",
    height=180,
    placeholder=(
        "Example: Python, SQL, Excel, Power BI, "
        "Machine Learning, Data Analysis"
    )
)


# ============================================================
# CANDIDATE SKILLS
# ============================================================

st.subheader("👤 Your Skills")

candidate_skills = st.text_input(
    "Enter your skills:",
    placeholder=(
        "Example: Python, SQL, Excel, Data Analysis"
    )
)


# ============================================================
# START INTERVIEW
# ============================================================

if st.button("🚀 Start Interview", type="primary"):

    if not job_description.strip():

        st.warning(
            "Please enter the job description."
        )

    elif not candidate_skills.strip():

        st.warning(
            "Please enter your skills."
        )

    else:

        # ----------------------------------------------------
        # Convert inputs into lists
        # ----------------------------------------------------

        candidate_skills_list = [
            skill.strip()
            for skill in candidate_skills.split(",")
            if skill.strip()
        ]

        job_requirements_list = [
            skill.strip()
            for skill in job_description.split(",")
            if skill.strip()
        ]

        # ----------------------------------------------------
        # Analyze candidate and job
        # ----------------------------------------------------

        job_result = analyze_job(
            candidate_skills_list,
            job_requirements_list
        )

        # ----------------------------------------------------
        # Generate interview questions
        # ----------------------------------------------------

        questions = generate_questions(
            job_result["matched_skills"],
            job_result["missing_skills"]
        )

        # ----------------------------------------------------
        # Save results in session state
        # ----------------------------------------------------

        st.session_state.job_result = job_result

        st.session_state.questions = questions

        st.session_state.current_question = 0

        st.session_state.scores = []

        st.session_state.evaluations = []

        st.session_state.started = True

        st.success(
            "✅ Interview started successfully!"
        )


# ============================================================
# JOB ANALYSIS
# ============================================================

if st.session_state.started:

    result = st.session_state.job_result

    st.divider()

    st.header("📊 Job Analysis")

    # --------------------------------------------------------
    # Match Percentage
    # --------------------------------------------------------

    match_percentage = result["match_percentage"]

    st.metric(
        "Job Match Percentage",
        f"{match_percentage:.2f}%"
    )

    st.write("")


    # --------------------------------------------------------
    # Matched and Missing Skills
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        matched_skills = result["matched_skills"]

        if matched_skills:

            for skill in matched_skills:
                st.success(skill)

        else:

            st.info("No matching skills found.")


    with col2:

        st.subheader("❌ Missing Skills")

        missing_skills = result["missing_skills"]

        if missing_skills:

            for skill in missing_skills:
                st.warning(skill)

        else:

            st.success(
                "No major missing skills detected."
            )


    # ========================================================
    # INTERVIEW ROUND
    # ========================================================

    st.divider()

    st.header("📝 Interview Round")

    questions = st.session_state.questions

    question_count = len(questions)

    # --------------------------------------------------------
    # Check if questions exist
    # --------------------------------------------------------

    if question_count == 0:

        st.info(
            "No interview questions were generated."
        )

    else:

        current_question = (
            st.session_state.current_question
        )

        # ----------------------------------------------------
        # Finished Interview
        # ----------------------------------------------------

        if current_question >= question_count:

            st.success(
                "🎉 Interview completed!"
            )

            # ------------------------------------------------
            # Final Performance Report
            # ------------------------------------------------

            st.divider()

            st.header("📈 Final Performance Report")

            scores = st.session_state.scores

            if scores:

                total_score = sum(scores)

                average_score = (
                    total_score / len(scores)
                )

                st.metric(
                    "Average Score",
                    f"{average_score:.2f}/10"
                )

                st.write(
                    f"**Questions Attempted:** "
                    f"{len(scores)}"
                )

                st.subheader(
                    "📝 Question-wise Scores"
                )

                for i, score in enumerate(scores):

                    st.write(
                        f"Question {i + 1}: "
                        f"**{score}/10**"
                    )

                # --------------------------------------------
                # Overall Performance
                # --------------------------------------------

                st.subheader(
                    "💡 Overall Suggestions"
                )

                if average_score >= 8:

                    st.success(
                        "Excellent performance! "
                        "Your answers show strong understanding."
                    )

                elif average_score >= 6:

                    st.info(
                        "Good performance. "
                        "Keep practicing to improve your confidence "
                        "and answer quality."
                    )

                elif average_score >= 4:

                    st.warning(
                        "Average performance. "
                        "Focus on improving your technical knowledge "
                        "and explaining your answers clearly."
                    )

                else:

                    st.error(
                        "You need more practice. "
                        "Revise the required skills and practice "
                        "interview questions regularly."
                    )

            else:

                st.info(
                    "No answers were evaluated."
                )


        # ----------------------------------------------------
        # Ask Current Question
        # ----------------------------------------------------

        else:

            st.write(
                f"### Question "
                f"{current_question + 1} of {question_count}"
            )

            question = questions[current_question]

            st.info(question)

            answer = st.text_area(
                "Your Answer:",
                key=f"answer_{current_question}",
                height=150,
                placeholder=(
                    "Type your answer here..."
                )
            )

            # ------------------------------------------------
            # Submit Answer
            # ------------------------------------------------

            if st.button(
                "✅ Submit Answer",
                key=f"submit_{current_question}"
            ):

                if not answer.strip():

                    st.warning(
                        "Please enter your answer before submitting."
                    )

                else:

                    # ----------------------------------------
                    # Evaluate answer
                    # ----------------------------------------

                    answer_result = evaluate_answer(
                        question,
                        answer
                    )

                    # ----------------------------------------
                    # Extract score
                    # ----------------------------------------

                    score = 0

                    if isinstance(
                        answer_result,
                        dict
                    ):

                        if "score" in answer_result:

                            score = answer_result["score"]

                        elif "rating" in answer_result:

                            score = answer_result["rating"]

                    elif isinstance(
                        answer_result,
                        (int, float)
                    ):

                        score = answer_result


                    # ----------------------------------------
                    # Make sure score is between 0 and 10
                    # ----------------------------------------

                    try:

                        score = float(score)

                    except:

                        score = 0


                    score = max(
                        0,
                        min(10, score)
                    )


                    # ----------------------------------------
                    # Save evaluation
                    # ----------------------------------------

                    st.session_state.scores.append(
                        score
                    )

                    st.session_state.evaluations.append(
                        answer_result
                    )


                    # ----------------------------------------
                    # Show evaluation
                    # ----------------------------------------

                    st.subheader(
                        "📋 Answer Evaluation"
                    )

                    if isinstance(
                        answer_result,
                        dict
                    ):

                        for key, value in answer_result.items():

                            formatted_key = (
                                str(key)
                                .replace("_", " ")
                                .title()
                            )

                            st.write(
                                f"**{formatted_key}:** "
                                f"{value}"
                            )

                    else:

                        st.write(
                            answer_result
                        )


                    st.metric(
                        "Score",
                        f"{score:.1f}/10"
                    )


                    # ----------------------------------------
                    # Move to next question
                    # ----------------------------------------

                    st.session_state.current_question += 1

                    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎯 AI Interview Assistant | "
    "AI-powered job analysis and interview preparation"
)