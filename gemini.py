import google.generativeai as genai

# Set API key (we will configure next)
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_answer(chunks, query):
    
    context = "\n\n".join(chunks)

    prompt = f"""
You are a medical assistant.

Use the below medical report context to answer the question clearly.

Context:
{context}

Question:
{query}

Answer in simple terms:
"""

    response = model.generate_content(prompt)

    return response.text