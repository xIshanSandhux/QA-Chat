from dotenv import load_dotenv
import os
import json
from Infra.redis.groqChatHistory import groqChat
from vectorDB.chromaDB.chroma import getQueryChunks
from src.services.LLM.factory import LLMProviderFactory

provider = LLMProviderFactory()

# will be using the documents parameter for giving the relevant chunks
async def generateResponse(session_id, query: str):
    
    try:
        # re-writing query for better context
        rewrite = await provider.query_rewrite(query)
        # Getting the chat history for the user
        history = await groqChat().getChatHistory(session_id)
        # appending to the current history for performance
        history.append({"role":"user","content":query})
        # generating response from the LLM
        res = await provider.generate_response(history)

        return res
    except Exception as e:
        print(f"Exception while generating a response: {str(e)}")
    finally:
        try:
            await groqChat().addChat(session_id,"user",query)
            await groqChat().addChat(session_id,"assistant",res)
        except Exception as e:
            print(f"Exception occurred while adding the user query and assistant response to redis")