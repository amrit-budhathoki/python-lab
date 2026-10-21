# Title: Random Fantasy Name and Stat Generator

# Generates random fantasy character names and stats with D&D-style attributes.
# Fun because it creates endless unique characters with personality through random
# combinations of syllables, fantasy suffixes, and randomized ability scores.

import random

def generate_name():
    prefixes = ["Ar", "Thel", "Grim", "Aur", "Val", "Mor", "Syl", "Kael", "Dor", "Zyx"]
    middles = ["en", "dor", "eth", "ian", "or", "ar", "il", "us", "ax", "on"]
    suffixes = ["dor", "eth", "iel", "ian", "ox", "us", "ax", "ir", "an", "or"]
    return random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)

def roll_stats():
    rolls = []
    for _ in range(6):
        dice = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
        rolls.append(sum(dice[:3]))
    return rolls

def get_class(stats):
    classes = {
        0: ("Barbarian", "STR"),
        1: ("Rogue", "DEX"),
        2: ("Cleric", "WIS"),
        3: ("Sorcerer", "CHA"),
        4: ("Wizard", "INT"),
        5: ("Ranger", "CON")
    }
    best_stat_idx = stats.index(max(stats))
    return classes[best_stat_idx]

def get_race():
    races = ["Human", "Elf", "Dwarf", "Orc", "Tiefling", "Dragonborn", "Halfling", "Gnome"]
    return random.choice(races)

def get_alignment():
    laws = ["Lawful", "Neutral", "Chaotic"]
    morals = ["Good", "Neutral", "Evil"]
    return random.choice(laws) + " " + random.choice(morals)

def print_character():
    name = generate_name()
    race = get_race()
    stats = roll_stats()
    class_name, primary_stat = get_class(stats)
    alignment = get_alignment()
    
    stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    
    print(f"\n{'='*50}")
    print(f"Name: {name.upper()}")
    print(f"Race: {race} | Class: {class_name}")
    print(f"Alignment: {alignment}")
    print(f"-" * 50)
    for stat_name, stat_val in zip(stat_names, stats):
        marker = " ◆" if stat_name == primary_stat else ""
        print(f"{stat_name}: {stat_val:2d}{marker}")
    print(f"{'='*50}")

if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════╗")
    print("║     FANTASY CHARACTER GENERATOR                   ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    for _ in range(5):
        print_character()
