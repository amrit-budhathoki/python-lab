# Title: The International Fixed Calendar Oddity

# Explores the fascinating International Fixed Calendar proposal from 1902,
# which would have made every month exactly 4 weeks (28 days) and every year
# perfectly symmetrical. Shows how different today's date would be and reveals
# the calendar's peculiar 13-month structure that was almost adopted globally.

from datetime import datetime, timedelta

def gregorian_to_fixed_calendar(date):
    """Convert a Gregorian date to International Fixed Calendar format."""
    year_start = datetime(date.year, 1, 1)
    days_since_start = (date - year_start).days
    
    # Month is 28 days, plus 1 extra day (Dec 31) that doesn't belong to any month
    month = (days_since_start // 28) + 1
    day = (days_since_start % 28) + 1
    
    # Handle leap year day (June 29 would be "Leap Day" between months 6 and 7)
    is_leap = date.year % 4 == 0 and (date.year % 100 != 0 or date.year % 400 == 0)
    
    if days_since_start == 364 or (is_leap and days_since_start == 365):
        return (13, 29, "Year Day")  # Dec 31 or leap day
    
    if is_leap and days_since_start >= 160:
        if days_since_start == 160:
            return (6, 29, "Leap Day")
        days_since_start -= 1
    
    month = (days_since_start // 28) + 1
    day = (days_since_start % 28) + 1
    
    return (month, day, None)

# Month names in the International Fixed Calendar
fixed_months = [
    "Januarius", "Februarius", "Martius", "Aprilis", "Maius", "Junius",
    "Quintilis", "Sextilis", "Septilis", "Octilis", "Novembris",
    "Decembris", "Undecimilis"
]

today = datetime.now()
fixed_month, fixed_day, special = gregorian_to_fixed_calendar(today)

print("=" * 60)
print("INTERNATIONAL FIXED CALENDAR COMPARISON")
print("=" * 60)
print(f"\nToday in Gregorian Calendar: {today.strftime('%A, %B %d, %Y')}")
print(f"\nToday in Fixed Calendar:")

if special:
    print(f"  {special} of {today.year}")
else:
    print(f"  {fixed_months[fixed_month-1]} {fixed_day}, {today.year}")

print("\n" + "=" * 60)
print("WHY THIS MATTERS:")
print("=" * 60)
print("""
• Every month has EXACTLY 28 days (4 perfect weeks)
• The year has 13 months of equal length
• Each date always falls on the same weekday every year
• No "broken" weeks that span months
• Only the Year Day (Dec 31) and Leap Day break the pattern
• Proposed in 1902, nearly adopted by the League of Nations
• Would have eliminated calendar chaos forever!
""")

print("Fixed Calendar Structure:")
for i, month in enumerate(fixed_months):
    print(f"  Month {i+1:2d}: {month:15s} (Days {i*28+1:3d}-{(i+1)*28:3d})")

days_until_year_end = (datetime(today.year + 1, 1, 1) - today).days
print(f"\nDays until Year Day (Dec 31): {days_until_year_end}")
