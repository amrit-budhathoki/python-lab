# Title: Bubble Sort Dance Party
# Visualizes the bubble sort algorithm step-by-step with ASCII art,
# showing comparisons and swaps as the array gradually becomes sorted.
# It's fun to watch disorder transform into order!

import random
import time

def print_array(arr, comparing=None, sorted_indices=None):
    if sorted_indices is None:
        sorted_indices = set()
    
    line = ""
    for i, val in enumerate(arr):
        if i in sorted_indices:
            line += f"\033[92m{val:2d}\033[0m "
        elif comparing and i in comparing:
            line += f"\033[91m{val:2d}\033[0m "
        else:
            line += f"{val:2d} "
    print(line)

def bubble_sort_visual(arr):
    n = len(arr)
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    
    print("\n🔀 BUBBLE SORT DANCE PARTY 🔀")
    print("Red = comparing | Green = sorted | White = unsorted")
    print("=" * 40)
    print("Initial array:")
    print_array(arr)
    print()
    
    for i in range(n):
        swapped = False
        sorted_indices = set(range(n - i, n))
        
        for j in range(0, n - i - 1):
            comparisons += 1
            print(f"Step {comparisons}: Comparing {arr[j]} and {arr[j+1]}", end=" → ")
            print_array(arr, comparing={j, j+1}, sorted_indices=sorted_indices)
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                print(f"         💫 SWAP!", end=" → ")
                print_array(arr, comparing={j, j+1}, sorted_indices=sorted_indices)
            
            time.sleep(0.15)
        
        if not swapped and i > 0:
            break
    
    print("\n" + "=" * 40)
    print("✨ SORTED! ✨")
    print_array(arr, sorted_indices=set(range(n)))
    print(f"\nStats: {comparisons} comparisons, {swaps} swaps")

# Run with a small random array
numbers = [random.randint(1, 99) for _ in range(8)]
bubble_sort_visual(numbers)
