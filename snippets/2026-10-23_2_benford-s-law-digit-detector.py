# Title: Benford's Law Digit Detector

# Benford's Law states that in many real-world datasets, the first digit is more
# likely to be small (1 appears ~30% of the time, 2 appears ~18%, etc). This program
# demonstrates the law by analyzing factorials and comparing observed vs expected frequencies.

import math
from collections import Counter

def first_digit(n):
    """Extract the first digit of a number."""
    return int(str(n)[0])

def benford_expected():
    """Return expected frequencies according to Benford's Law."""
    return {d: math.log10(1 + 1/d) for d in range(1, 10)}

def analyze_sequence(generator, count=1000):
    """Analyze first digits in a sequence of numbers."""
    digits = [first_digit(generator(i)) for i in range(1, count + 1)]
    return Counter(digits)

def print_comparison(observed, expected, title):
    """Display comparison between observed and expected frequencies."""
    print(f"\n{title}")
    print("-" * 60)
    print(f"{'Digit':<8} {'Observed %':<18} {'Expected %':<18} {'Diff':<10}")
    print("-" * 60)
    
    total = sum(observed.values())
    chi_squared = 0
    
    for digit in range(1, 10):
        obs_freq = (observed.get(digit, 0) / total) * 100
        exp_freq = expected[digit] * 100
        diff = obs_freq - exp_freq
        chi_squared += ((observed.get(digit, 0) - total * expected[digit]) ** 2) / (total * expected[digit])
        print(f"{digit:<8} {obs_freq:<18.2f} {exp_freq:<18.2f} {diff:+.2f}%")
    
    print("-" * 60)
    print(f"Chi-squared statistic: {chi_squared:.2f}")
    return chi_squared < 20  # Rough threshold for "fits Benford's Law"

# Main analysis
print("=" * 60)
print("BENFORD'S LAW ANALYSIS")
print("=" * 60)

expected = benford_expected()

# Test 1: Factorials
observed_factorial = analyze_sequence(lambda i: math.factorial(i), 1000)
fits1 = print_comparison(observed_factorial, expected, "Test 1: Factorials (n!)")

# Test 2: Powers of 2
observed_powers = analyze_sequence(lambda i: 2 ** i, 1000)
fits2 = print_comparison(observed_powers, expected, "Test 2: Powers of 2 (2^n)")

# Test 3: Fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

observed_fib = analyze_sequence(fibonacci, 500)
fits3 = print_comparison(observed_fib, expected, "Test 3: Fibonacci Numbers")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Factorials follow Benford's Law: {'✓ Yes' if fits1 else '✗ No'}")
print(f"Powers of 2 follow Benford's Law: {'✓ Yes' if fits2 else '✗ No'}")
print(f"Fibonacci follows Benford's Law: {'✓ Yes' if fits3 else '✗ No'}")
print("\nBenford's Law appears in natural datasets because they span")
print("multiple orders of magnitude with logarithmic distribution!")
