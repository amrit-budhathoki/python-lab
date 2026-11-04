# Title: The Week Numbering Paradox

# ISO 8601 week numbers can make dates behave strangely: some dates belong to
# the previous or next year's week numbering! This explores those oddities by
# finding all dates in a year where the ISO week year differs from calendar year.

from datetime import date, timedelta

def find_week_numbering_oddities(year):
    """Find dates where ISO week year differs from calendar year."""
    oddities = []
    
    # Check entire year plus buffer for edge cases
    start = date(year - 1, 12, 15)
    end = date(year + 1, 1, 15)
    current = start
    
    while current <= end:
        iso_year, iso_week, iso_day = current.isocalendar()
        calendar_year = current.year
        
        if iso_year != calendar_year:
            oddities.append((current, iso_year, iso_week))
        
        current += timedelta(days=1)
    
    return oddities

def main():
    print("🗓️  ISO WEEK NUMBERING PARADOX\n")
    print("Dates where the ISO week year differs from the calendar year:\n")
    
    for target_year in [2024, 2025, 2026]:
        oddities = find_week_numbering_oddities(target_year)
        
        print(f"Year {target_year}:")
        print(f"  Found {len(oddities)} dates with paradoxical week numbering\n")
        
        # Group by calendar month
        by_month = {}
        for date_obj, iso_year, iso_week in oddities:
            month = date_obj.month
            if month not in by_month:
                by_month[month] = []
            by_month[month].append((date_obj, iso_year, iso_week))
        
        for month in sorted(by_month.keys()):
            dates = by_month[month]
            month_name = date(2024, month, 1).strftime("%B")
            print(f"  {month_name}:")
            
            for date_obj, iso_year, iso_week in dates[:3]:  # Show first 3
                day_name = date_obj.strftime("%A")
                print(f"    {date_obj} ({day_name}) → ISO week {iso_week} of {iso_year}")
            
            if len(dates) > 3:
                print(f"    ... and {len(dates) - 3} more")
            print()
        
        print()
    
    # Explain the phenomenon
    print("Why this happens:")
    print("  • ISO 8601 weeks always start on Monday and end on Sunday")
    print("  • Week 1 is the first week with a Thursday in it")
    print("  • December 29-31 might belong to week 1 of next year")
    print("  • January 1-3 might belong to week 1 of previous year")

if __name__ == "__main__":
    main()
