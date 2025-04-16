import datetime
import calendar

# Countdown till a future date (e.g. exam date)
today = datetime.date.today()
exam_date = datetime.date(2025, 6, 1)
days_left = (exam_date - today).days
print(f"Days left for exam: {days_left} days")

# Date formatting
now = datetime.datetime.now()
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("Formatted DateTime:", formatted)

# Checking leap year
year = 2028
if calendar.isleap(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
