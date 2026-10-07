# Title: Gregorian Calendar Leap Year Paradox

# This program reveals the fascinating "leap second" and Gregorian calendar rules:
# Most years divisible by 4 are leap years, but century years must be divisible by 400.
# It visualizes the pattern showing years like 1900 and 2100 are NOT leap years despite being divisible by 4.

from datetime import datetime, timedelta
import calendar

def is_leap_gregorian(year):
    """Determine if a year is a leap year using Gregorian rules"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print("🗓️  GREGORIAN LEAP YEAR PARADOX\n")
print("=" * 50)

# Show the century paradox
century_years = [1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]
print("\nCentury Years (divisible by 100):")
print("-" * 50)
for year in century_years:
    is_leap = is_leap_gregorian(year)
    status = "✓ LEAP" if is_leap else "✗ NOT LEAP"
    divisible_400 = "÷400" if year % 400 == 0 else ""
    print(f"{year}: {status:12} {divisible_400}")

# Count leap years in a 400-year cycle (perfectly balanced!)
print("\n" + "=" * 50)
print("Leap years in 400-year cycle (1601-2000):")
leap_count = sum(1 for y in range(1601, 2001) if is_leap_gregorian(y))
print(f"Total: {leap_count} leap years out of 400")
print(f"Average year length: {400 + leap_count}/400 = {(400 + leap_count)/400:.5f} days")
print(f"Tropical year: 365.2425 days")
print(f"Match: {(400 + leap_count)/400 == 365.2425}")

# Show the pattern visually
print("\n" + "=" * 50)
print("Leap year pattern (20 years starting 1896):\n")
for year in range(1896, 1916):
    is_leap = is_leap_gregorian(year)
    marker = "🔵" if is_leap else "⚪"
    print(f"{marker} {year}", end="  ")
    if (year - 1895) % 4 == 0:
        print()

print("\n\n⚠️  Notice: 1900 breaks the 4-year pattern!\n")
