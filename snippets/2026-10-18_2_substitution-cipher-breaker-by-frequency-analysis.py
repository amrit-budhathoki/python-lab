# Title: Substitution Cipher Breaker by Frequency Analysis

# This program demonstrates how to break a simple substitution cipher
# by analyzing letter frequency patterns and comparing them to English.
# It's interesting because it shows a practical cryptanalysis technique
# that works on any reasonably long substitution-encrypted text.

import string
from collections import Counter

def frequency_analysis(text):
    """Return sorted letter frequencies in text"""
    letters = [c.upper() for c in text if c.isalpha()]
    freq = Counter(letters)
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

def create_cipher_map(cipher_freq, english_freq):
    """Map cipher letters to likely plaintext based on frequency"""
    mapping = {}
    for (cipher_letter, _), (english_letter, _) in zip(cipher_freq, english_freq):
        mapping[cipher_letter] = english_letter
    return mapping

def decrypt_with_map(ciphertext, mapping):
    """Apply substitution mapping to decrypt"""
    result = []
    for char in ciphertext:
        upper_char = char.upper()
        if upper_char in mapping:
            decrypted = mapping[upper_char]
            result.append(decrypted if char.isupper() else decrypted.lower())
        else:
            result.append(char)
    return ''.join(result)

# English letter frequency (approximate)
english_freq = [('E', 12.70), ('T', 9.06), ('A', 8.17), ('O', 7.51),
                 ('I', 6.97), ('N', 6.75), ('S', 6.33), ('H', 6.09),
                 ('R', 5.99), ('D', 4.25), ('L', 4.03), ('C', 2.78),
                 ('U', 2.76), ('M', 2.41), ('W', 2.36), ('F', 2.23),
                 ('G', 2.02), ('Y', 1.97), ('P', 1.93), ('B', 1.29),
                 ('V', 0.98), ('K', 0.77), ('J', 0.15), ('X', 0.15),
                 ('Q', 0.10), ('Z', 0.07)]

# Sample text (from "The Quick Brown Fox")
original = "The quick brown fox jumps over the lazy dog"

# Simple substitution cipher: shift each letter by 5
cipher_key = str.maketrans(
    string.ascii_uppercase,
    string.ascii_uppercase[5:] + string.ascii_uppercase[:5]
)
ciphertext = original.upper().translate(cipher_key)

print("=" * 50)
print("SUBSTITUTION CIPHER BREAKER")
print("=" * 50)
print(f"Original:  {original}")
print(f"Encrypted: {ciphertext}")
print()

# Analyze frequencies in ciphertext
cipher_freq = frequency_analysis(ciphertext)
print("Cipher letter frequencies (top 10):")
for letter, count in cipher_freq[:10]:
    print(f"  {letter}: {count}")
print()

# Create and apply frequency-based mapping
mapping = create_cipher_map(cipher_freq, english_freq)
decrypted = decrypt_with_map(ciphertext, mapping)

print("Decryption mapping (first 10):")
for i, (cipher_letter, plain_letter) in enumerate(sorted(mapping.items())[:10]):
    print(f"  {cipher_letter} → {plain_letter}")
print()

print(f"Decrypted:  {decrypted}")
print()
print("Success!" if decrypted.upper() == original.upper() else "Partial match (longer texts work better)")
