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

doc = pymupdf.open("sample_two_page.pdf")

print(pdf.to_markdown(doc,page_chunks=True))
# for page in doc:
    # print(page)
    # print("--------------------------------")
# print(doc[6])

    