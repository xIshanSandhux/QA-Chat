import json
from vectorDB.chromaDB.chroma import getsearchPDFChunks


async def searchPDF(query: str, sessionId: str, fileName: str):

    try:
        relChunks = await getsearchPDFChunks(sessionId, fileName, query)
        print(relChunks)
    except Exception as e:
        raise ValueError(f"Error searching PDF: {e}")
