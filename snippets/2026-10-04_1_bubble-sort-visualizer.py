# Title: Bubble Sort Visualizer
# Demonstrates the bubble sort algorithm step by step, showing how adjacent elements
# are compared and swapped to sort a list. Each step is printed to visualize the
# sorting process, making it easy to understand how this classic algorithm works.

import random
import time

def bubble_sort_with_steps(arr):
    """Perform bubble sort while printing each step."""
    n = len(arr)
    steps = 0
    
    print(f"Starting array: {arr}\n")
    
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        
        for j in range(0, n - i - 1):
            steps += 1
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they're in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Step {steps}: Swapped {arr[j + 1]} and {arr[j]} → {arr}")
        
        if not swapped:
            print(f"  No swaps made - array is sorted!")
            break
        print()
    
    return arr, steps

# Main program
print("=" * 50)
print("BUBBLE SORT STEP-BY-STEP VISUALIZATION")
print("=" * 50)
print()

# Create a small random list for demonstration
numbers = [64, 34, 25, 12, 22, 11, 90]

# Run the sorting algorithm with visualization
sorted_numbers, total_steps = bubble_sort_with_steps(numbers)

print()
print("=" * 50)
print(f"Final sorted array: {sorted_numbers}")
print(f"Total comparisons/swaps: {total_steps}")
print("=" * 50)
