# Title: Collatz Conjecture Path Length Explorer

# The Collatz conjecture states that any positive integer eventually reaches 1
# by repeatedly applying: divide by 2 if even, multiply by 3 and add 1 if odd.
# This program visualizes the path lengths and finds the longest sequences,
# revealing surprising patterns in this unsolved mathematical mystery.

def collatz_length(n):
    """Calculate the length of the Collatz sequence for n."""
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def collatz_path(n):
    """Return the full Collatz sequence for n."""
    path = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        path.append(n)
    return path

# Analyze numbers up to 10000
max_length = 0
max_number = 0
lengths = []

print("Collatz Conjecture Explorer")
print("=" * 50)

for i in range(1, 10001):
    length = collatz_length(i)
    lengths.append(length)
    if length > max_length:
        max_length = length
        max_number = i

print(f"Searched numbers 1 to 10,000")
print(f"Longest sequence: {max_length} steps (starting from {max_number})")
print()
print(f"Path for {max_number}:")
path = collatz_path(max_number)
print(" → ".join(map(str, path[:20])) + (" → ..." if len(path) > 20 else ""))
print()

# Show distribution
print("Sequence length distribution:")
for bucket in range(0, max_length + 1, 20):
    count = sum(1 for l in lengths if bucket <= l < bucket + 20)
    bar = "█" * (count // 10)
    print(f"{bucket:3d}-{bucket+19:3d}: {bar} ({count})")

print()
print("Top 10 numbers with longest sequences:")
sorted_nums = sorted(range(1, 10001), key=lambda n: collatz_length(n), reverse=True)
for i, num in enumerate(sorted_nums[:10], 1):
    print(f"  {i:2d}. {num:5d} → {collatz_length(num)} steps")
