# Title: Procedural Planet Generator

# Generates random alien planets with realistic properties: names, sizes, atmospheric compositions, and habitability ratings. Fun because each planet is unique and the descriptions create a sense of cosmic discovery!

import random

def generate_planet():
    syllables = ['Zeta', 'Krypton', 'Vex', 'Thal', 'Proxima', 'Nyx', 'Zorb', 'Kepler', 'Tau', 'Gliese']
    suffixes = ['-7b', '-Prime', '-X', '-Omega', '-Terra', '-II', '-Nova', '-Rex']
    name = random.choice(syllables) + random.choice(suffixes)
    
    planet_type = random.choices(
        ['Rocky', 'Gas Giant', 'Ice World', 'Desert', 'Ocean', 'Volcanic'],
        weights=[30, 20, 15, 15, 12, 8]
    )[0]
    
    diameter = random.randint(4000, 150000)
    gravity = round(random.uniform(0.3, 3.5), 2)
    temp = random.randint(-250, 500)
    
    atmosphere = random.choices(
        ['None', 'Thin CO₂', 'Thick N₂', 'O₂-rich', 'Methane', 'Toxic', 'Unknown'],
        weights=[10, 15, 20, 15, 10, 15, 15]
    )[0]
    
    water = random.choices(['None', 'Trace', 'Partial', 'Abundant'], weights=[20, 30, 35, 15])[0]
    
    life = 'None'
    if temp > -40 and temp < 80 and atmosphere != 'None' and atmosphere != 'Unknown':
        if water in ['Partial', 'Abundant']:
            life = random.choices(['Microbial', 'Simple Flora', 'Complex Life', 'Civilized'], weights=[40, 35, 20, 5])[0]
    
    habitability = 0
    if temp > -30 and temp < 50:
        habitability += 30
    if atmosphere in ['O₂-rich', 'Thick N₂']:
        habitability += 25
    if water in ['Partial', 'Abundant']:
        habitability += 25
    if gravity > 0.8 and gravity < 1.5:
        habitability += 20
    
    return {
        'name': name,
        'type': planet_type,
        'diameter_km': diameter,
        'gravity_g': gravity,
        'temp_c': temp,
        'atmosphere': atmosphere,
        'water': water,
        'life': life,
        'habitability': min(100, habitability)
    }

def display_planet(planet):
    print(f"\n🌍 PLANET: {planet['name']}")
    print(f"   Type: {planet['type']}")
    print(f"   Diameter: {planet['diameter_km']:,} km")
    print(f"   Surface Gravity: {planet['gravity_g']}G")
    print(f"   Temperature: {planet['temp_c']}°C")
    print(f"   Atmosphere: {planet['atmosphere']}")
    print(f"   Water: {planet['water']}")
    print(f"   Life: {planet['life']}")
    print(f"   Habitability Score: {planet['habitability']}/100")
    if planet['habitability'] > 70:
        print(f"   ✨ EXCELLENT for colonization!")
    elif planet['habitability'] > 40:
        print(f"   ⚠️  MODERATE potential with technology")

print("=" * 50)
print("       GALACTIC SURVEY SYSTEM v3.7")
print("=" * 50)

for i in range(6):
    planet = generate_planet()
    display_planet(planet)

print("\n" + "=" * 50)
print(f"Scanned 6 star systems. Safe travels!")
