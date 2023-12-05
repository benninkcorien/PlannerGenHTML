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
template = env.get_template("05daily/day.html")


current_date = start_date
while current_date <= end_date:
    # Format date for filename
    file_name = current_date.strftime("%Y-%m-%d-%A-%B.html")

    # Format dates for previous and next buttons
    prev_date = (current_date - timedelta(days=1)).strftime("%Y-%m-%d-%A-%B.html")
    next_date = (current_date + timedelta(days=1)).strftime("%Y-%m-%d-%A-%B.html")

    # Render the template with the current date
    rendered = template.render(
        current_date=current_date.strftime("%Y-%m-%d"),
        current_day=current_date.strftime("%A"),
        current_month=current_date.strftime("%B"),
        prev_link=prev_date,
        next_link=next_date,
    )

    # Save to file
    with open(f"dailyhtml/{file_name}", "w", encoding="utf-8") as file:
        file.write(rendered)

    # Move to next day
    current_date += timedelta(days=1)
