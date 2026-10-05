from job_analyzer import analyze_job


candidate_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI"
]

job_requirements = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Statistics"
]


result = analyze_job(
    candidate_skills,
    job_requirements
)


print("\n========== JOB ANALYSIS ==========")

print(f"\nJob Match: {result['match_percentage']}%")

print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print("✓", skill)

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("✗", skill)

print("\n==================================")