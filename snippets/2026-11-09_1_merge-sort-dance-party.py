# Title: Merge Sort Dance Party

# Visualizes merge sort algorithm with colorful terminal animations showing
# how elements are recursively split and merged back together in order.
# Interesting because you can see the binary tree structure of divide-and-conquer
# happening in real-time with satisfying visual feedback.

import time
import random

def merge_sort_visual(arr, left=0, right=None, depth=0):
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # Recursive calls with visual feedback
        merge_sort_visual(arr, left, mid, depth + 1)
        merge_sort_visual(arr, mid + 1, right, depth + 1)
        
        # Merge phase with visualization
        merge_with_visual(arr, left, mid, right, depth)
        time.sleep(0.1)

def merge_with_visual(arr, left, mid, right, depth):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    colors = [f"\033[9{i%7+1}m" for i in range(len(arr))]
    reset = "\033[0m"
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    # Print current state
    bar = ""
    max_val = max(arr)
    for num in arr:
        bar_len = int((num / max_val) * 30)
        bar += "█" * bar_len + " "
    
    print(f"{'  ' * depth}{colors[depth % len(colors)]}[{depth}] {bar}{reset}")

def main():
    print("\n🎨 MERGE SORT DANCE PARTY 🎨\n")
    arr = [random.randint(1, 100) for _ in range(16)]
    
    print("Initial array:")
    print(arr)
    print("\nSorting in progress:\n")
    
    merge_sort_visual(arr)
    
    print("\n✨ Final sorted array:")
    print(arr)
    print("\n✨ Done!\n")

if __name__ == "__main__":
    main()
