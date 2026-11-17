# Title: Bogo Sort - The Hilariously Inefficient Sorting Algorithm

# This visualizes bogosort, which randomly shuffles until sorted. It's intentionally
# the worst sorting algorithm ever created, making it funny to watch - especially with
# small lists. The terminal shows each shuffle attempt with live progress bars.

import random
import time

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def print_bar(arr, attempt):
    max_val = max(arr)
    bar = ''.join('█' * int(50 * x / max_val) for x in arr)
    print(f"\r Attempt {attempt:5d} | {bar} | {arr}", end='', flush=True)

def bogo_sort(arr):
    arr = arr.copy()
    attempt = 0
    
    print(f"\n Starting array: {arr}")
    print(f" Sorting with BOGO SORT (worst algorithm ever)...\n")
    
    start_time = time.time()
    
    while not is_sorted(arr):
        random.shuffle(arr)
        attempt += 1
        
        if attempt % 10 == 0:
            print_bar(arr, attempt)
        
        if attempt > 100000:
            print(f"\n ❌ Gave up after {attempt} attempts!")
            return arr
    
    elapsed = time.time() - start_time
    print_bar(arr, attempt)
    print(f"\n ✓ Sorted in {attempt} attempts ({elapsed:.3f}s)!\n")
    return arr

# Run demonstrations with increasing list sizes
print("\n" + "="*70)
print("  BOGO SORT: Watching Chaos Become Order (or Not)")
print("="*70)

for size in [4, 5]:
    arr = list(range(1, size + 1))
    random.shuffle(arr)
    bogo_sort(arr)
    time.sleep(0.5)

print("🎲 Pro tip: Don't use bogosort for anything real!\n")
