import os
from pypdf import PdfWriter

merger = PdfWriter()

pdf_folder = "pdffiles"
pdf_files = [
    os.path.join(pdf_folder, filename)
    for filename in os.listdir(pdf_folder)
    if filename.endswith(".pdf")
]
for pdf in pdf_files:
    merger.append(pdf)

merger.write("00planner/planner.pdf")
merger.close()
