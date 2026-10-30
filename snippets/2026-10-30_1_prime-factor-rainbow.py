# Title: Prime Factor Rainbow

# Generates colorful ASCII art by visualizing the prime factorization patterns
# of numbers. Each prime gets a unique symbol, creating beautiful repeating
# patterns that reveal the hidden structure of integers.

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def factorization_signature(n):
    if n <= 1:
        return ""
    factors = prime_factors(n)
    unique_primes = sorted(set(factors))
    prime_to_symbol = {p: chr(ord('A') + i) for i, p in enumerate(unique_primes)}
    return ''.join(prime_to_symbol[f] for f in factors)

def get_color(prime):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    return colors[prime % len(colors)]

def colored_signature(n):
    if n <= 1:
        return " "
    factors = prime_factors(n)
    reset = '\033[0m'
    unique_primes = sorted(set(factors))
    prime_to_symbol = {p: chr(ord('A') + i) for i, p in enumerate(unique_primes)}
    
    result = ""
    for f in factors:
        symbol = prime_to_symbol[f]
        result += get_color(f) + symbol + reset
    return result

print("\n" + "="*60)
print("PRIME FACTOR RAINBOW - Numbers 1 to 100")
print("="*60 + "\n")

for row in range(10):
    line = ""
    for col in range(10):
        n = row * 10 + col + 1
        sig = colored_signature(n)
        if not sig.strip():
            line += "  . "
        else:
            line += sig + " "
    print(f"{row*10+1:3d}-{row*10+10:3d}: {line}")

print("\n" + "="*60)
print("INTERESTING FACTORIZATION PATTERNS")
print("="*60 + "\n")

interesting = [60, 120, 210, 360, 2520, 5040]
for n in interesting:
    factors = prime_factors(n)
    unique = sorted(set(factors))
    print(f"{n:4d} = {' × '.join(map(str, factors)):30s} | Unique primes: {unique}")

print("\n" + "="*60)
print("LONGEST FACTORIZATIONS (most prime factors)")
print("="*60 + "\n")

longest = []
for n in range(2, 101):
    longest.append((len(prime_factors(n)), n, prime_factors(n)))

longest.sort(reverse=True)
for count, n, factors in longest[:5]:
    print(f"{n:3d} has {count} factors: {' × '.join(map(str, factors))}")
