from google.cloud import storage

client = storage.Client()
bucket = client.bucket("medical-report-storage")
blob = bucket.blob("Report1.pdf")

data = blob.download_as_bytes()

print("File size:", len(data))
print("First bytes:", data[:10])