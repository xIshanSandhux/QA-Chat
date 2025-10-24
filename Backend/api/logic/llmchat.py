from google import genai
from dotenv import load_dotenv
import os
# fetching API KEY from env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# example of full chat
# fullChatexample = [
#     {"role": "user", "parts": [{"text": "Explain how AI works in a few words"}]}, 
# {"role": "model", "parts": [{"text": "AI is a technology that allows machines to learn and make decisions based on data."}]},
# ]

fullChat = []

client = genai.Client(api_key=GOOGLE_API_KEY)

# adding to chat history
# role: user or model
# text: the text to add to the chat history
# will be changed when redis is implemented 
# will be changed to return the format to be stored in redis?
def addToChat(role, text):
    fullChat.append({"role": role, "parts": [{"text": text}]})

# getting chat history
# will be changed when redis is implemented 
# will be changed to get the chat from redis and then return the full chat history in a list
def getChatHistory():
    return fullChat

async def generateResponse(query: str):
    
    addToChat("user", query)
    chatfull = getChatHistory()
    print(chatfull)
    print("Generating response...")
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=chatfull
    )
    addToChat("model", response.text)
    print(getChatHistory())
    return response.text
