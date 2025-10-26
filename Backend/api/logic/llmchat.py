from google import genai
from dotenv import load_dotenv
import os
from api.redis.chatupdates import addToChat, getChatHistory

# fetching API KEY from env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)

async def generateResponse(session_id, query: str):
    
    await addToChat(session_id, "user", query)
    chat_history = await getChatHistory(session_id)
    print("Generating response...")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=chat_history
    )
    await addToChat(session_id, "model", response.text)
    print(await getChatHistory(session_id))
    return response.text
