# Title: Cosmic Name Generator

# Generates random alien species names and their planets using procedural rules.
# Fun because it creates believable sci-fi names with consistent phonetics per species.

import random

def generate_phonemes():
    """Create lists of consonant and vowel phonemes"""
    consonants = ['z', 'k', 'th', 'sh', 'x', 'v', 'qu', 'kr', 'br', 'gl', 'tr', 'dr', 'sp', 'st']
    vowels = ['a', 'e', 'i', 'o', 'u', 'ae', 'ai', 'ei', 'oi', 'ou']
    return consonants, vowels

def generate_species_name(consonants, vowels):
    """Generate a unique alien species name"""
    length = random.randint(2, 4)
    name = ""
    for i in range(length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()

def generate_planet_name(species_name, consonants, vowels):
    """Generate a planet name related to the species"""
    prefix = species_name[:random.randint(2, 3)].lower()
    suffix_length = random.randint(1, 2)
    suffix = ""
    for i in range(suffix_length):
        if i % 2 == 0:
            suffix += random.choice(consonants)
        else:
            suffix += random.choice(vowels)
    return (prefix + suffix).capitalize()

def generate_planet_traits():
    """Generate random planetary characteristics"""
    climates = ['desert', 'frozen', 'tropical', 'volcanic', 'oceanic', 'toxic']
    sizes = ['dwarf', 'earth-sized', 'super-earth', 'gas giant', 'binary']
    moons = random.randint(0, 7)
    return random.choice(climates), random.choice(sizes), moons

def main():
    """Generate a cosmic civilization report"""
    consonants, vowels = generate_phonemes()
    
    print("=" * 50)
    print("COSMIC CIVILIZATION REPORT")
    print("=" * 50)
    
    num_species = random.randint(3, 6)
    
    for i in range(num_species):
        species = generate_species_name(consonants, vowels)
        planet = generate_planet_name(species, consonants, vowels)
        climate, size, moons = generate_planet_traits()
        
        print(f"\nSpecies {i+1}: {species}")
        print(f"  Homeworld: {planet}")
        print(f"  Climate: {climate}")
        print(f"  Size: {size}")
        print(f"  Moons: {moons}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    random.seed()
    main()
