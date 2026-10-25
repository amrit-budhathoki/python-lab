# Title: The Doomsday Algorithm
# Calculates what day of the week any date falls on using John Conway's Doomsday Algorithm.
# Interesting because it's a mental math trick that works for any date in history!

from datetime import datetime, timedelta

def doomsday(year, month, day):
    """Calculate day of week using Conway's Doomsday Algorithm"""
    
    # Century anchor day (400-year cycle)
    century = year // 100
    anchor = (5 * (century % 4) + 2) % 7
    
    # Year code
    yr = year % 100
    y_code = (yr + yr // 4) % 7
    
    # Doomsday for each month (mnemonic: 4/4, 6/6, 8/8, 10/10, 12/12, and others)
    doomsdays = {
        1: 31,  # Jan 31
        2: 28 if not is_leap(year) else 29,  # Feb 28/29
        3: 7,   # Mar 7
        4: 4,   # Apr 4
        5: 9,   # May 9
        6: 6,   # Jun 6
        7: 11,  # Jul 11
        8: 8,   # Aug 8
        9: 5,   # Sep 5
        10: 10, # Oct 10
        11: 7,  # Nov 7
        12: 12  # Dec 12
    }
    
    dday = doomsdays[month]
    
    # Days from doomsday to target day
    offset = (day - dday) % 7
    
    # Final day of week calculation
    day_num = (anchor + y_code + offset) % 7
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[day_num]

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test with some famous dates and verify with Python's datetime
test_dates = [
    (1969, 7, 20, "Moon landing"),
    (1989, 11, 9, "Fall of Berlin Wall"),
    (2000, 1, 1, "Y2K"),
    (1582, 10, 15, "Gregorian calendar adoption"),
    (1776, 7, 4, "US Independence"),
]

print("=" * 60)
print("DOOMSDAY ALGORITHM - Historical Date Verification")
print("=" * 60)

for year, month, day, event in test_dates:
    calculated = doomsday(year, month, day)
    
    # Verify with datetime if possible (datetime only handles 1-9999)
    if 1 <= year <= 9999:
        actual = datetime(year, month, day).strftime("%A")
        match = "✓" if calculated == actual else "✗"
    else:
        actual = "?"
        match = "?"
    
    print(f"{event}")
    print(f"  Date: {month:02d}/{day:02d}/{year}")
    print(f"  Calculated: {calculated:9s} | Actual: {actual:9s} {match}")
    print()
