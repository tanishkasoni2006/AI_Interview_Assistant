from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the pre-trained sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match(candidate_skills, job_requirements):
    """
    Compares candidate skills with job requirements
    and returns a match percentage.
    """

    candidate_text = ", ".join(candidate_skills)
    job_text = ", ".join(job_requirements)

    # Convert both texts into numerical vectors
    candidate_embedding = model.encode([candidate_text])
    job_embedding = model.encode([job_text])

    # Calculate similarity
    similarity = cosine_similarity(
        candidate_embedding,
        job_embedding
    )[0][0]

    # Convert similarity into percentage
    match_percentage = round(similarity * 100, 2)

    return match_percentage
