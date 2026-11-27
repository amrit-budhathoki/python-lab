# Title: Insertion Sort Visualizer
# Watch insertion sort organize numbers in real-time with animated bars growing as elements are sorted, showing each comparison and insertion step clearly.

import time
import random

def print_bar(value, max_val, width=30):
    filled = int((value / max_val) * width)
    return '█' * filled + '░' * (width - filled)

def insertion_sort_visual(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        print(f"\n--- Step {i}: Inserting {key} ---")
        print_array(arr, j, i, max(arr))
        time.sleep(0.3)
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(f"\n--- Shifting {arr[j]} right ---")
            print_array(arr, j, i, max(arr))
            time.sleep(0.2)
            j -= 1
        
        arr[j + 1] = key
        print(f"\n--- Inserted {key} at position {j + 1} ---")
        print_array(arr, -1, -1, max(arr))
        time.sleep(0.3)

def print_array(arr, compare_idx=-1, insert_idx=-1, max_val=100):
    for idx, value in enumerate(arr):
        marker = ""
        if idx == compare_idx:
            marker = " ◄ comparing"
        elif idx == insert_idx:
            marker = " ◄ inserting"
        
        bar = print_bar(value, max_val)
        print(f"{value:3d} {bar}{marker}")

def main():
    print("╔════════════════════════════════╗")
    print("║   INSERTION SORT VISUALIZER    ║")
    print("╚════════════════════════════════╝\n")
    
    arr = [random.randint(10, 100) for _ in range(8)]
    print("Initial array:")
    print_array(arr, -1, -1, max(arr))
    time.sleep(1)
    
    insertion_sort_visual(arr)
    
    print("\n" + "="*50)
    print("SORTING COMPLETE!")
    print("="*50)
    print_array(arr, -1, -1, max(arr))

if __name__ == "__main__":
    main()
