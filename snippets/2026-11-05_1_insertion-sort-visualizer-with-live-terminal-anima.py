# Title: Insertion Sort Visualizer with Live Terminal Animation

# Watches insertion sort reorganize random numbers in real-time.
# Each number is drawn as a bar, and you see it shift left until it finds its place.
# Interesting because it's mesmerizing to watch the algorithm "insert" each element.

import random
import time

def visualize_insertion_sort(arr, width=60):
    """Visualize insertion sort with terminal animation."""
    arr = arr.copy()
    n = len(arr)
    
    def draw(highlight_idx=-1, insert_idx=-1):
        """Draw the current state of the array as bars."""
        max_val = max(arr)
        print("\033[2J\033[H", end="")  # Clear screen
        
        for i in range(n):
            bar_length = int((arr[i] / max_val) * width)
            bar = "█" * bar_length
            
            if i == highlight_idx:
                print(f"\033[92m{bar}\033[0m {arr[i]}")  # Green
            elif i == insert_idx:
                print(f"\033[93m{bar}\033[0m {arr[i]}")  # Yellow
            else:
                print(f"{bar} {arr[i]}")
        print()
    
    # Insertion sort with visualization
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        draw(highlight_idx=i)
        time.sleep(0.3)
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            draw(highlight_idx=j, insert_idx=j+1)
            time.sleep(0.15)
            j -= 1
        
        arr[j + 1] = key
        draw()
        time.sleep(0.2)
    
    # Final sorted display
    print("\033[92m" + "SORTED!" + "\033[0m")
    draw()

# Run the visualization
random.seed(42)
numbers = [random.randint(10, 100) for _ in range(12)]
visualize_insertion_sort(numbers)
