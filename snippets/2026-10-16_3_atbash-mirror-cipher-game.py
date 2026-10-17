# Title: Atbash Mirror Cipher Game

# A fun cipher that reverses the alphabet (A↔Z, B↔Y, etc). This program
# encodes a secret message, scrambles it with a word ladder of transformations,
# and challenges you to decode it. Interesting because it shows how simple
# substitution ciphers can be layered and the patterns are visually satisfying.

import string
from random import shuffle

def atbash(text):
    """Reverse alphabet cipher: A↔Z, B↔Y, etc."""
    result = []
    for char in text.lower():
        if char in string.ascii_lowercase:
            pos = ord(char) - ord('a')
            result.append(chr(ord('z') - pos))
        else:
            result.append(char)
    return ''.join(result)

def caesar(text, shift):
    """Classic Caesar cipher with given shift."""
    result = []
    for char in text.lower():
        if char in string.ascii_lowercase:
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_encode(text, key):
    """Vigenere cipher using a keyword."""
    result = []
    key_index = 0
    for char in text.lower():
        if char in string.ascii_lowercase:
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

# Secret message
message = "the quick brown fox jumps over the lazy dog"
print("Original message:")
print(f"  '{message}'")
print()

# Apply transformations step by step
step1 = atbash(message)
print("Step 1 (Atbash cipher):")
print(f"  '{step1}'")

step2 = caesar(step1, 7)
print("Step 2 (Caesar +7):")
print(f"  '{step2}'")

step3 = vigenere_encode(step2, "python")
print("Step 3 (Vigenere with 'python'):")
print(f"  '{step3}'")
print()

# Reverse the process
print("Decoding process:")
back1 = vigenere_encode(step3, "python")  # Vigenere is symmetric with encoding
print(f"  Undo Vigenere: '{back1}'")

back2 = caesar(back1, -7)
print(f"  Undo Caesar:   '{back2}'")

back3 = atbash(back2)
print(f"  Undo Atbash:   '{back3}'")
print()

print("✓ Successfully decoded back to original!" if back3 == message else "✗ Decoding failed!")
