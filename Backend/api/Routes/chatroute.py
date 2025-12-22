from api.logic.llmchat import generateResponse
from RAG.QueryRewrite.rewrite import rewriteQuery
from api.logic.searchlogic import searchPDF
from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

router = APIRouter()

class userQuery(BaseModel):
    currentQuery: str
    sessionId: str = None
    rag: bool = False

class searchPDFQuery(BaseModel):
    query: str
    sessionId: str
    fileName: str

@router.post("/chatResponse", status_code=status.HTTP_201_CREATED)
async def chatResponse(query: userQuery):
    try:
        if not query.sessionId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session ID is required.")
        
        if query.rag:
            chatResponse = await generateResponse(query.sessionId, query.currentQuery, query.rag)
        else:
            chatResponse = await generateResponse(query.sessionId, query.currentQuery)
        return {"chatResponse": chatResponse}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/searchpdf", status_code=status.HTTP_201_CREATED)
async def searchpdf(searchQuery: searchPDFQuery):
    try:
        if not searchQuery.sessionId or not searchQuery.fileName:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session ID and File Name are required.")
        
        rewrite = await rewriteQuery(searchQuery.query)
        searchresults = await searchPDF(rewrite, searchQuery.sessionId, searchQuery.fileName)
        return {"searchresults": searchresults}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
