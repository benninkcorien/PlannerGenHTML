import pdfkit

# List of HTML files
html_files = [
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\cover.html",
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\index.html",
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\year_1.html",
]

# Output PDF file
output_pdf = r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\pdfkitoutput.pdf"

# Convert HTML to PDF
pdfkit.from_file(html_files, output_pdf)
