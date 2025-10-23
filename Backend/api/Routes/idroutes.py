from api.logic.idgen import session_id_gen
from fastapi import APIRouter, status, HTTPException

router = APIRouter()

@router.post("/sessionIdGen", status_code=status.HTTP_201_CREATED)
async def sessionIdGen():
    try:
        id = await session_id_gen()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    return {"sessionId": id}

