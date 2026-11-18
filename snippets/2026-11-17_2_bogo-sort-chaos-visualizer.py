# Title: Bogo Sort Chaos Visualizer

# Visualizes the hilariously inefficient bogo sort algorithm by randomly shuffling
# an array until it's sorted. The terminal display shows the current state with
# colored bars, making it fun to watch chaos slowly (or quickly!) resolve into order.

import random
import time

def print_bars(arr, iteration):
    max_val = max(arr)
    width = 40
    print(f"\rIteration {iteration}: ", end="")
    for num in arr:
        bar_len = int((num / max_val) * width)
        print("█" * bar_len + "░" * (width - bar_len), end=" ")
    print(end="", flush=True)

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogo_sort_visualize(arr):
    iteration = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        iteration += 1
        if iteration % 100 == 0 or iteration < 10:
            print_bars(arr, iteration)
        time.sleep(0.001)
    print_bars(arr, iteration)
    print(f"\n✓ Sorted in {iteration} iterations!")
    return arr

def main():
    print("🎲 BOGO SORT CHAOS VISUALIZER 🎲")
    print("Watching random shuffles until sorted...\n")
    
    test_cases = [
        [5, 2, 8, 1, 9],
        [3, 1, 4, 1, 5, 9, 2, 6],
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {arr}")
        bogo_sort_visualize(arr.copy())
        time.sleep(0.5)
    
    print("\n🎉 Bogo sort: Proof that patience is a virtue!")

if __name__ == "__main__":
    main()
