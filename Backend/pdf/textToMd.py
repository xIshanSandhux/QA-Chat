from io import BytesIO
import pymupdf4llm as pdf
import pymupdf
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from embedding.embed import embedDoc

sample_pdf_10_lines = b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << >> >>
endobj
4 0 obj
<< /Length 520 >>
stream
BT
/F1 18 Tf 50 780 Td (Sample PDF Document) Tj
0 -30 Td /F1 14 Tf (Section 1) Tj
0 -30 Td /F1 12 Tf (This is a test line number 1.) Tj
0 -20 Td (This is a test line number 2.) Tj
0 -20 Td (This is a test line number 3.) Tj
0 -20 Td (This is a test line number 4.) Tj
0 -20 Td (This is a test line number 5.) Tj
0 -20 Td (This is a test line number 6.) Tj
0 -20 Td (This is a test line number 7.) Tj
0 -20 Td (This is a test line number 8.) Tj
0 -20 Td (This is a test line number 9.) Tj
0 -20 Td (This is a test line number 10.) Tj
ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000010 00000 n 
0000000053 00000 n 
0000000102 00000 n 
0000000213 00000 n 
trailer
<< /Root 1 0 R /Size 5 >>
startxref
730
%%EOF"""


fileObj = BytesIO(sample_pdf_10_lines)

doc = pymupdf.open('CoverLetter.pdf')
md = pdf.to_markdown(doc)
# md = pdf.to_markdown(doc)
print(md)
print(type(md))
print(len(md))
chunks = [md[i:i+2000] for i in range(0, len(md), 2000)]
embeddings = embedDoc(chunks)
print(len(embeddings))
print(type(embeddings))
# print(len(chunks))
# print(chunks)




    