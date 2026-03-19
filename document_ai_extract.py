from google.cloud import documentai

project_id = "574320271763"
location = "us"
processor_id = "8d045f4a590d6942"

file_path = "downloaded_report.pdf"

def process_document():

    print("Starting Document AI...")

    client = documentai.DocumentProcessorServiceClient()

    name = client.processor_path(project_id, location, processor_id)

    with open(file_path, "rb") as f:
        file_content = f.read()

    print("File loaded successfully")

    raw_document = documentai.RawDocument(
        content=file_content,
        mime_type="application/pdf",
    )

    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document,
    )

    print("Sending document to Document AI...")

    result = client.process_document(request=request)

    document = result.document

    print("\n========= EXTRACTED TEXT =========\n")

    print(document.text)

process_document()