# Title: Sexy Prime Pairs Explorer

# Finds and visualizes "sexy primes" - prime pairs that differ by 6.
# It's fun because these primes have a cheeky name and form interesting patterns!
# We'll display them visually and show statistics about their distribution.

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
    for p in range(2, limit - 6):
        if is_prime(p) and is_prime(p + 6):
            sexy_pairs.append((p, p + 6))
    return sexy_pairs

def visualize_sexy_primes(pairs):
    print("\n" + "="*60)
    print("🔥 SEXY PRIME PAIRS EXPLORER 🔥")
    print("="*60)
    print("\nPrimes that differ by exactly 6 are called 'sexy primes'")
    print("(From the Latin 'sex' meaning six)\n")
    
    for idx, (p1, p2) in enumerate(pairs[:20], 1):
        bar_length = p2 // 10
        bar = "█" * bar_length
        print(f"{idx:2d}. ({p1:4d}, {p2:4d})  gap: 6  │{bar}│")
    
    if len(pairs) > 20:
        print(f"\n... and {len(pairs) - 20} more sexy prime pairs!")
    
    print("\n" + "="*60)
    print("STATISTICS")
    print("="*60)
    
    all_primes_in_pairs = set()
    for p1, p2 in pairs:
        all_primes_in_pairs.add(p1)
        all_primes_in_pairs.add(p2)
    
    total_primes = sum(1 for i in range(2, pairs[-1][1] + 1) if is_prime(i))
    
    print(f"Total sexy prime pairs found: {len(pairs)}")
    print(f"Unique primes in pairs: {len(all_primes_in_pairs)}")
    print(f"Total primes up to {pairs[-1][1]}: {total_primes}")
    print(f"Percentage in sexy pairs: {len(all_primes_in_pairs)/total_primes*100:.1f}%")
    
    gaps = [pairs[i+1][0] - pairs[i][0] for i in range(len(pairs)-1)]
    if gaps:
        print(f"\nAverage gap between consecutive pairs: {sum(gaps)/len(gaps):.1f}")
        print(f"Largest gap: {max(gaps)}")
        print(f"Smallest gap: {min(gaps)}")
    
    print("\n" + "="*60)
    
    triplets = []
    for i in range(len(pairs) - 2):
        if pairs[i+1][0] - pairs[i][0] == 6:
            if triplets and triplets[-1][2] == pairs[i][0]:
                triplets[-1] = (triplets[-1][0], triplets[-1][1], pairs[i+1][1])
            else:
                triplets.append((pairs[i][0], pairs[i][1], pairs[i+1][1]))
    
    if triplets:
        print(f"\n🌟 SEXY PRIME TRIPLETS (three in a row!): {len(triplets)}")
        for t in triplets[:10]:
            print(f"   {t}")

limit = 1000
sexy_primes = find_sexy_primes(limit)
visualize_sexy_primes(sexy_primes)
