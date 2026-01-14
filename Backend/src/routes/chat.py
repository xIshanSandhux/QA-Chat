from src.controllers.chatController import generateResponse
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel, ValidationError

router = APIRouter()

class userQuery(BaseModel):
    currentQuery: str = "Empty"
    sessionId: str = "Empty"

@router.post("/chatResponse",status_code=status.HTTP_201_CREATED)
async def chatResponse(query: userQuery):
    try:
        if query.sessionId=="Empty":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Session ID.")
        if query.currentQuery=="Empty":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Query")
        chatRes = await generateResponse(query.sessionId,query.currentQuery)
        return {"sessionId": query.sessionId,"chatResponse": chatRes}
    
    except ValidationError as e:
        print(f"Input error by user while calling the chat response")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        print(f"Error occured while the user called the chat response endpoint: {str(e)}")
        raise HTTPException(status_code=500,detail=str(e))