import os
from io import BytesIO
from xhtml2pdf import pisa


def convert_html_to_pdf(source_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(".html"):
            html_file_path = os.path.join(source_folder, filename)
            pdf_file_name = os.path.splitext(filename)[0] + ".pdf"
            pdf_file_path = os.path.join(output_folder, pdf_file_name)

            with open(html_file_path, "r", encoding="utf-8") as html_file:
                html = html_file.read()
                result_file = open(pdf_file_path, "w+b")
                pisa_status = pisa.CreatePDF(
                    BytesIO(html.encode("utf-8")), dest=result_file
                )

                # Close the PDF object cleanly.
                result_file.close()


source_folder = "html"
output_folder = "plannerfile"
convert_html_to_pdf(source_folder, output_folder)
