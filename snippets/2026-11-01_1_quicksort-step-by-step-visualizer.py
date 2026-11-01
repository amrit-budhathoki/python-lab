# Title: Quicksort Step-by-Step Visualizer
# Quicksort is a fast divide-and-conquer sorting algorithm. This visualizer shows each pivot
# selection and partition operation, demonstrating how the algorithm recursively sorts by
# partitioning arrays around pivot elements. It's interesting because quicksort is one of
# the most practical sorting algorithms despite having poor worst-case complexity.

import random

def quicksort_visualize(arr, low=0, high=None, depth=0, step_count=[0]):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Choose random pivot (randomized quicksort)
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        pivot_val = arr[high]
        
        # Partition step
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot_val:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        partition_idx = i + 1
        
        # Visualize step
        step_count[0] += 1
        indent = "  " * depth
        sorted_str = "".join([f"[{x:2d}]" if x == pivot_val else f" {x:2d} " for x in arr])
        print(f"Step {step_count[0]:2d} (depth {depth}): {indent}Pivot={pivot_val:2d} | {sorted_str}")
        
        # Recursively sort left and right
        quicksort_visualize(arr, low, partition_idx - 1, depth + 1, step_count)
        quicksort_visualize(arr, partition_idx + 1, high, depth + 1, step_count)

# Demo
print("=" * 70)
print("QUICKSORT STEP-BY-STEP VISUALIZATION")
print("=" * 70)
print()

arr = [random.randint(10, 99) for _ in range(8)]
print(f"Initial array: {arr}")
print()
print("Sorting process (pivot shown in brackets):")
print()

quicksort_visualize(arr)

print()
print(f"Final sorted array: {arr}")
print(f"Is sorted: {arr == sorted(arr)}")
