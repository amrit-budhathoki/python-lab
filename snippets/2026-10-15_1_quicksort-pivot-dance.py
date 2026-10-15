# Title: Quicksort Pivot Dance

# Visualizes quicksort in action with a terminal animation showing how pivot selection
# partitions the array. Watch the bars shuffle and reorganize in real-time as the
# algorithm divides and conquers - it's mesmerizing to see order emerge from chaos!

import random
import time

def visualize_bar(value, max_val, width=40):
    filled = int((value / max_val) * width)
    return "█" * filled + "░" * (width - filled)

def print_state(arr, max_val, left=-1, right=-1, pivot_idx=-1):
    print("\033[2J\033[H")
    for i, val in enumerate(arr):
        marker = ""
        if i == pivot_idx:
            marker = " ← PIVOT"
        elif i == left:
            marker = " ← LEFT"
        elif i == right:
            marker = " ← RIGHT"
        print(f"{i:2d}: {visualize_bar(val, max_val)} {val:3d}{marker}")
    print("\n" + "=" * 60)
    time.sleep(0.05)

def quicksort_visual(arr, low, high, max_val):
    if low < high:
        pivot_idx = partition_visual(arr, low, high, max_val)
        quicksort_visual(arr, low, pivot_idx - 1, max_val)
        quicksort_visual(arr, pivot_idx + 1, high, max_val)

def partition_visual(arr, low, high, max_val):
    pivot = arr[high]
    i = low - 1
    print_state(arr, max_val, pivot_idx=high)
    
    for j in range(low, high):
        print_state(arr, max_val, left=i, right=j, pivot_idx=high)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print_state(arr, max_val, left=i, right=j, pivot_idx=high)
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print_state(arr, max_val, pivot_idx=i + 1)
    return i + 1

def main():
    arr = [random.randint(10, 99) for _ in range(15)]
    max_val = max(arr)
    
    print("Starting array:")
    print_state(arr, max_val)
    time.sleep(1)
    
    quicksort_visual(arr, 0, len(arr) - 1, max_val)
    
    print("\n✓ Sorted! Final array:")
    for i, val in enumerate(arr):
        print(f"{i:2d}: {visualize_bar(val, max_val)} {val:3d}")

if __name__ == "__main__":
    main()
