# Title: Logic Grid Puzzle Solver

# Solves a classic logic puzzle using constraint satisfaction and backtracking.
# Interesting because it demonstrates how to solve deduction puzzles programmatically
# by eliminating impossible combinations until only valid solutions remain.

from itertools import permutations

def solve_logic_puzzle():
    # Puzzle: Four people (Alice, Bob, Carol, Dave) have different favorite colors,
    # fruits, and numbers. Find the unique assignment satisfying all constraints.
    
    people = ['Alice', 'Bob', 'Carol', 'Dave']
    colors = ['Red', 'Blue', 'Green', 'Yellow']
    fruits = ['Apple', 'Banana', 'Cherry', 'Date']
    numbers = [1, 2, 3, 4]
    
    def check_constraints(assignment):
        # assignment: dict mapping person -> (color, fruit, number)
        
        # Constraint 1: Alice's favorite number is less than Bob's
        if assignment['Alice'][2] >= assignment['Bob'][2]:
            return False
        
        # Constraint 2: The person with Red likes Banana
        for person, (color, fruit, num) in assignment.items():
            if color == 'Red' and fruit != 'Banana':
                return False
            if fruit == 'Banana' and color != 'Red':
                return False
        
        # Constraint 3: Carol's number is even
        if assignment['Carol'][2] % 2 != 0:
            return False
        
        # Constraint 4: The person with Green doesn't like Apple
        for person, (color, fruit, num) in assignment.items():
            if color == 'Green' and fruit == 'Apple':
                return False
        
        # Constraint 5: Dave's number is 4
        if assignment['Dave'][2] != 4:
            return False
        
        # Constraint 6: Blue and Cherry go together
        for person, (color, fruit, num) in assignment.items():
            if color == 'Blue' and fruit != 'Cherry':
                return False
            if fruit == 'Cherry' and color != 'Blue':
                return False
        
        return True
    
    # Generate all possible assignments
    for color_perm in permutations(colors):
        for fruit_perm in permutations(fruits):
            for num_perm in permutations(numbers):
                assignment = {
                    people[i]: (color_perm[i], fruit_perm[i], num_perm[i])
                    for i in range(4)
                }
                
                if check_constraints(assignment):
                    return assignment
    
    return None

result = solve_logic_puzzle()

print("Logic Puzzle Solution:")
print("=" * 50)
if result:
    for person in ['Alice', 'Bob', 'Carol', 'Dave']:
        color, fruit, num = result[person]
        print(f"{person:6} | Color: {color:6} | Fruit: {fruit:6} | Number: {num}")
else:
    print("No solution found!")
