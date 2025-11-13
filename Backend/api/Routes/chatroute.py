from api.logic.llmchat import generateResponse
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

router = APIRouter()

class userQuery(BaseModel):
    currentQuery: str
    sessionId: str = None
    webSearch: bool = False


@router.post("/chatResponse", status_code=status.HTTP_201_CREATED)
async def chatResponse(query: userQuery):
    try:
        if not query.sessionId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session ID is required.")
        
        if query.webSearch:
            print("Web Search is enabled")
            # call the web search function
            # nedd to add the functionality
            # prolly dont need the else statement
        else:
            print("Web Search is disabled")
        chatResponse = await generateResponse(query.sessionId, query.currentQuery)
        return {"chatResponse": chatResponse}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
