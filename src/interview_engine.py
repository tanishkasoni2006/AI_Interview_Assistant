from src.job_analyzer import analyze_job
from src.interview_questions import generate_questions
from src.interview_evaluator import evaluate_answer


def run_interview_analysis(
    candidate_skills,
    job_requirements,
    question,
    answer
):

    # Analyze candidate skills against job requirements
    job_result = analyze_job(
        candidate_skills,
        job_requirements
    )

    # Generate interview questions
    questions = generate_questions(
        job_result["matched_skills"],
        job_result["missing_skills"]
    )

    # Evaluate the candidate's answer
    answer_result = evaluate_answer(
        question,
        answer
    )

    return {
        "job_analysis": job_result,
        "questions": questions,
        "answer_evaluation": answer_result
    }