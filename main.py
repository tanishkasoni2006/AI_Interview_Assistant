from src.job_analyzer import analyze_job
from src.interview_questions import generate_questions
from src.interview_evaluator import evaluate_answer


def main():

    print("\n====================================")
    print("        AI INTERVIEW ASSISTANT")
    print("====================================")

    # Candidate skills
    candidate_skills = [
        "Python",
        "SQL",
        "Excel",
        "Data Analysis"
    ]

    # Job requirements
    job_requirements = [
        "Python",
        "SQL",
        "Machine Learning",
        "Data Analysis"
    ]

    # ---------------------------------
    # JOB ANALYSIS
    # ---------------------------------

    print("\nAnalyzing Job Requirements...")

    result = analyze_job(
        candidate_skills,
        job_requirements
    )

    print("\n========== JOB ANALYSIS ==========")

    print(f"Job Match: {result['match_percentage']:.2f}%")

    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print("✓", skill)

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print("✗", skill)

    # ---------------------------------
    # GENERATE INTERVIEW QUESTIONS
    # ---------------------------------

    questions = generate_questions(
        result["matched_skills"],
        result["missing_skills"]
    )

    print("\n====================================")
    print("          INTERVIEW ROUND")
    print("====================================")

    total_score = 0
    question_count = 0

    # ---------------------------------
    # ASK QUESTIONS
    # ---------------------------------

    for question in questions:

        print("\nQuestion:")
        print(question)

        answer = input("\nYour Answer: ")

        evaluation = evaluate_answer(
            question,
            answer
        )

        print("\n----- Evaluation -----")

        print(f"Score: {evaluation['score']}/10")

        print("\nStrengths:")
        for strength in evaluation["strengths"]:
            print("✓", strength)

        print("\nSuggestions:")
        for suggestion in evaluation["suggestions"]:
            print("→", suggestion)

        total_score += evaluation["score"]
        question_count += 1

    # ---------------------------------
    # FINAL INTERVIEW RESULT
    # ---------------------------------

    if question_count > 0:

        average_score = total_score / question_count

        print("\n====================================")
        print("       FINAL INTERVIEW RESULT")
        print("====================================")

        print(
            f"Average Score: {average_score:.2f}/10"
        )

        print(
            f"Questions Attempted: {question_count}"
        )


if __name__ == "__main__":
    main()