from dotenv import load_dotenv

load_dotenv()

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client() 

# Enable the Google Search tool
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is the current price of Bitcoin?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    )
)
print(response.text)
