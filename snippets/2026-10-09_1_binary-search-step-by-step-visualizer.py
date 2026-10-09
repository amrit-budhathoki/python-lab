# Title: Binary Search Step-by-Step Visualizer

# Demonstrates the binary search algorithm finding a target in a sorted list.
# Shows each comparison step, making it clear why binary search is O(log n).

import time

def binary_search_visual(arr, target):
    """Binary search that prints each step of the algorithm."""
    left, right = 0, len(arr) - 1
    step = 0
    
    print(f"\n🔍 Searching for {target} in: {arr}\n")
    
    while left <= right:
        mid = (left + right) // 2
        step += 1
        
        # Visualize the current search window
        visual = [' ' * 3] * len(arr)
        for i in range(left, right + 1):
            visual[i] = f"{arr[i]:3d}"
        
        print(f"Step {step}: {' '.join(visual)}")
        print(f"         Checking index {mid} (value: {arr[mid]})")
        
        if arr[mid] == target:
            print(f"✅ Found {target} at index {mid} after {step} steps!\n")
            return mid
        elif arr[mid] < target:
            print(f"   {arr[mid]} < {target}, search RIGHT ➡️")
            left = mid + 1
        else:
            print(f"   {arr[mid]} > {target}, search LEFT ⬅️")
            right = mid - 1
        
        print()
        time.sleep(0.3)
    
    print(f"❌ {target} not found after {step} steps!\n")
    return -1

# Demo: search a sorted list
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78, 89, 95]
binary_search_visual(numbers, 23)
binary_search_visual(numbers, 50)

# Show why binary search is efficient
print("📊 Efficiency comparison:")
print(f"   List size: {len(numbers)}")
print(f"   Maximum steps needed: {len(numbers).__bit_length__()}")
print(f"   vs Linear search worst case: {len(numbers)}")
