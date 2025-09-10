from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_relevant_chunk(chunks, question):
    vectorizer = TfidfVectorizer().fit_transform(chunks + [question])
    similarity_matrix = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    best_idx = similarity_matrix.argmax()
    return chunks[best_idx]
