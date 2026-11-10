# Title: Selection Sort Dance Party

# Visualizes selection sort with colorful terminal animation. Each pass finds the minimum
# element and swaps it into position, with bars growing taller as they get sorted. Fun to
# watch the algorithm make progress from left to right with live terminal updates.

import random
import time

def print_bar(height, width=2):
    return "█" * (height * width)

def selection_sort_visual(arr):
    n = len(arr)
    colors = ["\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[0m"]
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print("\033[2J\033[H")
        print(f"Selection Sort - Pass {i + 1}/{n}")
        print("=" * 50)
        
        for idx, val in enumerate(arr):
            color = colors[idx % len(colors)]
            status = "✓" if idx < i + 1 else " "
            bar = print_bar(val)
            print(f"{color}{status} [{val:2d}] {bar}\033[0m")
        
        print("=" * 50)
        time.sleep(0.3)
    
    print("\033[2J\033[H")
    print("Selection Sort - COMPLETE!")
    print("=" * 50)
    for idx, val in enumerate(arr):
        bar = print_bar(val)
        print(f"\033[92m✓ [{val:2d}] {bar}\033[0m")
    print("=" * 50)

if __name__ == "__main__":
    random.seed(42)
    data = [random.randint(1, 15) for _ in range(10)]
    selection_sort_visual(data)
