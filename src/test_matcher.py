from skill_matcher import calculate_match


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


match = calculate_match(
    candidate_skills,
    job_requirements
)

print(f"Job Match: {match}%")
