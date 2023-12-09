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

current_date = start_date
while current_date <= end_date:
    # Format date for filename
    file_name = current_date.strftime("%Y-%m-%d.html")

    # Format dates for previous and next buttons
    prev_date = (current_date - timedelta(days=1)).strftime("%Y-%m-%d")
    next_date = (current_date + timedelta(days=1)).strftime("%Y-%m-%d")

    # Render the template with the current date and all dates
    rendered = template.render(
        current_date=current_date.strftime("%Y-%m-%d"),
        current_day=current_date.strftime("%A"),
        current_month=current_date.strftime("%B"),
        prev_link=f"#{prev_date}",
        next_link=f"#{next_date}",
        allthedates=allthedates,
        timedelta=timedelta,
    )

    # Move to next day
    current_date += timedelta(days=1)

    # Save to file
    with open("html/dailies.html", "w", encoding="utf-8") as file:
        file.write(rendered)
