# Title: Kaprekar's Constant Discovery

# Kaprekar's routine: repeatedly sort digits descending, subtract ascending sort.
# With 4-digit numbers, this always reaches 6174 (Kaprekar's constant) in at most 7 steps.
# This program demonstrates the mesmerizing convergence to this mathematical black hole.

def kaprekar_step(n, digits=4):
    """Perform one step of Kaprekar's routine."""
    s = str(n).zfill(digits)
    desc = int(''.join(sorted(s, reverse=True)))
    asc = int(''.join(sorted(s)))
    return desc - asc

def find_kaprekar_path(start, digits=4):
    """Find the path from start to Kaprekar's constant."""
    path = [start]
    current = start
    seen = {start}
    
    while current != 6174:
        current = kaprekar_step(current, digits)
        if current in seen:
            break
        path.append(current)
        seen.add(current)
    
    return path

print("=" * 60)
print("KAPREKAR'S CONSTANT EXPLORER (4-digit numbers)")
print("=" * 60)

test_numbers = [3524, 1000, 9998, 5555, 1111, 2468, 7349]

for num in test_numbers:
    path = find_kaprekar_path(num)
    print(f"\nStarting from {num}:")
    print(f"  Path: {' → '.join(map(str, path))}")
    print(f"  Steps to 6174: {len(path) - 1}")

print("\n" + "=" * 60)
print("STATISTICS: Testing all 4-digit numbers (except repdigits)")
print("=" * 60)

step_counts = []
for n in range(1, 10000):
    s = str(n).zfill(4)
    if len(set(s)) == 1:
        continue
    path = find_kaprekar_path(n)
    step_counts.append(len(path) - 1)

print(f"Total numbers tested: {len(step_counts)}")
print(f"Max steps needed: {max(step_counts)}")
print(f"Average steps: {sum(step_counts) / len(step_counts):.2f}")

step_distribution = {}
for steps in step_counts:
    step_distribution[steps] = step_distribution.get(steps, 0) + 1

print("\nDistribution of steps to convergence:")
for steps in sorted(step_distribution.keys()):
    count = step_distribution[steps]
    bar = "█" * (count // 100)
    print(f"  {steps} steps: {count:5d} numbers {bar}")

print("\n✨ All paths lead to the mysterious 6174! ✨")
