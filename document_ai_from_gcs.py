from google.cloud import documentai
from google.cloud import storage
from text_processing import clean_text, chunk_text
from text_processing import smart_chunk_text
from embeddings import generate_embeddings
from vector_store import VectorStore
from embeddings import get_query_embedding
from gemini import generate_answer



project_id = "574320271763"
location = "us"
processor_id = "8d045f4a590d6942"

bucket_name = "medical-report-storage"
file_name = "Report1.pdf"

# Download file from GCS
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_name)

file_content = blob.download_as_bytes()

# Document AI client
client = documentai.DocumentProcessorServiceClient()

name = client.processor_path(project_id, location, processor_id)

raw_document = documentai.RawDocument(
    content=file_content,
    mime_type="image/webp"
)

request = documentai.ProcessRequest(
    name=name,
    raw_document=raw_document
)

result = client.process_document(request=request)

document = result.document

print("\n========= EXTRACTED TEXT =========\n")
print(document.text)

cleaned_text = clean_text(document.text)

#chunks = chunk_text(cleaned_text)
chunks = smart_chunk_text(document.text)

print("\n========= CHUNKS =========\n")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---\n")
    print(chunk)

embeddings = generate_embeddings(chunks)

print("\n========= EMBEDDINGS =========\n")
print(f"Generated {len(embeddings)} embeddings")

#Create vector DB
vector_db = VectorStore(embeddings, chunks)

# Example query
#query = "Is the brain normal?"

#query = input("\nAsk your question: ")

#query_embedding = get_query_embedding(query)

#results = vector_db.search(query_embedding)

#print("\n========= SEARCH RESULTS =========\n")

while True:
    query = input("\nAsk your question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = get_query_embedding(query)
    results = vector_db.search(query_embedding)
    answer = generate_answer(results, query)

    print("\n========= ANSWER =========\n")
    print(answer)

for r in results:
    print("\n--- Relevant Chunk ---\n")
    print(r)

answer = generate_answer(results, query)

print("\n========= FINAL ANSWER =========\n")
print(answer)