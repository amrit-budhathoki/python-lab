# Title: Knapsack Problem Dynamic Programming Solver

# Demonstrates the classic 0/1 knapsack problem using dynamic programming.
# Watch as the algorithm fills a table showing optimal values for each capacity,
# then backtracks to find which items were actually selected. Interesting because
# it shows how breaking a hard problem into overlapping subproblems makes it solvable!

def solve_knapsack():
    items = [
        ("Laptop", 5, 3000),
        ("Headphones", 1, 200),
        ("Book", 2, 50),
        ("Phone", 1, 800),
        ("Tablet", 3, 600),
        ("Watch", 1, 150),
    ]
    
    capacity = 8
    n = len(items)
    
    # Build DP table: dp[i][w] = max value using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("=== KNAPSACK SOLVER ===\n")
    print(f"Items: {', '.join(name for name, _, _ in items)}")
    print(f"Weights: {', '.join(str(w) for _, w, _ in items)}")
    print(f"Values: {', '.join(str(v) for _, _, v in items)}")
    print(f"Capacity: {capacity}\n")
    
    # Fill the DP table
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                # Can we fit this item?
                include = dp[i - 1][w - weight] + value
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, weight, value = items[i - 1]
            selected.append((name, weight, value))
            w -= weight
    
    selected.reverse()
    
    print("=== SOLUTION ===")
    print(f"Max value achievable: {dp[n][capacity]}\n")
    print("Selected items:")
    total_weight = 0
    total_value = 0
    for name, weight, value in selected:
        print(f"  • {name}: weight={weight}, value=${value}")
        total_weight += weight
        total_value += value
    
    print(f"\nTotal weight used: {total_weight}/{capacity}")
    print(f"Total value: ${total_value}")
    
    print("\n=== DP TABLE (last 5 rows) ===")
    print("Capacity:", list(range(capacity + 1)))
    for i in range(max(0, n - 4), n + 1):
        item_name = items[i - 1][0] if i > 0 else "Start"
        print(f"{item_name:12s}: {dp[i]}")

solve_knapsack()
