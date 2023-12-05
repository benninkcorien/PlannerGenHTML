from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader
import readvars as thevars

startyear = thevars.startyear
startmonth = thevars.startmonth
howmanymonths = thevars.howmanymonths
start_date = datetime(startyear, startmonth, 1)
end_date = start_date + relativedelta(months=howmanymonths) - timedelta(days=1)
# Set up Jinja environment
env = Environment(loader=FileSystemLoader("templates"))


templates = ["02year/year_1.jinja", "02year/year_2.jinja"]

i = 1
for templ in templates:
    template = env.get_template(templ)

    file_name = f"year_{i}"

    # Render the template with the current date
    rendered = template.render()

    # Save to file
    with open(f"html/{file_name}.html", "w", encoding="utf-8") as file:
        file.write(rendered)
    i += 1
