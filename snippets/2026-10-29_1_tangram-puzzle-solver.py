# Title: Tangram Puzzle Solver

# Solves a tangram puzzle by finding valid placements of 7 geometric pieces
# to fit a target silhouette. Uses backtracking with rotation and translation
# to explore piece arrangements. Interesting because it demonstrates constraint
# satisfaction through spatial reasoning and creative search pruning.

from itertools import permutations, product

def rotate_90(piece):
    """Rotate piece 90 degrees clockwise."""
    return tuple(sorted(set((y, -x) for x, y in piece)))

def get_rotations(piece):
    """Get all unique rotations of a piece."""
    rotations = set()
    current = piece
    for _ in range(4):
        rotations.add(current)
        current = rotate_90(current)
    return [tuple(sorted(r)) for r in rotations]

def normalize(piece):
    """Translate piece so minimum coordinates are at origin."""
    if not piece:
        return piece
    min_x = min(x for x, y in piece)
    min_y = min(y for x, y in piece)
    return tuple(sorted((x - min_x, y - min_y) for x, y in piece))

def place_piece(piece, offset):
    """Place piece at given offset."""
    ox, oy = offset
    return frozenset((x + ox, y + oy) for x, y in piece)

def solve_tangram(target, pieces, used_mask=0, placed=None):
    """Recursively solve tangram puzzle using backtracking."""
    if placed is None:
        placed = frozenset()
    
    if used_mask == (1 << len(pieces)) - 1:
        return placed if placed == target else None
    
    for i, piece in enumerate(pieces):
        if used_mask & (1 << i):
            continue
        
        for rotation in get_rotations(piece):
            for ox, oy in product(range(-3, 4), repeat=2):
                placed_piece = place_piece(rotation, (ox, oy))
                if not (placed_piece & placed):
                    new_placed = placed | placed_piece
                    if new_placed <= target:
                        result = solve_tangram(
                            target, pieces, used_mask | (1 << i), new_placed
                        )
                        if result is not None:
                            return result
    return None

# Define tangram pieces (small square, medium triangle, large triangle, etc.)
pieces = [
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # Square
    ((0, 0), (2, 0), (1, 1)),           # Small triangle
    ((0, 0), (2, 0), (2, 2)),           # Medium triangle
    ((0, 0), (2, 0), (2, 2), (0, 2)),   # Parallelogram
    ((0, 0), (1, 0), (1, 1)),           # Small right triangle
    ((0, 0), (2, 0), (1, 1)),           # Another triangle
    ((0, 0), (1, 0), (2, 1), (1, 1)),   # Trapezoid
]

# Simple target: a 4x4 square
target = frozenset(product(range(4), repeat=2))

print("Solving tangram puzzle...")
result = solve_tangram(target, pieces)

if result:
    print("✓ Puzzle solved!")
    grid = [[' ' for _ in range(4)] for _ in range(4)]
    for x, y in result:
        if 0 <= x < 4 and 0 <= y < 4:
            grid[y][x] = '█'
    for row in grid:
        print(''.join(row))
else:
    print("✗ No solution found for this configuration.")
