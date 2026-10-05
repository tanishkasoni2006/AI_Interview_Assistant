def analyze_skills(candidate_skills, job_requirements):
    """
    Finds matched and missing skills.
    """

    candidate = {
        str(skill).strip().lower()
        for skill in candidate_skills
        if str(skill).strip()
    }

    required = {
        str(skill).strip().lower()
        for skill in job_requirements
        if str(skill).strip()
    }

    matched = sorted(candidate.intersection(required))
    missing = sorted(required - candidate)

    return matched, missing