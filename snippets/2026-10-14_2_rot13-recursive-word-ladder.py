# Title: ROT13 Recursive Word Ladder

# This program creates a word ladder using ROT13 cipher tricks, where each step
# transforms a word by rotating letters and showing how words "evolve" through
# cipher space. It's interesting because it visualizes how simple ciphers create
# unexpected semantic bridges between seemingly unrelated words.

import random
from string import ascii_lowercase

def rot_n(text, n):
    """Rotate each letter in text by n positions in alphabet."""
    return ''.join(
        ascii_lowercase[(ascii_lowercase.index(c) + n) % 26]
        if c in ascii_lowercase else c
        for c in text.lower()
    )

def find_ladder(word, depth, max_depth=5, visited=None):
    """Build a ladder by applying different rotations until reaching max depth."""
    if visited is None:
        visited = set()
    
    if depth >= max_depth or word in visited:
        return [word]
    
    visited.add(word)
    
    # Try a few random rotations
    rotations = random.sample(range(1, 26), min(3, 25))
    
    for rotation in rotations:
        next_word = rot_n(word, rotation)
        # Only continue if it creates an "interesting" looking word
        if next_word not in visited and sum(1 for c in next_word if c in ascii_lowercase) >= 3:
            ladder = find_ladder(next_word, depth + 1, max_depth, visited)
            return [word] + ladder
    
    return [word]

def cipher_transform_show(start_word, steps):
    """Show a word transforming through cipher space with rotations."""
    print(f"\n🔀 Cipher Ladder starting from: {start_word}")
    print("=" * 50)
    
    current = start_word
    for i in range(steps):
        rotation = random.randint(1, 13)
        next_word = rot_n(current, rotation)
        
        # Show the transformation
        print(f"Step {i+1} (ROT{rotation}): {current:12} → {next_word:12}", end="")
        
        # Analyze "distance"
        diff = sum(1 for a, b in zip(current, next_word) if a != b)
        print(f"  [{diff} letters changed]")
        
        current = next_word

def main():
    """Main program: show multiple cipher tricks."""
    print("✨ CIPHER TRANSFORM TRICKS ✨")
    print()
    
    words = ["hello", "python", "cipher", "secret", "magic"]
    
    # Trick 1: Progressive rotation
    for word in random.sample(words, 3):
        cipher_transform_show(word, 5)
    
    print("\n" + "=" * 50)
    print("🎲 RANDOM ROTATION PALINDROME CHECK")
    print("=" * 50)
    
    # Trick 2: Find when rotation creates near-palindromes
    test_word = "code"
    print(f"\nSearching for interesting rotations of '{test_word}':")
    
    for rotation in range(1, 26):
        rotated = rot_n(test_word, rotation)
        reverse = rotated[::-1]
        
        # Count matching positions with reverse
        matches = sum(1 for a, b in zip(rotated, reverse) if a == b)
        
        if matches >= 2:
            print(f"  ROT{rotation:2d}: {rotated} vs {reverse} - {matches} matches!")

if __name__ == "__main__":
    random.seed(42)
    main()
