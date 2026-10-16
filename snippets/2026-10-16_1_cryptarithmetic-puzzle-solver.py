# Title: Cryptarithmetic Puzzle Solver

# Solves the classic SEND + MORE = MONEY puzzle by finding digit assignments
# where each letter maps to a unique digit (0-9) and the arithmetic equation works.
# Interesting because it uses constraint satisfaction through brute force permutations.

from itertools import permutations

def solve_cryptarithmetic():
    """Solve SEND + MORE = MONEY puzzle"""
    
    solutions = []
    
    # Each letter must map to a unique digit
    # S, E, N, D, M, O, R, Y are the 8 unique letters
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    
    # Try all permutations of digits 0-9 mapped to these letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Leading digits cannot be 0
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Calculate the values
        SEND = (mapping['S'] * 1000 + mapping['E'] * 100 + 
                mapping['N'] * 10 + mapping['D'])
        MORE = (mapping['M'] * 1000 + mapping['O'] * 100 + 
                mapping['R'] * 10 + mapping['E'])
        MONEY = (mapping['M'] * 10000 + mapping['O'] * 1000 + 
                 mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y'])
        
        # Check if the equation holds
        if SEND + MORE == MONEY:
            solutions.append((mapping, SEND, MORE, MONEY))
    
    return solutions

# Solve and display
print("Solving: SEND + MORE = MONEY\n")
solutions = solve_cryptarithmetic()

if solutions:
    for mapping, send, more, money in solutions:
        print("Solution found:")
        for letter in sorted(mapping.keys()):
            print(f"  {letter} = {mapping[letter]}", end="  ")
        print(f"\n\n  {send}")
        print(f"+ {more}")
        print(f"-------")
        print(f" {money}\n")
else:
    print("No solution found.")
