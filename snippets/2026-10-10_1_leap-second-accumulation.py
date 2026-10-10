# Title: Leap Second Accumulation

# This program shows how leap seconds accumulate over time and when they occur.
# It's interesting because leap seconds are a quirky real-world adjustment to keep
# UTC aligned with Earth's rotation, and we visualize the cumulative drift they prevent.

from datetime import datetime, timedelta
import calendar

# Known leap seconds (inserted at end of June 30 or Dec 31)
# Format: (year, month, cumulative_count)
leap_seconds = [
    (1972, 6, 1), (1972, 12, 2), (1973, 12, 3), (1974, 12, 4), (1975, 12, 5),
    (1976, 12, 6), (1977, 12, 7), (1978, 12, 8), (1979, 12, 9), (1981, 6, 10),
    (1982, 6, 11), (1983, 6, 12), (1985, 6, 13), (1987, 12, 14), (1989, 12, 15),
    (1990, 12, 16), (1992, 6, 17), (1993, 6, 18), (1994, 6, 19), (1995, 12, 20),
    (1997, 6, 21), (1998, 12, 22), (2005, 12, 23), (2008, 12, 24), (2012, 6, 25),
    (2015, 6, 26), (2016, 12, 27), (2020, 12, 28), (2022, 6, 29),
]

print("╔════════════════════════════════════════════════════════════════╗")
print("║          LEAP SECOND ACCUMULATION OVER TIME                    ║")
print("╚════════════════════════════════════════════════════════════════╝\n")

# Calculate total seconds that would have drifted without leap seconds
base_year = 1972
current_year = 2024
years_elapsed = current_year - base_year
theoretical_drift = years_elapsed * 0.0016  # ~1.6ms per year average

print(f"Without leap seconds, UTC would drift by ~{theoretical_drift:.3f} seconds")
print(f"from Earth's actual rotation in {years_elapsed} years.\n")

print("Leap Seconds Inserted:")
print("─" * 60)

last_year = 0
for year, month, count in leap_seconds:
    month_name = calendar.month_name[month]
    end_day = 30 if month == 6 else 31
    
    # Show gaps between leap seconds
    if last_year > 0 and year - last_year > 2:
        gap = year - last_year
        print(f"  └─ {gap}-year gap\n")
    
    print(f"  {count:2d}. {month_name:9s} {end_day}, {year} → {count} second{'s' if count > 1 else ''} total")
    last_year = year

# Calculate average interval
intervals = [leap_seconds[i+1][0] - leap_seconds[i][0] for i in range(len(leap_seconds)-1)]
avg_interval = sum(intervals) / len(intervals)

print("\n" + "─" * 60)
print(f"\nTotal leap seconds inserted: {leap_seconds[-1][2]}")
print(f"Average interval between insertions: {avg_interval:.1f} years")
print(f"Current UTC offset from TAI: -{leap_seconds[-1][2]} seconds")

# Fun fact
print("\n" + "╔════════════════════════════════════════════════════════════════╗")
print("║ 🤓 FUN FACT: The earliest leap second was June 30, 1972.        ║")
print("║    Earth's rotation is slowing by ~2.3ms per century due to      ║")
print("║    tidal friction. At this rate, we'd need a leap second every   ║")
print(f"║    ~{1/0.0016:.0f} years without them!                                    ║")
print("╚════════════════════════════════════════════════════════════════╝")
