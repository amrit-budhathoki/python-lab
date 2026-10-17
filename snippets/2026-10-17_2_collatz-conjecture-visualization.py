# Title: Collatz Conjecture Visualization

# The Collatz conjecture: repeatedly apply n→n/2 (if even) or n→3n+1 (if odd).
# Every starting number eventually reaches 1. This explores the conjecture by
# showing the longest chains and finding which number produces the most steps.

def collatz_length(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

# Find the most interesting number up to 10000
max_steps = 0
champion = 0
for i in range(1, 10001):
    steps = collatz_length(i)
    if steps > max_steps:
        max_steps = steps
        champion = i

print("=" * 60)
print("COLLATZ CONJECTURE EXPLORER")
print("=" * 60)
print(f"\nAmong numbers 1-10,000:")
print(f"Champion: {champion} with {max_steps} steps")

# Show the sequence for the champion
seq = collatz_sequence(champion)
print(f"\nSequence for {champion}:")
print(f"Start: {seq[0]}")
print(f"Peak: {max(seq)}")
print(f"End: {seq[-1]}")
print(f"Length: {len(seq)}")

# Show the actual sequence
print(f"\nFull path ({len(seq)} numbers):")
for i in range(0, len(seq), 10):
    print(" → ".join(map(str, seq[i:min(i+10, len(seq))])))

# Statistics
print(f"\n" + "=" * 60)
print("STATISTICS:")
all_lengths = [collatz_length(i) for i in range(1, 1001)]
print(f"Average steps (1-1000): {sum(all_lengths) / len(all_lengths):.1f}")
print(f"Minimum steps: {min(all_lengths)}")
print(f"Maximum steps: {max(all_lengths)}")
print("=" * 60)
