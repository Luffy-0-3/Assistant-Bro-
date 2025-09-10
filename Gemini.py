from google import genai
from google.genai import types

def neerajai(command):
    api = "YOUR_GOOGLE_GENAI_API_KEY"  # Use your own API key here

    client = genai.Client(api_key=api)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are an instructor like Jarvis/Siri, just give the answer in 50 words with simpler understanding and without ** symbols"
        ),
        contents=command
    )
    return response.text
