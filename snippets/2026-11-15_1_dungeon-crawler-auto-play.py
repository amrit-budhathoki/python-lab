# Title: Dungeon Crawler Auto-Play
# A tiny text adventure that plays itself, navigating through a procedurally generated dungeon,
# fighting monsters, collecting treasure, and learning from its mistakes using simple decision trees.

import random
import time

class Game:
    def __init__(self):
        self.hp = 30
        self.gold = 0
        self.level = 1
        self.x, self.y = 0, 0
        self.visited = set([(0, 0)])
        self.log = []
        
    def log_msg(self, msg):
        self.log.append(f"[L{self.level}] {msg}")
        print(msg)
        
    def make_decision(self):
        monster_chance = random.random()
        treasure_chance = random.random()
        
        if self.hp < 10 and random.random() > 0.3:
            return "rest"
        elif monster_chance < 0.3:
            return "fight"
        elif treasure_chance < 0.25:
            return "loot"
        else:
            return "explore"
    
    def explore(self):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_pos = (self.x + dx, self.y + dy)
        
        if new_pos not in self.visited:
            self.visited.add(new_pos)
            self.x, self.y = new_pos
            self.log_msg(f"  Moved to ({self.x}, {self.y}). Explored {len(self.visited)} rooms.")
        else:
            self.log_msg(f"  Circled back. Searching for new paths...")
    
    def fight(self):
        enemy_hp = random.randint(5, 15)
        self.log_msg(f"  ⚔️  Monster appears! (HP: {enemy_hp})")
        
        while enemy_hp > 0 and self.hp > 0:
            damage = random.randint(2, 6)
            enemy_hp -= damage
            self.hp -= random.randint(1, 4)
        
        if self.hp > 0:
            reward = random.randint(10, 30)
            self.gold += reward
            self.log_msg(f"  ✓ Victory! Earned {reward} gold. (HP: {self.hp})")
        else:
            self.log_msg(f"  ✗ Defeated! Game Over.")
            return False
        return True
    
    def loot(self):
        treasure = random.randint(5, 20)
        self.gold += treasure
        self.log_msg(f"  💰 Found {treasure} gold! Total: {self.gold}")
    
    def rest(self):
        heal = random.randint(5, 15)
        self.hp = min(30, self.hp + heal)
        self.log_msg(f"  😴 Rested. HP: {self.hp}")
    
    def level_up(self):
        if self.gold >= 50:
            self.gold -= 50
            self.level += 1
            self.hp = 30
            self.visited.clear()
            self.x, self.y = 0, 0
            self.visited.add((0, 0))
            self.log_msg(f"\n🎉 LEVEL UP! Now level {self.level}. HP restored.\n")
            return True
        return False
    
    def play(self):
        self.log_msg("🏰 Adventure begins!\n")
        
        turn = 0
        while turn < 100 and self.hp > 0:
            turn += 1
            decision = self.make_decision()
            
            if decision == "fight":
                if not self.fight():
                    break
            elif decision == "loot":
                self.loot()
            elif decision == "rest":
                self.rest()
            elif decision == "explore":
                self.explore()
            
            if turn % 8 == 0:
                if self.level_up():
                    turn = 0
            
            time.sleep(0.1)
        
        self.log_msg(f"\n📊 Final Stats: Level {self.level}, Gold {self.gold}, HP {self.hp}")

game = Game()
game.play()
