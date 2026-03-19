from vertexai.language_models import TextEmbeddingModel
import vertexai

# Initialize Vertex AI
vertexai.init(project="574320271763", location="us-central1")

model = TextEmbeddingModel.from_pretrained("text-embedding-004")

def generate_embeddings(chunks):
    embeddings = []
    
    for chunk in chunks:
        response = model.get_embeddings([chunk])
        embeddings.append(response[0].values)
    
    return embeddings

def get_query_embedding(query):
    response = model.get_embeddings([query])
    return response[0].values