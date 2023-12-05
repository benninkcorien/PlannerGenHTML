import os
import glob
from weasyprint import HTML


def combine_html_files(directory):
    combined_html = "<html><head><style> .page-break { page-break-before: always; }</style></head><body>"
    first_file = True
    for html_file in glob.glob(os.path.join(directory, "*.html")):
        with open(html_file, "r", encoding="utf-8") as file:
            content = file.read()
            if first_file:
                first_file = False
            else:
                combined_html += '<div class="page-break"></div>'
            combined_html += content
    combined_html += "</body></html>"
    return combined_html


html_dir = "html"
output_pdf = "weasy/combinedhtml.pdf"

combined_html = combine_html_files(html_dir)
HTML(string=combined_html).write_pdf(output_pdf)
