# Title: Polybius Square Cipher Decoder
# A classic cipher that maps letters to coordinate pairs. This program encodes a secret message
# into a grid, then decodes it back by treating digit pairs as row/column positions. Fun because
# you can visually see the pattern and it's historically used by spies and prisoners.

import random

def encode_message(message):
    """Encode message using Polybius square coordinates."""
    grid = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 25 letters (I/J combined)
    encoded = []
    for char in message.upper():
        if char in grid:
            pos = grid.index(char)
            row = pos // 5 + 1
            col = pos % 5 + 1
            encoded.append(f"{row}{col}")
    return "".join(encoded)

def decode_message(encoded):
    """Decode Polybius square coordinates back to message."""
    grid = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    decoded = []
    for i in range(0, len(encoded), 2):
        if i + 1 < len(encoded):
            row = int(encoded[i]) - 1
            col = int(encoded[i + 1]) - 1
            pos = row * 5 + col
            if 0 <= pos < len(grid):
                decoded.append(grid[pos])
    return "".join(decoded)

def display_grid():
    """Show the Polybius square visually."""
    grid = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    print("\n  Polybius Square:")
    print("    1 2 3 4 5")
    for row in range(5):
        print(f"  {row + 1} {' '.join(grid[row*5:(row+1)*5])}")
    print()

# Main demo
messages = [
    "HELLO WORLD",
    "SECRET MESSAGE",
    "POLYBIUS CIPHER",
    "PYTHON ROCKS"
]

display_grid()

for msg in messages:
    clean_msg = "".join(c for c in msg if c.isalpha())
    encoded = encode_message(clean_msg)
    decoded = decode_message(encoded)
    
    print(f"Original:  {clean_msg}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
    print(f"Match:     {clean_msg == decoded} ✓" if clean_msg == decoded else f"Match:     False ✗")
    print()

# Bonus: scramble a message by taking random pairs
print("Scrambled coordinate pairs from 'CODEBREAKER':")
test = encode_message("CODEBREAKER")
pairs = [test[i:i+2] for i in range(0, len(test), 2)]
random.shuffle(pairs)
print(f"Original coordinates: {test}")
print(f"Scrambled pairs:      {''.join(pairs)}")
print(f"Decoded from scramble: {decode_message(''.join(pairs))}")
