# Title: Emirp Explorer

# Find emirps (primes that spell different primes backwards) and visualize their distribution.
# Emirps are a fun mathematical curiosity that combine digit reversal with primality testing.

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

def reverse_number(n):
    return int(str(n)[::-1])

def is_emirp(n):
    if not is_prime(n):
        return False
    reversed_n = reverse_number(n)
    if reversed_n == n:  # palindromic primes don't count
        return False
    return is_prime(reversed_n)

emirps = []
for num in range(2, 10000):
    if is_emirp(num):
        emirps.append(num)

print("╔════════════════════════════════════════╗")
print("║          EMIRP EXPLORER REPORT         ║")
print("╚════════════════════════════════════════╝\n")
print(f"Found {len(emirps)} emirps below 10,000\n")

# Show the first 20
print("First 20 emirps:")
for i, e in enumerate(emirps[:20], 1):
    rev = reverse_number(e)
    print(f"  {i:2d}. {e:4d} ↔ {rev:4d}")

print(f"\n... and {max(0, len(emirps) - 20)} more!\n")

# Distribution by decade
print("Distribution by decade:")
decades = {}
for e in emirps:
    decade = (e // 10) * 10
    decades[decade] = decades.get(decade, 0) + 1

for decade in sorted(decades.keys())[:15]:
    count = decades[decade]
    bar = "█" * count
    print(f"  {decade:4d}-{decade+9:4d}: {bar} ({count})")

# Interesting stats
print(f"\nLargest emirp below 10,000: {emirps[-1]}")
print(f"Average emirp value: {sum(emirps) // len(emirps)}")
print(f"Emirps with all different digits:")
all_diff = [e for e in emirps if len(set(str(e))) == len(str(e))]
print(f"  Found {len(all_diff)}: {all_diff[:10]}")
