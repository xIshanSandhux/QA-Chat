from fastapi import APIRouter, status, HTTPException, UploadFile, File, Form
from pdf.textToMd import readDoc, create_chunks
from vectorDB.chromaDB.chroma import add_chunks
from typing import Annotated


router = APIRouter()

@router.post("/pdfUpload", status_code=status.HTTP_201_CREATED)
async def pdfUpload(pdfFile: Annotated[UploadFile, File()],sessionId: Annotated[str, Form()]):
    file_content = await pdfFile.read()
    md = readDoc(file_content)
    chunks = create_chunks(md)
    num_chunks = await add_chunks(sessionId, chunks)
    if num_chunks==0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No chunks added to the database")
    return {"message": f"Added {num_chunks} chunks to the database"}   