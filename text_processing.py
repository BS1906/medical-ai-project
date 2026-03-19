import re

def clean_text(text):
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks

def smart_chunk_text(text):
    sections = ["Technique", "Findings", "Impression"]
    
    chunks = []
    current_chunk = ""
    
    for line in text.split("\n"):
        if any(section in line for section in sections):
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = line
        else:
            current_chunk += " " + line
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks