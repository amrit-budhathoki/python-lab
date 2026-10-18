# Title: Fibonacci Prime Finder with Golden Ratio Hunt

# This program finds prime numbers within the Fibonacci sequence and tracks
# how the ratio between consecutive Fibonacci numbers converges to the golden ratio.
# It's interesting because it combines number theory (primes) with a mathematical
# constant that appears everywhere in nature, showing the beautiful intersection.

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

def fibonacci_sequence(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def main():
    LIMIT = 1000000
    GOLDEN_RATIO = (1 + 5**0.5) / 2
    
    fib_list = list(fibonacci_sequence(LIMIT))
    primes_in_fib = []
    
    print("🔍 Hunting for Prime Fibonacci Numbers...\n")
    print(f"{'Index':<6} {'Fib(n)':<12} {'Prime?':<8} {'Ratio':<12}")
    print("-" * 50)
    
    for i, fib_num in enumerate(fib_list):
        if fib_num < 2:
            continue
            
        prime = is_prime(fib_num)
        
        if i > 0:
            ratio = fib_list[i] / fib_list[i-1] if fib_list[i-1] != 0 else 0
            ratio_str = f"{ratio:.6f}"
        else:
            ratio_str = "N/A"
        
        if prime:
            primes_in_fib.append(fib_num)
            status = "✓ PRIME"
            print(f"{i:<6} {fib_num:<12} {status:<8} {ratio_str:<12}")
    
    print("\n" + "="*50)
    print(f"📊 Statistics:")
    print(f"   Total Fibonacci numbers up to {LIMIT:,}: {len(fib_list)}")
    print(f"   Prime Fibonacci numbers found: {len(primes_in_fib)}")
    print(f"   Golden Ratio (φ): {GOLDEN_RATIO:.10f}")
    print(f"\n   Last ratio calculated: {fib_list[-1] / fib_list[-2]:.10f}")
    print(f"   Difference from φ: {abs(fib_list[-1] / fib_list[-2] - GOLDEN_RATIO):.2e}")
    print(f"\n🎯 Prime Fibonacci numbers: {primes_in_fib}")

if __name__ == "__main__":
    main()
