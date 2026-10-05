from src.skill_matcher import calculate_match
from src.skill_gap import analyze_skills


def convert_to_skill_list(skills):
    """Convert skill input into a clean list of skills."""

    if isinstance(skills, str):
        return [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

    return [
        str(skill).strip()
        for skill in skills
        if str(skill).strip()
    ]


def analyze_job(candidate_skills, job_requirements):
    """
    Performs complete candidate-job analysis.
    """

    # Convert input into proper skill lists
    candidate_skills = convert_to_skill_list(candidate_skills)
    job_requirements = convert_to_skill_list(job_requirements)

    # Calculate match percentage
    match_percentage = calculate_match(
        candidate_skills,
        job_requirements
    )

    # Find matched and missing skills
    matched_skills, missing_skills = analyze_skills(
        candidate_skills,
        job_requirements
    )

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }