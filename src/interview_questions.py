def generate_questions(matched_skills, missing_skills):

    questions = []

    # Questions based on matched skills
    for skill in matched_skills:
        questions.append(
            f"What is {skill} and how have you used it in a project?"
        )

    # Questions based on missing skills
    for skill in missing_skills:
        questions.append(
            f"What do you know about {skill}?"
        )

        questions.append(
            f"How would you learn or apply {skill} in a real-world project?"
        )

    return questions