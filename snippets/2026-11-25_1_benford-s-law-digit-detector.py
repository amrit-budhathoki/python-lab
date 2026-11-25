# Title: Benford's Law Digit Detector

# Benford's Law states that in many real-world datasets, the first digit follows a
# specific logarithmic distribution (1 appears ~30% of the time, 2 ~18%, etc).
# This program generates various sequences and checks if they obey this curious law.

import math
from collections import Counter

def get_first_digit(n):
    """Extract the first digit of a positive number."""
    return int(str(abs(n))[0])

def benford_expected():
    """Calculate expected Benford's Law distribution."""
    return {d: math.log10(1 + 1/d) * 100 for d in range(1, 10)}

def analyze_sequence(name, numbers):
    """Analyze first digit distribution of a sequence."""
    digits = [get_first_digit(n) for n in numbers if n > 0]
    counts = Counter(digits)
    
    print(f"\n{name}:")
    print("Digit | Observed | Expected | Match")
    print("-" * 40)
    
    expected = benford_expected()
    matches = 0
    
    for digit in range(1, 10):
        observed = (counts.get(digit, 0) / len(digits)) * 100 if digits else 0
        exp = expected[digit]
        match = "✓" if abs(observed - exp) < 5 else "✗"
        if match == "✓":
            matches += 1
        print(f"{digit:5d} | {observed:8.1f}% | {exp:8.1f}% | {match}")
    
    print(f"Match ratio: {matches}/9")
    return matches

# Generate various sequences
# Fibonacci numbers
fibs = [1, 1]
for _ in range(100):
    fibs.append(fibs[-1] + fibs[-2])

# Powers of 2
powers_of_2 = [2**i for i in range(50)]

# Factorials
factorials = [1]
for i in range(1, 21):
    factorials.append(factorials[-1] * i)

# Prime-like sequence (multiples of integers)
multiples = [i * j for i in range(1, 15) for j in range(1, 20)]

# Random numbers (should NOT follow Benford's)
import random
random.seed(42)
random_nums = [random.randint(1, 10000) for _ in range(500)]

# Run analysis
print("=" * 50)
print("BENFORD'S LAW DETECTOR")
print("=" * 50)

results = []
results.append(analyze_sequence("Fibonacci Sequence", fibs))
results.append(analyze_sequence("Powers of 2", powers_of_2))
results.append(analyze_sequence("Factorials", factorials))
results.append(analyze_sequence("Integer Multiples", multiples))
results.append(analyze_sequence("Random Numbers", random_nums))

print("\n" + "=" * 50)
print("SUMMARY: Natural sequences tend to follow Benford's Law,")
print("while uniform random numbers do not. This reveals the hidden")
print("mathematical structure in real-world data!")
print("=" * 50)
