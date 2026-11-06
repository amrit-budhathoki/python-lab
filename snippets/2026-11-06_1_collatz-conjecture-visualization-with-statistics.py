# Title: Collatz Conjecture Visualization with Statistics

# This program explores the Collatz conjecture by computing sequences for many starting
# numbers and visualizing the results. It's interesting because despite its simple rules,
# the conjecture remains unproven and produces surprisingly complex behavior patterns.

import math

def collatz_sequence(n):
    """Generate the Collatz sequence starting from n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def visualize_sequence(seq, max_width=60):
    """Create a simple ASCII visualization of sequence height."""
    if not seq:
        return ""
    max_val = max(seq)
    normalized = [int((v / max_val) * max_width) if max_val > 0 else 0 for v in seq]
    return "".join("█" if h > 0 else "·" for h in normalized)

def analyze_sequences(start, end):
    """Analyze Collatz sequences for a range of numbers."""
    stats = {
        'max_length': 0,
        'max_height': 0,
        'longest_start': 0,
        'highest_start': 0,
        'lengths': [],
        'heights': []
    }
    
    for n in range(start, end + 1):
        seq = collatz_sequence(n)
        length = len(seq)
        height = max(seq)
        
        stats['lengths'].append(length)
        stats['heights'].append(height)
        
        if length > stats['max_length']:
            stats['max_length'] = length
            stats['longest_start'] = n
        
        if height > stats['max_height']:
            stats['max_height'] = height
            stats['highest_start'] = n
    
    return stats

def print_header(text, char="="):
    """Print a formatted header."""
    print(f"\n{char * 60}")
    print(f"  {text}")
    print(f"{char * 60}\n")

# Main execution
print_header("COLLATZ CONJECTURE EXPLORER", "═")

# Analyze sequences from 1 to 100
stats = analyze_sequences(1, 100)

print(f"Analyzed 100 numbers (1-100)")
print(f"Longest sequence:  {stats['longest_start']} → {stats['max_length']} steps")
print(f"Highest peak:      {stats['highest_start']} → {stats['max_height']}")
print(f"Average steps:     {sum(stats['lengths']) / len(stats['lengths']):.1f}")
print(f"Average peak:      {sum(stats['heights']) / len(stats['heights']):.0f}")

# Show detailed sequences for interesting numbers
print_header("DETAILED SEQUENCES")

interesting = [27, stats['longest_start'], stats['highest_start']]
for n in sorted(set(interesting)):
    seq = collatz_sequence(n)
    vis = visualize_sequence(seq, 50)
    print(f"n={n:3d} ({len(seq):2d} steps, peak={max(seq):5d})")
    print(f"  {vis}")
    print(f"  Path: {' → '.join(map(str, seq[:8]))}" + 
          ("..." if len(seq) > 8 else ""))
    print()

# Distribution analysis
print_header("DISTRIBUTION ANALYSIS")
print("Step count distribution:")
for i in range(0, stats['max_length'], 5):
    count = sum(1 for l in stats['lengths'] if i <= l < i + 5)
    bar = "█" * (count * 2)
    print(f"  {i:3d}-{i+4:3d} steps: {bar} ({count})")

print("\n" + "─" * 60)
print(f"All {len([x for x in range(1, 101)])} numbers tested eventually reach 1! ✓")
