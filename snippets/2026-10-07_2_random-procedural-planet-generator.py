# Title: Random Procedural Planet Generator

# Generates quirky alien planets with random names, climates, and inhabitants.
# Fun because each planet is completely unique and the descriptions are absurdly specific.

import random

def generate_planet():
    prefixes = ["Zyx", "Krel", "Vor", "Thex", "Nyx", "Psi", "Omeg", "Tau"]
    suffixes = ["ia", "on", "us", "ar", "ex", "or", "yx", "el"]
    planet_name = random.choice(prefixes) + random.choice(suffixes)
    
    colors = ["crimson", "azure", "chartreuse", "magenta", "silver", "obsidian"]
    color = random.choice(colors)
    
    climates = [
        "scorching desert with glass dunes",
        "perpetual thunderstorm zone",
        "frozen methane tundra",
        "acid rain jungle",
        "zero-gravity asteroid field",
        "bioluminescent swamp"
    ]
    climate = random.choice(climates)
    
    inhabitants = [
        "silicon-based crystalline beings",
        "sentient gas clouds",
        "tentacled philosophers",
        "microscopic hive minds",
        "floating geometric entities",
        "underground mushroom civilizations"
    ]
    inhabitant = random.choice(inhabitants)
    
    gravity = round(random.uniform(0.1, 3.5), 2)
    diameter = random.randint(2000, 20000)
    age = random.randint(100, 9999)
    
    days_per_year = random.randint(50, 500)
    moons = random.randint(0, 7)
    
    print(f"\n🌍 Planet: {planet_name}")
    print(f"   Color: {color}")
    print(f"   Climate: {climate}")
    print(f"   Diameter: {diameter:,} km")
    print(f"   Gravity: {gravity}g")
    print(f"   Age: {age} million years")
    print(f"   Days per year: {days_per_year}")
    print(f"   Moons: {moons}")
    print(f"   Inhabitants: {inhabitant}")
    print(f"   Habitability: {'⭐' * random.randint(1, 5)}")

print("═" * 50)
print("RANDOM PROCEDURAL PLANET GENERATOR")
print("═" * 50)

for _ in range(5):
    generate_planet()

print("\n" + "═" * 50)
