from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader
import readvars as thevars

startyear = thevars.startyear
# Set up Jinja environment
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("01index/index.jinja")

# Render the template with the startyear variable
rendered_template = template.render(startyear=startyear)

# Specify the output file path (change this to the desired path)
output_file_path = "html/index.html"

# Save the rendered template to an HTML file
with open(output_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(rendered_template)

print(f"Rendered template saved as {output_file_path}")
