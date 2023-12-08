import random
from jinja2 import Environment, FileSystemLoader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from PyPDF2 import PdfMerger
import io

env = Environment(
    loader=FileSystemLoader(r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\templates")
)

cover_images = ["cover1.jpg", "cover2.jpg", "cover3.jpg", "cover4.jpg"]
selected_cover = random.choice(cover_images)
cover_template = env.get_template("cover_page.html")
cover_html = cover_template.render(cover_image=selected_cover)

index_template = env.get_template("index_page.html")
index_html = index_template.render()

date_template = env.get_template("date_page.html")
current_date = datetime.now().strftime("%Y-%m-%d")
date_html = date_template.render(current_date=current_date)


cover_pdf = HTML(string=cover_html).write_pdf()
index_pdf = HTML(string=index_html).write_pdf()
date_pdf = HTML(string=date_html).write_pdf()

# Combine PDF pages
merger = PdfMerger()
for pdf in [cover_pdf, index_pdf, date_pdf]:
    # Convert each PDF byte stream to a BytesIO object
    pdf_stream = io.BytesIO(pdf)
    merger.append(pdf_stream)

# Write to a file
with open(
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\final_document.pdf",
    "wb",
    encoding="utf-8",
) as final_pdf:
    merger.write(final_pdf)

# Cleanup
merger.close()
