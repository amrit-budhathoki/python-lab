# Title: Bubble Sort Step-by-Step Visualizer

# Demonstrates the bubble sort algorithm by sorting a random list and displaying
# each pass. Interesting because you can see how comparisons gradually bubble larger
# elements to the end, making the algorithm's O(n²) nature visually clear.

import random

def bubble_sort_visual(arr):
    n = len(arr)
    print(f"Starting array: {arr}\n")
    
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        
        for j in range(n - i - 1):
            # Highlight the comparison
            display = arr.copy()
            print(f"  Comparing {display[j]} and {display[j + 1]}", end="")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f" → Swap! Array now: {arr}")
            else:
                print(f" → No swap. Array: {arr}")
        
        print(f"  After pass {i + 1}: {arr}\n")
        
        if not swapped:
            print("No swaps made. Array is sorted!")
            break
    
    return arr

# Create a small random list
test_list = [random.randint(1, 20) for _ in range(6)]
result = bubble_sort_visual(test_list)
print(f"Final sorted array: {result}")
