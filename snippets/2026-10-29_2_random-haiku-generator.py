# Title: Random Haiku Generator

# Generates random haikus by selecting words that fit the 5-7-5 syllable structure.
# Interesting because it combines poetry with randomness, creating unique haikus each time.

import random

syllables = {
    1: ['cat', 'dog', 'rain', 'snow', 'moon', 'sun', 'tree', 'wind', 'spring', 'pond', 'stream', 'path', 'stone', 'bird', 'flower'],
    2: ['cherry', 'willow', 'water', 'garden', 'winter', 'autumn', 'summer', 'morning', 'evening', 'silence', 'whisper', 'shadow', 'dancer', 'painter'],
}

verbs_1 = ['falls', 'blooms', 'glows', 'flows', 'drifts', 'calls']
verbs_2 = ['dancing', 'falling', 'singing', 'flowing', 'resting', 'waiting']

def word_by_count(count):
    if count in syllables:
        return random.choice(syllables[count])
    return "nature"

def line_5():
    a = word_by_count(2)
    b = word_by_count(3)
    return f"{a} {b}"

def line_7():
    a = word_by_count(3)
    b = random.choice(verbs_2)
    c = word_by_count(2)
    return f"{a} {b} {c}"

def haiku():
    return "\n".join([line_5(), line_7(), line_5()])

def generate_haiku():
    words_5_1 = ['morning', 'garden', 'moonlight']
    words_5_2 = ['whispers', 'blossoms', 'waters']
    
    line1 = f"{random.choice(words_5_1)} {random.choice(word_by_count(1) for _ in range(1))}"
    line2 = f"{random.choice(words_5_2)} {random.choice(verbs_2)} {random.choice(word_by_count(1) for _ in range(1))}"
    line3 = f"{random.choice(words_5_1)} {random.choice(word_by_count(1) for _ in range(1))}"
    
    return f"{line1}\n{line2}\n{line3}"

for i in range(3):
    print(haiku())
    print()
