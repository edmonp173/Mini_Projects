import calendar
def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:")
    print(cal)

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

print_calendar(year, month)