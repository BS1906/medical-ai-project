from google.cloud import storage

bucket_name = "medical-report-storage"
file_name = "Report1.pdf"   # change to your actual path

client = storage.Client()

bucket = client.bucket(bucket_name)

blob = bucket.blob(file_name)

blob.download_to_filename("downloaded_report.pdf")

print("File downloaded successfully")