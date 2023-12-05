import os
import glob
from weasyprint import HTML


def convert_html_to_pdf(html_file_path, output_pdf_path):
    # Load the HTML file
    HTML(html_file_path).write_pdf(output_pdf_path)


# Test 1 file
# html_file = "html/monthly_page_1.html"
# pdf_file = "weasy/test.pdf"
# convert_html_to_pdf(html_file, pdf_file)

html_dir = "html"
pdf_dir = "weasy"

os.makedirs(pdf_dir, exist_ok=True)

# Loop through all HTML files in the html_dir
for html_file in glob.glob(os.path.join(html_dir, "*.html")):
    base_name = os.path.basename(html_file).split(".")[0]
    pdf_file = os.path.join(pdf_dir, f"{base_name}.pdf")
    convert_html_to_pdf(html_file, pdf_file)
