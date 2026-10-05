from interview_questions import generate_questions


matched_skills = [
    "python",
    "sql",
    "excel"
]

missing_skills = [
    "statistics",
    "tableau"
]


questions = generate_questions(
    matched_skills,
    missing_skills
)


print("\n========== INTERVIEW QUESTIONS ==========\n")

for number, question in enumerate(questions, start=1):
    print(f"{number}. {question}")

print("\n=========================================")