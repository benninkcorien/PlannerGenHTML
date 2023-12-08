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

thehtmlfile = r"F:\PlannerGenerator\PlannerGenHTML\00test-one-file\test.html"
thepfdfile = r"F:\PlannerGenerator\PlannerGenHTML\00test-one-file\output\test.pdf"


convert_html_to_pdf(thehtmlfile, thepfdfile)
