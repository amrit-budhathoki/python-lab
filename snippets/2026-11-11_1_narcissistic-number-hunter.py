# Title: Narcissistic Number Hunter

# Finds all narcissistic numbers (Armstrong numbers) up to a given limit.
# A narcissistic number equals the sum of its own digits each raised to the power
# of the number of digits. They're rare mathematical gems that seem to "know" themselves!

def is_narcissistic(n):
    """Check if a number is narcissistic (Armstrong number)."""
    digits = str(n)
    num_digits = len(digits)
    digit_sum = sum(int(d) ** num_digits for d in digits)
    return digit_sum == n

def find_narcissistic_numbers(limit):
    """Find all narcissistic numbers up to the given limit."""
    narcissistic = []
    for num in range(1, limit):
        if is_narcissistic(num):
            narcissistic.append(num)
    return narcissistic

def visualize_narcissistic(n):
    """Show the breakdown of why a number is narcissistic."""
    digits = str(n)
    num_digits = len(digits)
    breakdown = " + ".join(f"{d}^{num_digits}" for d in digits)
    calculation = " + ".join(str(int(d) ** num_digits) for d in digits)
    result = sum(int(d) ** num_digits for d in digits)
    
    print(f"  {n}: {breakdown} = {calculation} = {result} ✓")

def main():
    limit = 10000
    narcissistic_nums = find_narcissistic_numbers(limit)
    
    print("=" * 50)
    print(f"Narcissistic Numbers (up to {limit})")
    print("=" * 50)
    print(f"\nFound {len(narcissistic_nums)} narcissistic numbers:\n")
    
    for num in narcissistic_nums:
        visualize_narcissistic(num)
    
    print("\n" + "=" * 50)
    print("Fun facts:")
    print(f"• There are only {len(narcissistic_nums)} narcissistic numbers below {limit}")
    print(f"• The largest known has 39 digits!")
    print(f"• Some are called 'pluperfect digital invariants'")
    print("=" * 50)

if __name__ == "__main__":
    main()
