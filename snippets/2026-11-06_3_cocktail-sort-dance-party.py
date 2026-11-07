# Title: Cocktail Sort Dance Party

# Visualizes cocktail sort (bidirectional bubble sort) by animating bars bouncing back and forth
# across the terminal. It's mesmerizing to watch elements settle into place from both directions!

import random
import time

def cocktail_sort_visualize(arr):
    n = len(arr)
    start, end = 0, n - 1
    swapped = True
    
    while start < end and swapped:
        swapped = False
        
        # Forward pass
        for i in range(start, end):
            display_bars(arr, i, i + 1, "→")
            time.sleep(0.05)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        end -= 1
        swapped = False
        
        # Backward pass
        for i in range(end - 1, start - 1, -1):
            display_bars(arr, i, i + 1, "←")
            time.sleep(0.05)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    display_bars(arr, -1, -1, "✓")

def display_bars(arr, idx1, idx2, direction):
    print("\033[H\033[J", end="")  # Clear screen
    max_val = max(arr)
    
    for i, val in enumerate(arr):
        bar_len = int((val / max_val) * 40) if max_val > 0 else 0
        bar = "█" * bar_len
        
        if i == idx1 or i == idx2:
            marker = f" {direction} "
        else:
            marker = "   "
        
        print(f"{marker}{bar}")
    
    print(f"\nDirection: {direction}")

# Main execution
random.seed(42)
numbers = [random.randint(1, 100) for _ in range(12)]
print("\033[2J")  # Clear screen
cocktail_sort_visualize(numbers)
print("\n✨ Sorting complete! ✨")
