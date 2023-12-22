import os
import glob
from pathlib import Path

from borb.pdf import Document
from borb.pdf import PDF
from borb.toolkit.export.html_to_pdf.html_to_pdf import HTMLToPDF


html_dir = "testfiles"
pdf_dir = "borb"

os.makedirs(pdf_dir, exist_ok=True)

# Loop through all HTML files in the html_dir
for html_file in glob.glob(os.path.join(html_dir, "*.html")):
    base_name = os.path.basename(html_file).split(".")[0]
    pdf_file = os.path.join(pdf_dir, f"{base_name}.pdf")
    print(f"Working on {base_name}")

    # read entire markdown file
    html_str: str = ""
    with open(html_file, "r", encoding="utf-8") as md_file_handle:
        html_str = md_file_handle.read()

    # convert
    doc: Document = HTMLToPDF.convert_html_to_pdf(html_str)
    assert doc is not None

    # write
    with open(pdf_file, "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)
