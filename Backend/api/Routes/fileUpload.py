from fastapi import APIRouter, status, HTTPException, UploadFile


router = APIRouter()

@router.post("/pdfUpload", status_code=status.HTTP_201_CREATED)
async def pdfUpload(pdfFile: UploadFile):
    print(f"Filename: {pdfFile.filename} || Content Type: {pdfFile.content_type}")
    file_content = await pdfFile.read()
    print(file_content)
    return {"message": "PDF uploaded successfully"}