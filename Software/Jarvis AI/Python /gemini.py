from google import genai


client = genai.Client(
    api_key="YOUR API KEY HERE"


)


def ask_gemini(question):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=f"""
You are Jarvis, a friendly AI assistant.

Rules:
- Talk naturally like a normal person.
- Do not use weird formatting like **, ##, bullet spam, or unnecessary headings.
- Keep answers conversational and easy to understand.
- Be concise unless the user asks for more detail.
- Do not start answers with phrases like "Certainly", "Of course", or "Absolutely" every time.
- Explain things like a helpful friend, not like a textbook.
- Match the user's casual tone.

User:
{question}
"""
    )

    return response.text


