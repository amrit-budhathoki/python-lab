# Title: The Eternal September Calendar

# In 1993, AOL gave free trial CDs to everyone, bringing millions of newbies
# to Usenet. The joke "It's always September" was born because the newbies
# never left, making it feel like an endless September. This visualizes a
# calendar frozen in that eternal September 1993, showing the oddity of
# a month that never ends.

from datetime import datetime, timedelta
import calendar

def print_eternal_september():
    # September 1993 - the month that never ended
    year = 1993
    month = 9
    
    print("\n" + "="*50)
    print("       🌐 ETERNAL SEPTEMBER 1993 🌐".center(50))
    print("="*50)
    print("\n(The month Usenet never recovered from)\n")
    
    # Get calendar for September 1993
    cal = calendar.monthcalendar(year, month)
    
    # Print header
    print("September 1993".center(50))
    print("-" * 50)
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    # Print calendar
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "  . "
            else:
                week_str += f" {day:2} "
        print(week_str)
    
    print("-" * 50)
    
    # Calculate what "today" would be if we're still in Sept 1993
    # Assume we're starting from Sept 1, keep wrapping through Sept
    days_since_1993 = (datetime.now() - datetime(1993, 9, 1)).days
    eternal_day = (days_since_1993 % 30) + 1
    
    print(f"\nDays elapsed since September began: {days_since_1993}")
    print(f"If you're still in September 1993:")
    print(f"You'd be on September {eternal_day}, 1993 (repeating endlessly)")
    
    # Show the irony
    print(f"\nActual date today: {datetime.now().strftime('%B %d, %Y')}")
    print(f"Usenet time: September {eternal_day}, 1993")
    
    # Calculate how many times September has cycled
    cycles = days_since_1993 // 30
    print(f"\nSeptember has repeated {cycles:,} times!")
    print(f"That's {cycles * 30 / 365:.1f} years of eternal Septembers\n")
    
    print("="*50)

print_eternal_september()
