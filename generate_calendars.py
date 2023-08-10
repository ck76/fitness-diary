import calendar

def generate_year_calendar(year):
    year_calendar = ""

    for month in range(1, 13):
        month_calendar = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]
        year_calendar += f"#### {month_name}\n\n"
        year_calendar += "|  Mon(月) | Tue(火) | Wed(水) | Thu(木) | Fri(金) | Sat(土) | Sun(日) |\n"
        year_calendar += "| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |\n"

        for week in month_calendar:
            week_row = "|"
            for day in week:
                if day == 0:
                    week_row += "         |"
                else:
                    week_row += f"    {day:2d}    |"
            year_calendar += week_row + "\n"

        year_calendar += "\n"

    return year_calendar

def save_calendar_to_file(year, calendar_data):
    filename = f"{year}.md"
    with open(filename, "w") as file:
        file.write(calendar_data)

start_year = 2024
end_year = 2099  # Change this to the desired end year

for year in range(start_year, end_year + 1):
    year_calendar_md = generate_year_calendar(year)
    save_calendar_to_file(year, year_calendar_md)
    print(f"Generated {year}.md")

print("Generation complete!")
