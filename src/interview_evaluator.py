def evaluate_answer(question, answer):
    """
    Evaluates an interview answer using simple keyword-based analysis.
    Returns a score, strengths, and suggestions.
    """

    # Handle empty answer
    if not answer.strip():
        return {
            "score": 0,
            "strengths": ["No answer provided."],
            "suggestions": ["Please provide an answer."]
        }

    answer_lower = answer.lower()
    answer_words = answer_lower.split()

    # Important answer-quality indicators
    indicators = [
        "because",
        "example",
        "project",
        "experience",
        "used",
        "implemented",
        "result",
        "problem",
        "solution",
        "process",
        "benefit",
        "why",
        "how"
    ]

    matched_indicators = 0

    for word in indicators:
        if word in answer_words:
            matched_indicators += 1

    # -----------------------------
    # Calculate base score
    # -----------------------------

    score = 5

    # More detailed answers
    if len(answer_words) >= 20:
        score += 1

    if len(answer_words) >= 40:
        score += 1

    if len(answer_words) >= 60:
        score += 1

    # Practical example / project
    if (
        "example" in answer_lower
        or "project" in answer_lower
        or "experience" in answer_lower
    ):
        score += 1

    # Explanation / reasoning
    if (
        "because" in answer_lower
        or "why" in answer_lower
        or "how" in answer_lower
    ):
        score += 1

    # Cap score at 10
    score = min(score, 10)

    # -----------------------------
    # Strengths
    # -----------------------------

    strengths = []

    if len(answer_words) >= 20:
        strengths.append("Answer contains sufficient detail.")

    if (
        "example" in answer_lower
        or "project" in answer_lower
        or "experience" in answer_lower
    ):
        strengths.append("Includes a practical example or project reference.")

    if (
        "because" in answer_lower
        or "why" in answer_lower
        or "how" in answer_lower
    ):
        strengths.append("Provides reasoning or explanation.")

    if matched_indicators >= 4:
        strengths.append("Answer covers multiple important points.")

    if not strengths:
        strengths.append("Answer is relevant to the question.")

    # -----------------------------
    # Suggestions
    # -----------------------------

    suggestions = []

    if len(answer_words) < 20:
        suggestions.append(
            "Add more detail to make the answer stronger."
        )

    if not (
        "example" in answer_lower
        or "project" in answer_lower
        or "experience" in answer_lower
    ):
        suggestions.append(
            "Add a practical example from a project or experience."
        )

    if not (
        "because" in answer_lower
        or "why" in answer_lower
        or "how" in answer_lower
    ):
        suggestions.append(
            "Explain why or how, not just what."
        )

    if not (
        "result" in answer_lower
        or "benefit" in answer_lower
    ):
        suggestions.append(
            "Mention the result or benefit of your approach."
        )

    if not suggestions:
        suggestions.append(
            "Good answer. Try to keep the explanation clear and specific."
        )

    # -----------------------------
    # Final result
    # -----------------------------

    return {
        "score": score,
        "strengths": strengths,
        "suggestions": suggestions
    }