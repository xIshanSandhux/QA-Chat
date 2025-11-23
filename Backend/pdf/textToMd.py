from io import BytesIO
import pymupdf4llm as pdf
import pymupdf
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

def readDoc(file: bytes):
    fileObj = BytesIO(file)
    doc = pymupdf.open(stream=fileObj)
    md = pdf.to_markdown(doc)
    return md

def create_chunks(doc: str):
    chunks = [doc[i:i+2000] for i in range(0, len(doc), 2000)]
    return chunks



    