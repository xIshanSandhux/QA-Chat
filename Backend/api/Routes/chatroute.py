from api.logic.llmchat import generateResponse
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

router = APIRouter()

class userQuery(BaseModel):
    currentQuery: str
    sessionId: str = None


@router.post("/chatResponse", status_code=status.HTTP_201_CREATED)
async def chatResponse(query: userQuery):
    try:
        if not query.sessionId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session ID is required.")
        
        chatResponse = await generateResponse(query.sessionId, query.currentQuery)
        return {"chatResponse": chatResponse}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
