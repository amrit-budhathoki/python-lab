# Title: Quicksort Step-by-Step Visualizer

# Quicksort is one of the most popular sorting algorithms. This program visualizes
# each step of the quicksort process, showing how the pivot partitions the array
# and how the algorithm recursively sorts subarrays. It's interesting because you
# can see the "divide and conquer" strategy in action, with clear visual feedback.

def quicksort_visualize(arr, low=0, high=None, depth=0, steps=None):
    if steps is None:
        steps = []
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high, depth, steps)
        quicksort_visualize(arr, low, pivot_index - 1, depth + 1, steps)
        quicksort_visualize(arr, pivot_index + 1, high, depth + 1, steps)
    
    return steps

def partition(arr, low, high, depth, steps):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps.append({
                'array': arr[:],
                'low': low,
                'high': high,
                'pivot': pivot,
                'i': i,
                'j': j,
                'depth': depth,
                'action': f'swap({arr[j]}, {arr[i]})'
            })
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append({
        'array': arr[:],
        'low': low,
        'high': high,
        'pivot': pivot,
        'i': i + 1,
        'j': high,
        'depth': depth,
        'action': f'pivot {pivot} placed at index {i + 1}'
    })
    
    return i + 1

def visualize_array(arr, low, high, pivot_idx):
    visual = ""
    for idx, val in enumerate(arr):
        if idx == pivot_idx:
            visual += f"[{val:2d}*] "
        elif low <= idx <= high:
            visual += f" {val:2d}  "
        else:
            visual += f"({val:2d}) "
    return visual

arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
print("Original array:", arr)
print("\n" + "="*70)
print("QUICKSORT STEP-BY-STEP VISUALIZATION")
print("="*70)

steps = quicksort_visualize(arr)

for step_num, step in enumerate(steps, 1):
    print(f"\nStep {step_num}: {step['action']}")
    print(f"Depth: {step['depth']}")
    visual = visualize_array(step['array'], step['low'], step['high'], 
                             step['array'].index(step['pivot']))
    print(f"Array: {visual}")

print("\n" + "="*70)
print("Final sorted array:", steps[-1]['array'])
print("Total steps:", len(steps))
