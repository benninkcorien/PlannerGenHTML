import random
from jinja2 import Environment, FileSystemLoader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from reportlab.lib.utils import ImageReader

# Setup Jinja environment
env = Environment(
    loader=FileSystemLoader(r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\templates")
)

# Render templates
cover_images = ["cover1.jpg", "cover2.jpg", "cover3.jpg", "cover4.jpg"]
selected_cover = random.choice(cover_images)

# Initialize ReportLab Canvas
c = canvas.Canvas(
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\final_document.pdf", pagesize=letter
)
width, height = letter

# Draw the cover page
cover_image_path = (
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\images\\" + selected_cover
)
cover_image = ImageReader(cover_image_path)
c.drawImage(cover_image, 0, 0, width=width, height=height)
c.showPage()

# Draw the index page
link_texts = ["Page 2", "Page 3", "Page 4", "Page 5"]
y_position = height - 100
for i, text in enumerate(link_texts, start=2):
    c.drawString(100, y_position, text)
    c.addOutlineEntry(text, f"dest_page_{i}", level=0, closed=None)
    y_position -= 20

c.showPage()

# Add destinations to each page and draw content
for i in range(2, 6):
    c.bookmarkPage(f"dest_page_{i}")
    c.drawString(100, height - 100, f"Page {i}")
    if i == 3:
        current_date = datetime.now().strftime("%Y-%m-%d")
        c.drawString(100, height - 120, f"Current Date: {current_date}")
    c.showPage()

# Save the PDF
c.save()
