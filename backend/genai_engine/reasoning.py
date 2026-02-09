from google import genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_reasoning(context):
    prompt = f"""
You are an AI disaster risk analyst.
Analyze the following climate data and generate insights:

{context}

Include:
- Risk explanation
- Local implications
- Preventive actions
"""

    response = model.generate_content(prompt)
    return response.text

