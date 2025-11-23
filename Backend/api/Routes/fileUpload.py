from fastapi import APIRouter, status, HTTPException, UploadFile, File, Form
import pymupdf
import pymupdf4llm
from io import BytesIO
from pdf.textToMd import readDoc, create_chunks
from embedding.embed import embedDoc
from vectorDB.chromaDB.chroma import add_chunks
from typing import Annotated


router = APIRouter()

@router.post("/pdfUpload", status_code=status.HTTP_201_CREATED)
async def pdfUpload(pdfFile: Annotated[UploadFile, File()],sessionId: Annotated[str, Form()]):
    print(f"Filename: {pdfFile.filename} || Content Type: {pdfFile.content_type}")
    print("Session ID from file upload: ", sessionId)
    file_content = await pdfFile.read()
    # doc = 
    md = readDoc(file_content)
    print(md)
    chunks = create_chunks(md)
    print(chunks)
    print('starting embedding')
    num_chunks = await add_chunks(sessionId, chunks)
    print(f"Added {num_chunks} chunks to the database")
    # embeddings = await embedDoc(chunks)
    print('chunks added')
    # print(embeddings)
    # print(type(file_content))
    # fileObj = BytesIO(file_content)
    # doc = pymupdf.open(stream=fileObj)
    # md = pymupdf4llm.to_markdown(doc)
    # print(type(md))
    # print(md)
    return {"message": "PDF uploaded successfully"}