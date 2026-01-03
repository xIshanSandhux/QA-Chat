from dotenv import load_dotenv
import os
import json
from api.redis.chatupdates import addToChat, getChatHistory
from vectorDB.chromaDB.chroma import getQueryChunks
from LLM.factory import LLMProviderFactory

provider = LLMProviderFactory()

# will be using the documents parameter for giving the relevant chunks
async def generateResponse(session_id, query: str):
    
    # await addToChat(session_id, "user", query)
    # chat_history = await getChatHistory(session_id)
    # if rag:
    #     system_prompt = open("api/logic/sysprompt.md", "r").read()
    #     relChunks = await getQueryChunks(session_id, query)
    #     chunks = json.dumps(relChunks["documents"])
    #     system_prompt = system_prompt + "\n\n" + "these are the relevant chunks from the document: " + chunks
    #     response = client.models.generate_content(
    #         model="gemini-2.5-flash",
    #         config=types.GenerateContentConfig(
    #             system_instruction=system_prompt),
    #             contents=chat_history
    #         )
    # else:
    #     response = client.models.generate_content(
    #         model="gemini-2.5-flash", contents=chat_history
    #     )
    # await addToChat(session_id, "model", response.text)
    # return response.text


    response = await provider.generate_response(query)
    return response
