from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
# fetching API KEY from env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# input data validation

class userQuery(BaseModel):
    currentQuery: str
    sessionId: str = None

# example of full chat
fullChat = [{"role": "user", "parts": [{"text": "Explain how AI works in a few words"}]}, 
{"role": "model", "parts": [{"text": "AI is a technology that allows machines to learn and make decisions based on data."}]},
{"role": "user", "parts": [{"text": "Give me the chat history"}]}]


client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=fullChat
)
print(response.text)
print(response)