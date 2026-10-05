from interview_evaluator import evaluate_answer


question = "What is SQL and where have you used it?"

answer = """
SQL is used to manage and query data from databases.
I have used SQL in my project to retrieve data using
SELECT and WHERE queries. I also used JOIN to combine
data from different tables.
"""


result = evaluate_answer(question, answer)


print("\n========== INTERVIEW EVALUATION ==========\n")

print("Question:")
print(question)

print("\nAnswer:")
print(answer)

print(f"\nScore: {result['score']}/10")

print("\nStrengths:")
for strength in result["strengths"]:
    print("✓", strength)

print("\nSuggestions:")
for suggestion in result["suggestions"]:
    print("→", suggestion)

print("\n==========================================")