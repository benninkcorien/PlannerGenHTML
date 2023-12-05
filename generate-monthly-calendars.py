import calendar
from datetime import datetime, timedelta
import readvars as thevars

startyear = thevars.startyear
startmonth = thevars.startmonth
startday = thevars.startday
howmanymonths = thevars.howmanymonths

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def generate_calendar_html(startyear, startmonth, startday, howmanymonths):
    # Stary Day whould be either "Monday" or "Sunday"
    if startday not in ("Monday", "Sunday"):
        return "Invalid start day"

    # Initialize the calendar
    cal = calendar.Calendar(firstweekday=0 if startday == "Monday" else 6)

    for i in range(howmanymonths):
        current_year = startyear
        current_month = startmonth + i
        if current_month > 12:
            current_year += 1
            current_month -= 12

        month_name = month_names[current_month - 1]
        month_calendar = cal.monthdatescalendar(current_year, current_month)

        html = f"<h2>{month_name} {current_year}</h2>"
        html += "<table><tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>"

        for week in month_calendar:
            html += "<tr>"
            for day in week:
                if day.month == current_month:
                    html += f"<td>{day.day}</td>"
                else:
                    html += "<td></td>"
            html += "</tr>"

        html += "</table>"

        # Save the generated HTML to a file
        file_name = f"month_{startmonth + i}.html"
        with open(f"templates/{file_name}", "w", encoding="utf-8") as html_file:
            html_file.write(html)

        print(f"Calendar HTML for {month_name} {current_year} saved as '{file_name}'")


generate_calendar_html(startyear, startmonth, startday, howmanymonths)
