import os
import glob
from jinja2 import Environment, FileSystemLoader
import readvars as thevars

print(thevars.startyear)
base_dir = "templates"

env = Environment(loader=FileSystemLoader(base_dir))

# Path where the compiled HTML files will be saved
output_path = "html"
os.makedirs(output_path, exist_ok=True)

# Delete all old files
try:
    files = os.listdir(output_path)
    for file in files:
        file_path = os.path.join(output_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
except:
    pass


# Create new html files for all templates
for part_file in glob.glob(r"templates\*\*.html"):
    part_name = os.path.basename(part_file).split(".")[0]
    relative_path = os.path.relpath(part_file, base_dir)
    relative_path = relative_path.replace("\\", "/")

    template = env.get_template(relative_path)

    rendered_html = template.render()
    with open(
        os.path.join(output_path, f"{part_name}.html"), "w", encoding="utf-8"
    ) as file:
        file.write(rendered_html)

print("HTML files compiled successfully.")
