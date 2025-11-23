from fastapi import APIRouter, status, HTTPException, UploadFile
import pymupdf
import pymupdf4llm
import io

router = APIRouter()

@router.post("/pdfUpload", status_code=status.HTTP_201_CREATED)
async def pdfUpload(pdfFile: UploadFile):
    print(f"Filename: {pdfFile.filename} || Content Type: {pdfFile.content_type}")
    file_content = await pdfFile.read()
    fileObj = io.BytesIO(file_content)
    doc = pymupdf.open(stream=fileObj)
    md = pymupdf4llm.to_markdown(doc)
    print(type(md))
    print(md)
    return {"message": "PDF uploaded successfully"}