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
template = env.get_template("05daily/day.jinja")

# Create an array of all dates
allthedates = [
    start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)
]

# Render the template with all dates
rendered = template.render(allthedates=allthedates, timedelta=timedelta)

# Save to file
with open("html/dailies.html", "w", encoding="utf-8") as file:
    file.write(rendered)
