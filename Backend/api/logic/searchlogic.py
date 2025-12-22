import json
from vectorDB.chromaDB.chroma import getsearchPDFChunks


async def searchPDF(query: str, sessionId: str, fileName: str):

    try:
        relChunks = await getsearchPDFChunks(sessionId, fileName, query)
        # print(relChunks)
        metadata = relChunks["metadatas"][0]
        chunks = relChunks["documents"][0]

        results = [{"page": metadata[x]["pageNumber"], "data": chunks[x]} for x in range(len(metadata))]
        # print("----------  Results  ----------")
        # print(results)
        return results
    except Exception as e:
        raise ValueError(f"Error searching PDF: {e}")
