import datetime

# Get user input for birth date
while True:
    try:
        birth_day = int(input("Which date were you born on? "))
        birth_month = int(input("Which month were you born in? "))
        birth_year = int(input("Which year were you born in? "))
        # Validate the date
        datetime.date(birth_year, birth_month, birth_day)
        break
    except ValueError:
        print("Invalid date. Please enter a valid date.")

try:
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    today = datetime.date.today()

    # Calculate age in years, months, days
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        # Get days in previous month
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (datetime.date(prev_year, prev_month % 12 + 1, 1) - datetime.timedelta(days=1)).day
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("Invalid date entered.")