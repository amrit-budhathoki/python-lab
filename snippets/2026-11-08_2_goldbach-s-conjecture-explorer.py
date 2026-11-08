# Title: Goldbach's Conjecture Explorer

# This program explores Goldbach's conjecture by finding all ways to express even numbers
# as sums of two primes. It's interesting because it's an unsolved problem in mathematics
# that has been verified for enormous numbers, yet remains unproven!

def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, limit + 1) if is_prime[i]]

def goldbach_partitions(n, primes_set):
    """Find all ways to express even number n as sum of two primes."""
    partitions = []
    for p in primes_set:
        if p > n // 2:
            break
        complement = n - p
        if complement in primes_set:
            partitions.append((p, complement))
    return partitions

def main():
    limit = 100
    primes = sieve_of_eratosthenes(limit)
    primes_set = set(primes)
    
    print("🔍 Goldbach's Conjecture Explorer")
    print("=" * 50)
    print(f"Testing: Every even number > 2 is sum of two primes\n")
    
    even_numbers = range(4, 51, 2)
    
    for n in even_numbers:
        partitions = goldbach_partitions(n, primes_set)
        count = len(partitions)
        
        # Show first and last partition for compact display
        if partitions:
            first = f"{partitions[0][0]} + {partitions[0][1]}"
            if count > 1:
                last = f"{partitions[-1][0]} + {partitions[-1][1]}"
                display = f"{first} ... {last}" if count > 2 else first
            else:
                display = first
            print(f"{n:3d} → {count:2d} ways: {display}")
        else:
            print(f"{n:3d} → COUNTEREXAMPLE FOUND! (This shouldn't happen)")
    
    print("\n" + "=" * 50)
    print("✅ Conjecture holds for all tested even numbers!")
    
    # Bonus: Show distribution of partition counts
    partition_counts = []
    for n in range(4, 201, 2):
        if n <= limit * 2:
            partitions = goldbach_partitions(n, primes_set)
            partition_counts.append(len(partitions))
    
    if partition_counts:
        print(f"\nFor even numbers 4-200:")
        print(f"  Min partitions: {min(partition_counts)}")
        print(f"  Max partitions: {max(partition_counts)}")
        print(f"  Avg partitions: {sum(partition_counts) / len(partition_counts):.1f}")

if __name__ == "__main__":
    main()
