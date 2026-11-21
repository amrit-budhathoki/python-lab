# Title: Cryptarithmetic Puzzle Solver

# Solves cryptarithmetic puzzles like SEND + MORE = MONEY by finding digit assignments
# where each letter maps to a unique digit (0-9) and the arithmetic equation is satisfied.
# Interesting because it uses constraint satisfaction and backtracking to explore a large space.

from itertools import permutations

def solve_cryptarithmetic(puzzle):
    """
    Solve a cryptarithmetic puzzle in the form: 'SEND + MORE = MONEY'
    Returns the mapping of letters to digits that satisfies the equation.
    """
    parts = puzzle.replace(' ', '').split('=')
    if len(parts) != 2:
        return None
    
    left_expr, result_expr = parts
    addends = left_expr.split('+')
    
    # Collect all unique letters
    all_letters = set()
    for expr in addends + [result_expr]:
        all_letters.update(expr)
    
    letters = list(all_letters)
    n = len(letters)
    
    if n > 10:
        return None
    
    # Get leading letters (cannot be zero)
    leading_letters = set()
    for expr in addends + [result_expr]:
        if len(expr) > 1:
            leading_letters.add(expr[0])
    
    # Try all permutations of digits for the letters
    for perm in permutations(range(10), n):
        mapping = dict(zip(letters, perm))
        
        # Check constraint: leading digits cannot be zero
        valid = all(mapping[letter] != 0 for letter in leading_letters)
        if not valid:
            continue
        
        # Convert words to numbers using the mapping
        def word_to_num(word):
            num = 0
            for char in word:
                num = num * 10 + mapping[char]
            return num
        
        # Check if the equation holds
        left_sum = sum(word_to_num(addend) for addend in addends)
        right_sum = word_to_num(result_expr)
        
        if left_sum == right_sum:
            return mapping
    
    return None

def display_solution(puzzle, mapping):
    """Display the puzzle solution nicely."""
    if mapping is None:
        print(f"No solution found for: {puzzle}")
        return
    
    print(f"Puzzle: {puzzle}")
    print(f"Solution: {mapping}")
    
    # Show the actual arithmetic
    parts = puzzle.replace(' ', '').split('=')
    left_expr, result_expr = parts
    addends = left_expr.split('+')
    
    def word_to_num(word):
        return int(''.join(str(mapping[char]) for char in word))
    
    for addend in addends:
        print(f"  {addend} = {word_to_num(addend)}")
    print(f"  {'-' * 10}")
    print(f"  {result_expr} = {word_to_num(result_expr)}")
    print()

# Classic cryptarithmetic puzzles
puzzles = [
    "SEND + MORE = MONEY",
    "CROSS + ROADS = DANGER",
    "FRUIT + FLIES = SWEET",
]

print("Cryptarithmetic Puzzle Solver")
print("=" * 40)
print()

for puzzle in puzzles:
    solution = solve_cryptarithmetic(puzzle)
    display_solution(puzzle, solution)
