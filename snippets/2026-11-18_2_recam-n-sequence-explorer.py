# Title: Recamán Sequence Explorer

# The Recamán sequence is a deceptively simple but chaotic integer sequence where each term
# is computed by subtracting or adding the step number, creating intricate patterns of jumps
# and loops. This program visualizes the sequence as an ASCII spiral, showing how the numbers
# bounce around in a beautiful, unpredictable dance that reveals hidden structure.

def recaman_sequence(n):
    """Generate first n terms of Recamán sequence"""
    seen = set()
    sequence = []
    current = 0
    seen.add(0)
    sequence.append(0)
    
    for i in range(1, n):
        # Try subtracting first
        candidate = current - i
        if candidate >= 0 and candidate not in seen:
            current = candidate
        else:
            # Otherwise add
            current = current + i
        
        seen.add(current)
        sequence.append(current)
    
    return sequence

def spiral_coordinates(index):
    """Convert linear index to spiral coordinates (Ulam spiral style)"""
    if index == 0:
        return 0, 0
    
    layer = 0
    side_length = 1
    pos_in_layer = index - 1
    
    while pos_in_layer >= side_length * 4:
        pos_in_layer -= side_length * 4
        layer += 1
        side_length += 1
    
    x, y = layer, -layer
    
    # Right side, moving up
    if pos_in_layer < side_length:
        x += pos_in_layer
    # Top side, moving left
    elif pos_in_layer < side_length * 2:
        x = layer
        y = -layer + (pos_in_layer - side_length)
    # Left side, moving down
    elif pos_in_layer < side_length * 3:
        x = layer - (pos_in_layer - side_length * 2)
        y = layer
    # Bottom side, moving right
    else:
        x = -layer
        y = layer - (pos_in_layer - side_length * 3)
    
    return x, y

def visualize_recaman(terms=200, size=40):
    """Visualize Recamán sequence on a grid"""
    sequence = recaman_sequence(terms)
    
    grid = {}
    max_coord = size // 2
    
    for index, value in enumerate(sequence):
        x, y = spiral_coordinates(index)
        if abs(x) <= max_coord and abs(y) <= max_coord:
            # Mark positions with step count (mod 10 for variety)
            grid[(x, y)] = str(index % 10)
    
    print("Recamán Sequence Spiral (first {} terms):\n".format(terms))
    for y in range(-max_coord, max_coord + 1):
        row = ""
        for x in range(-max_coord, max_coord + 1):
            if (x, y) in grid:
                row += grid[(x, y)]
            elif x == 0 and y == 0:
                row += "S"
            else:
                row += "·"
        print(row)
    
    print("\nSequence start: {}".format(sequence[:20]))
    print("Max value reached: {}".format(max(sequence)))
    print("Unique values: {}/{}".format(len(set(sequence)), len(sequence)))

visualize_recaman()
