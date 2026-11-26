# Title: Infinite Tower Escape

# A text adventure where the AI player automatically climbs a randomly-generated
# tower, makes strategic decisions based on game state, and races against a
# collapsing floor. Watch the AI navigate risk vs reward to escape!

import random
import time

class Tower:
    def __init__(self):
        self.floor = 0
        self.health = 100
        self.inventory = []
        self.collapse_floor = 0
        self.won = False
    
    def describe(self):
        print(f"\n📍 Floor {self.floor} | Health: {self.health}% | Items: {len(self.inventory)} | Collapse at: {self.collapse_floor}")
    
    def generate_event(self):
        events = [
            ("treasure", "Found a glowing crystal! +10 health"),
            ("trap", "Stepped on a spike! -15 health"),
            ("monster", "Encountered a goblin! Must fight!"),
            ("staircase", "Found stairs leading up!"),
            ("potion", "Found a healing potion!"),
        ]
        return random.choice(events)
    
    def play_turn(self):
        event_type, description = self.generate_event()
        print(f"  {description}")
        
        if event_type == "treasure":
            self.inventory.append("crystal")
            self.health = min(100, self.health + 10)
        elif event_type == "trap":
            self.health -= 15
        elif event_type == "monster":
            if "sword" in self.inventory:
                print(f"    ⚔️  Used sword to defeat goblin!")
                self.inventory.remove("sword")
            else:
                self.health -= 20
        elif event_type == "staircase":
            self.floor += 1
            print(f"    🪜 Climbed to floor {self.floor}!")
        elif event_type == "potion":
            self.inventory.append("potion")
        
        if "potion" in self.inventory and self.health < 50:
            self.health = min(100, self.health + 30)
            self.inventory.remove("potion")
            print(f"    💊 Used potion! Health now {self.health}%")
        
        self.health = max(0, self.health)
        
        if self.floor > self.collapse_floor + 3 and random.random() < 0.4:
            self.collapse_floor = self.floor
            print(f"    ⚠️  Floor below collapsed! Must keep climbing!")
    
    def ai_decision(self):
        if self.health <= 0:
            return False
        if self.floor >= 10:
            self.won = True
            return False
        return True

def main():
    print("=" * 50)
    print("🏰 INFINITE TOWER ESCAPE 🏰")
    print("=" * 50)
    print("Watch the AI climb the tower, dodge traps, and escape!\n")
    
    tower = Tower()
    turn = 0
    
    while tower.ai_decision():
        turn += 1
        tower.describe()
        tower.play_turn()
        time.sleep(0.5)
        
        if turn > 50:
            break
    
    print("\n" + "=" * 50)
    if tower.won:
        print("🎉 SUCCESS! The AI escaped the tower!")
    else:
        print("💀 GAME OVER! The tower claimed another victim.")
    print(f"Final Floor: {tower.floor} | Final Health: {tower.health}%")
    print("=" * 50)

if __name__ == "__main__":
    main()
