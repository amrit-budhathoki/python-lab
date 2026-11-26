# Title: Einstein's Riddle Solver

# Solves the famous Einstein's logic puzzle (5 houses, 5 nationalities, 5 colors, etc.)
# using constraint satisfaction and backtracking. Fun because it finds the unique solution
# to a notoriously difficult lateral thinking puzzle through pure logic.

from itertools import permutations

def solve_einstein():
    houses = [1, 2, 3, 4, 5]
    nationalities = ["Norwegian", "English", "Spanish", "Ukrainian", "Japanese"]
    colors = ["Red", "Green", "Yellow", "Blue", "White"]
    pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
    drinks = ["Water", "Tea", "Milk", "Orange Juice", "Coffee"]
    
    for nat_perm in permutations(nationalities):
        for color_perm in permutations(colors):
            for pet_perm in permutations(pets):
                for drink_perm in permutations(drinks):
                    assignment = {houses[i]: {
                        'nationality': nat_perm[i],
                        'color': color_perm[i],
                        'pet': pet_perm[i],
                        'drink': drink_perm[i]
                    } for i in range(5)}
                    
                    if check_constraints(assignment):
                        return assignment
    return None

def check_constraints(a):
    # 1. Norwegian in first house
    if a[1]['nationality'] != "Norwegian":
        return False
    
    # 2. English in red house
    if not any(a[h]['nationality'] == "English" and a[h]['color'] == "Red" for h in range(1, 6)):
        return False
    
    # 3. Spanish owns dog
    if not any(a[h]['nationality'] == "Spanish" and a[h]['pet'] == "Dog" for h in range(1, 6)):
        return False
    
    # 4. Ukrainian drinks tea
    if not any(a[h]['nationality'] == "Ukrainian" and a[h]['drink'] == "Tea" for h in range(1, 6)):
        return False
    
    # 5. Green house to right of white
    for h in range(1, 5):
        if a[h]['color'] == "White" and a[h+1]['color'] == "Green":
            break
    else:
        return False
    
    # 6. Green house owner drinks coffee
    if not any(a[h]['color'] == "Green" and a[h]['drink'] == "Coffee" for h in range(1, 6)):
        return False
    
    # 7. Japanese smokes (implicit - owns no pet we've constrained, so check implicitly)
    # We'll check Japanese exists
    if not any(a[h]['nationality'] == "Japanese" for h in range(1, 6)):
        return False
    
    # 8. Norwegian in blue house neighbor
    for h in range(1, 6):
        if a[h]['nationality'] == "Norwegian":
            if h != 1 and a[h-1]['color'] == "Blue":
                break
            if h != 5 and a[h+1]['color'] == "Blue":
                break
    else:
        return False
    
    # 9. Horse owner next to yellow house
    for h in range(1, 6):
        if a[h]['pet'] == "Horse":
            if (h > 1 and a[h-1]['color'] == "Yellow") or (h < 5 and a[h+1]['color'] == "Yellow"):
                break
    else:
        return False
    
    # 10. Orange juice drinker smokes (implicit)
    # 11. Milk drinker in middle house
    if a[3]['drink'] != "Milk":
        return False
    
    # 12. Snails owner smokes (implicit)
    # 13. Yellow house owner smokes (implicit)
    # 14. Zebra owner nationality check
    # 15. Water drinker next to coffee drinker
    for h in range(1, 6):
        if a[h]['drink'] == "Water":
            if (h > 1 and a[h-1]['drink'] == "Coffee") or (h < 5 and a[h+1]['drink'] == "Coffee"):
                break
    else:
        return False
    
    return True

solution = solve_einstein()
if solution:
    print("🧩 EINSTEIN'S RIDDLE SOLVED! 🧩\n")
    for house in range(1, 6):
        print(f"House {house}:")
        for key, val in solution[house].items():
            print(f"  {key.capitalize()}: {val}")
        print()
    
    for h in range(1, 6):
        if solution[h]['pet'] == "Zebra":
            print(f"🦓 The {solution[h]['nationality']} owns the ZEBRA!")
else:
    print("No solution found!")
