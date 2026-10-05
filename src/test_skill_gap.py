from skill_gap import analyze_skills


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


matched, missing = analyze_skills(
    candidate_skills,
    job_requirements
)


print("Matched Skills:")
for skill in matched:
    print("✓", skill)


print("\nMissing Skills:")
for skill in missing:
    print("✗", skill)