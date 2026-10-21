# Title: Cosmic Name Generator

# Generates random sci-fi alien species names and their homeworlds with fun traits.
# Interesting because it combines phonetic rules with randomized syllables to create
# pronounceable yet varied fantasy names, plus planetary characteristics.

import random

def generate_syllable():
    consonants = "bkmnpqrstvxzthqghlj"
    vowels = "aeiouy"
    patterns = [
        lambda: random.choice(consonants),
        lambda: random.choice(consonants) + random.choice(vowels),
        lambda: random.choice(vowels) + random.choice(consonants),
        lambda: random.choice(consonants) + random.choice(vowels) + random.choice(consonants),
    ]
    return random.choice(patterns)()

def generate_species_name():
    syllables = random.randint(2, 4)
    name = "".join(generate_syllable() for _ in range(syllables))
    return name.capitalize()

def generate_planet_name():
    prefixes = ["Prime", "Neo", "Alpha", "Zeta", "Tau", "Kepler", "Gliese", "TRAPPIST"]
    suffixes = ["-1", "-7b", "-9d", "-12g", "-3c"]
    return random.choice(prefixes) + random.choice(suffixes)

def generate_trait():
    traits = [
        "silicon-based lifeforms",
        "telepathic hive minds",
        "nocturnal predators",
        "photosynthetic beings",
        "crystalline exoskeletons",
        "aquatic colonizers",
        "gravity-resistant floaters",
        "sentient fungi network",
        "bioluminescent communicators",
        "quantum-entangled consciousness",
    ]
    return random.choice(traits)

def generate_planet_type():
    types = [
        "barren desert world",
        "frozen ice giant",
        "toxic swamp moon",
        "carbon asteroid",
        "molten super-Earth",
        "lush jungle world",
        "underground cavern system",
    ]
    return random.choice(types)

def generate_cosmic_entry():
    species = generate_species_name()
    planet = generate_planet_name()
    trait = generate_trait()
    world = generate_planet_type()
    
    return f"Species: {species}\n  Homeworld: {planet} ({world})\n  Notable trait: {trait}"

print("╔════════════════════════════════════════════╗")
print("║     COSMIC SPECIES & HOMEWORLD ARCHIVE     ║")
print("╚════════════════════════════════════════════╝\n")

for _ in range(8):
    print(generate_cosmic_entry())
    print()
