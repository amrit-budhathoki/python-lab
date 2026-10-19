# Title: Tower of Hanoi Step-by-Step Solver

# Visualizes the classic Tower of Hanoi puzzle being solved recursively.
# Shows each move as disks are transferred between pegs, demonstrating how
# recursion elegantly breaks down an exponential problem into simple steps.

def hanoi(n, source, target, auxiliary, moves):
    """Recursively solve Tower of Hanoi and record each move"""
    if n == 1:
        moves.append((source, target))
        return
    
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)

def display_pegs(pegs, move_num, total_moves):
    """Display current state of all three pegs"""
    print(f"\nMove {move_num}/{total_moves}:")
    peg_names = ['A', 'B', 'C']
    max_height = max(len(p) for p in pegs)
    
    for level in range(max_height, 0, -1):
        for peg_idx in range(3):
            if len(pegs[peg_idx]) >= level:
                disk_size = pegs[peg_idx][level - 1]
                disk = '█' * (disk_size * 2 - 1)
                print(f"  {disk.center(11)}", end="")
            else:
                print(f"  {'|'.center(11)}", end="")
        print()
    
    print("  " + "-" * 35)
    for i in range(3):
        print(f"  {peg_names[i]:^11}", end="")
    print("\n")

def solve_hanoi(num_disks):
    """Solve Tower of Hanoi and display each step"""
    moves = []
    hanoi(num_disks, 0, 2, 1, moves)
    
    pegs = [list(range(num_disks, 0, -1)), [], []]
    peg_names = ['A', 'B', 'C']
    
    print(f"{'='*35}")
    print(f"Tower of Hanoi with {num_disks} disks")
    print(f"Solution requires {len(moves)} moves")
    print(f"{'='*35}")
    
    display_pegs(pegs, 0, len(moves))
    
    for move_num, (source, target) in enumerate(moves, 1):
        disk = pegs[source].pop()
        pegs[target].append(disk)
        
        print(f"Move disk {disk} from peg {peg_names[source]} to peg {peg_names[target]}")
        display_pegs(pegs, move_num, len(moves))
        
        if move_num % 8 == 0 and move_num < len(moves):
            input("Press Enter to continue...")

solve_hanoi(4)
