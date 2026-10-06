# Title: Random Haiku Generator

# Generates random haikus by selecting random words from syllable-organized categories.
# Interesting because it creates valid 5-7-5 syllable poems that are sometimes genuinely poetic!

import random

# Word pool organized by syllable count
syllables = {
    1: ["mist", "wind", "rain", "snow", "moon", "dawn", "dusk", "spring", "fall", "heat", "cold", "dream", "peace", "stone", "tree", "wave", "fire", "ice", "sun", "night"],
    2: ["falling", "rising", "shadow", "silence", "whisper", "echo", "gentle", "silent", "silver", "golden", "crimson", "midnight", "morning", "winter", "summer", "evening", "lonely", "fragile"],
    3: ["wandering", "floating", "whispered", "forgotten", "dancing", "trembling", "glowing", "flowing", "awakened", "fading", "endless", "eternal"],
}

def get_words(count, target_syllables):
    """Get random words that sum to target syllables"""
    words = []
    remaining = target_syllables
    
    while remaining > 0:
        # Pick a syllable count that doesn't exceed remaining
        available = [s for s in syllables.keys() if s <= remaining]
        if not available:
            break
        
        syl = random.choice(available)
        words.append(random.choice(syllables[syl]))
        remaining -= syl
    
    return words if len(words) == count else get_words(count, target_syllables)

def generate_haiku():
    """Generate a random haiku with 5-7-5 syllable structure"""
    line1 = " ".join(get_words(2, 5))
    line2 = " ".join(get_words(3, 7))
    line3 = " ".join(get_words(2, 5))
    
    return f"{line1.capitalize()}\n{line2.capitalize()}\n{line3.capitalize()}"

# Generate and display 3 haikus
for i in range(3):
    print(f"Haiku {i + 1}:")
    print(generate_haiku())
    print()
