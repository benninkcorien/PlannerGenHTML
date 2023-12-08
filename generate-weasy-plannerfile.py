import os
import glob
from weasyprint import HTML


def convert_html_to_pdf(html_file_path, output_pdf_path):
    # Load the HTML file
    HTML(html_file_path).write_pdf(output_pdf_path)


theplannerfile = r"F:\PlannerGenerator\PlannerGenHTML\html\planner_full_result.html"
thepdffile = r"F:\PlannerGenerator\PlannerGenHTML\weasy\theplanner_full.pdf"


# Loop through all HTML files in the html_dir
convert_html_to_pdf(theplannerfile, thepdffile)
