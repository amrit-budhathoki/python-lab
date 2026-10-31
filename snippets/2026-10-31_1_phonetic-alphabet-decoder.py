# Title: Phonetic Alphabet Decoder

# Ever wonder what secret messages sound like when spelled out loud?
# This program encodes text into NATO phonetic alphabet, then decodes it back.
# Interesting because it shows how homophones can hide messages in plain sound.

import itertools

nato_phonetic = {
    'A': 'Alfa',    'B': 'Bravo',   'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot', 'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett', 'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November','O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',   'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',  'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'
}

reverse_nato = {v: k for k, v in nato_phonetic.items()}

def encode_nato(text):
    """Convert text to NATO phonetic alphabet"""
    words = []
    for char in text.upper():
        if char in nato_phonetic:
            words.append(nato_phonetic[char])
        elif char == ' ':
            words.append('(space)')
        elif char.isdigit():
            words.append(f'({char})')
    return ' '.join(words)

def decode_nato(nato_string):
    """Decode NATO phonetic back to text"""
    words = nato_string.split()
    result = []
    for word in words:
        if word == '(space)':
            result.append(' ')
        elif word.startswith('(') and word.endswith(')'):
            result.append(word[1:-1])
        elif word in reverse_nato:
            result.append(reverse_nato[word])
    return ''.join(result)

def find_anagrams(nato_string):
    """Find alternative decodings using creative word matching"""
    words = nato_string.split()
    possible = []
    for word in words:
        matches = [k for k, v in nato_phonetic.items() if v.lower() == word.lower()]
        if not matches:
            matches = [word]
        possible.append(matches)
    
    combos = list(itertools.product(*possible))
    return [''.join(combo) for combo in combos[:10]]

messages = [
    "HELLO WORLD",
    "SECRET MESSAGE",
    "PYTHON ROCKS"
]

print("=" * 60)
print("NATO PHONETIC CIPHER DECODER")
print("=" * 60)

for msg in messages:
    encoded = encode_nato(msg)
    decoded = decode_nato(encoded)
    
    print(f"\nOriginal:  {msg}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
    print(f"Match:     {msg == decoded} ✓" if msg == decoded else f"Match:     False ✗")

print("\n" + "=" * 60)
print("SOUND-ALIKE DETECTOR")
print("=" * 60)

tricky = "BRAVO ROMEO ALPHA VICTOR OSCAR"
print(f"\nPhonetic string: {tricky}")
decodings = find_anagrams(tricky)
print(f"Possible meanings: {decodings}")
