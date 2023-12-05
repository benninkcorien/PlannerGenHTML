from io import BytesIO
from xhtml2pdf import pisa
import os

# Define your custom page size here
# custom_page_size = (150 * mm, 150 * mm)  # Convert millimeters to points


# Create a BytesIO buffer to hold the PDF data
# buffer = BytesIO()

# # Convert the HTML/CSS template to a PDF using xhtml2pdf and store it in the buffer
# with open("test.html", "r", encoding="utf-8") as html_file:
#     html = html_file.read()

# pisa_status = pisa.CreatePDF(html, dest=buffer)

# # Check if there was an error in conversion
# if pisa_status.err:
#     raise Exception("An error occurred while generating the PDF")

# # Get the PDF data from the buffer
# pdf_data = buffer.getvalue()
# buffer.close()

# # Write the PDF data to a file or return it as needed
# with open("test.pdf", "wb") as f:
#     f.write(pdf_data)


# Create an output buffer for the PDF
buffer = BytesIO()

# Specify the path to the /html folder
html_folder = r"F:\PlannerGenerator\PlannerGenHTML\html"

# Get a list of HTML files in the folder
html_files = [
    os.path.join(html_folder, filename)
    for filename in os.listdir(html_folder)
    if filename.endswith(".html")
]

# Sort the HTML files by filename
html_files.sort()

# Iterate through HTML files and add each page to the PDF
for html_file_path in html_files:
    with open(html_file_path, "r", encoding="utf-8") as html_file:
        html = html_file.read()

    # Add a page break if this is not the first page
    if buffer.tell() > 0:
        buffer.write(b"<pagebreak>")

    # Convert the HTML page to PDF and append it to the buffer
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    # Check if there was an error in conversion
    if pisa_status.err:
        raise Exception("An error occurred while generating the PDF")

# Save the combined PDF to a file
with open("plannerfile/combined.pdf", "wb") as pdf_file:
    pdf_file.write(buffer.getvalue())

# Close the buffer
buffer.close()

print("Combined PDF generated as 'combined.pdf'")
