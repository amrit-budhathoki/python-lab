# Title: Sexy Prime Finder
# Finds "sexy primes" (prime pairs differing by 6) and displays them in a fun chart.
# Interesting because it combines number theory with visual representation of mathematical patterns.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_sexy_primes(limit):
    sexy_pairs = []
    for p in range(2, limit):
        if is_prime(p) and is_prime(p + 6):
            sexy_pairs.append((p, p + 6))
    return sexy_pairs

def print_sexy_chart(pairs):
    print("\n" + "="*60)
    print("🔥 SEXY PRIMES FOUND (differ by 6) 🔥")
    print("="*60)
    
    for smaller, larger in pairs:
        gap_visual = "─" * (larger - smaller - 6)
        bar_length = min(40, larger // 5)
        bar = "█" * bar_length
        print(f"{smaller:4d} {bar:40s} {larger:4d}")
    
    print("="*60)
    print(f"Total sexy prime pairs found: {len(pairs)}\n")
    
    # Group by decade and show stats
    decades = {}
    for p1, p2 in pairs:
        decade = (p1 // 10) * 10
        decades[decade] = decades.get(decade, 0) + 1
    
    print("Distribution by decade:")
    for decade in sorted(decades.keys()):
        count = decades[decade]
        chart = "★" * count
        print(f"{decade:4d}s: {chart} ({count})")

def bonus_cousin_primes(limit):
    """Cousin primes differ by 4 - find these too!"""
    cousin_pairs = []
    for p in range(2, limit):
        if is_prime(p) and is_prime(p + 4):
            cousin_pairs.append((p, p + 4))
    return cousin_pairs

# Main execution
if __name__ == "__main__":
    limit = 500
    
    sexy = find_sexy_primes(limit)
    print_sexy_chart(sexy)
    
    # Bonus: cousin primes
    cousins = bonus_cousin_primes(limit)
    print(f"As a bonus, found {len(cousins)} cousin prime pairs (differ by 4)")
    print(f"Examples: {cousins[:5]}")
    
    # Fun fact
    print(f"\n✨ Fun fact: Among the first {limit} numbers,")
    print(f"   there are {len(sexy)} sexy prime pairs and {len(cousins)} cousin prime pairs!")
