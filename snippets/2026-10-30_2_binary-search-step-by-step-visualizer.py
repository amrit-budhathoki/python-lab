# Title: Binary Search Step-by-Step Visualizer

# Demonstrates binary search algorithm by finding a secret number in a sorted list.
# Shows each step of the search process, highlighting the shrinking search space.
# Interesting because it visualizes how binary search eliminates half the possibilities each iteration.

import random

def binary_search_visualize(arr, target):
    left, right = 0, len(arr) - 1
    step = 0
    
    print(f"🔍 Finding {target} in: {arr}\n")
    
    while left <= right:
        mid = (left + right) // 2
        step += 1
        
        # Visualize the current search space
        visual = ""
        for i in range(len(arr)):
            if i < left or i > right:
                visual += "·"
            elif i == mid:
                visual += "█"
            else:
                visual += "▌"
        
        print(f"Step {step}: {visual}")
        print(f"         Range: [{left}, {right}]  Mid: arr[{mid}]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"\n✨ Found {target} at index {mid}!\n")
            return mid
        elif arr[mid] < target:
            print(f"         → {arr[mid]} < {target}, search RIGHT\n")
            left = mid + 1
        else:
            print(f"         → {arr[mid]} > {target}, search LEFT\n")
            right = mid - 1
    
    print(f"❌ {target} not found!\n")
    return -1

# Generate sorted list and random target
numbers = sorted([random.randint(1, 100) for _ in range(15)])
target = random.choice(numbers + [random.randint(1, 100)])

print("=" * 60)
print("BINARY SEARCH ALGORITHM STEP-BY-STEP")
print("=" * 60 + "\n")

binary_search_visualize(numbers, target)

# Show another example with a different target
print("=" * 60)
target2 = random.choice(numbers)
binary_search_visualize(numbers, target2)
