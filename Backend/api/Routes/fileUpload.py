from fastapi import APIRouter, status, HTTPException, UploadFile, File, Form
from pdf.textToMd import readDoc, create_chunks
from vectorDB.chromaDB.chroma import add_chunks
from typing import Annotated, List
import asyncio


router = APIRouter()
async def chunkTasks(chunks: List[str],pageNumber: int, sessionId: str, fileName: str):
        await add_chunks(sessionId, chunks,pageNumber, fileName)

@router.post("/pdfUpload", status_code=status.HTTP_201_CREATED)
async def pdfUpload(pdfFile: Annotated[UploadFile, File()],sessionId: Annotated[str, Form()]):
    fileName = pdfFile.filename
    # print(fileName)
    if pdfFile.content_type != 'application/pdf':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File is not a PDF")

    file_content = await pdfFile.read()
    fileContent = readDoc(file_content)
    chunks = {}
    for pageNumber, pageContent in fileContent.items():
        chunks[pageNumber] = create_chunks(pageContent)

    # num_chunks = await add_chunks(sessionId, chunks)
    try:
        tasks = [chunkTasks(chunk, pageNumber, sessionId, fileName) for pageNumber, chunk in chunks.items()]
        await asyncio.gather(*tasks)
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return {"message": "Chunks added to the database", "curFile": fileName}



