# Title: Dungeon Crawler Auto-Play

# A text adventure game that plays itself! Watch as an AI agent navigates
# a procedurally generated dungeon, fights monsters, collects treasure, and
# learns which strategies work best through repeated playthroughs.

import random
from collections import defaultdict

class DungeonGame:
    def __init__(self):
        self.rooms = {i: {"monsters": random.randint(0, 3), "treasure": random.randint(0, 2)} for i in range(8)}
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.episodes = 20
        
    def play_episode(self, learning=True):
        pos, hp, gold = 0, 10, 0
        history = []
        
        while hp > 0 and pos < 7:
            state = (pos, min(hp, 3), min(gold, 2))
            actions = ["move", "fight", "heal"] if hp < 10 else ["move", "fight"]
            
            if learning and random.random() < 0.2:
                action = random.choice(actions)
            else:
                action = max(actions, key=lambda a: self.q_table[state][a])
            
            reward = 0
            if action == "move":
                pos = min(pos + 1, 7)
                reward = 1
            elif action == "fight":
                monsters = self.rooms[pos]["monsters"]
                if monsters > 0:
                    hp -= monsters * 2
                    reward = monsters * 5
                    self.rooms[pos]["monsters"] = 0
                else:
                    reward = -2
            elif action == "heal":
                hp = min(hp + 3, 10)
                reward = -1
            
            if pos == 7:
                reward += 50
                
            history.append((state, action, reward))
            
            if learning:
                self.q_table[state][action] += 0.1 * (reward + 0.9 * max(self.q_table[(pos, min(hp, 3), min(gold + self.rooms[pos].get("treasure", 0), 2))].values() or [0]))
        
        return len(history), hp > 0, history
    
    def run(self):
        print("🎮 DUNGEON CRAWLER AUTO-PLAY 🎮\n")
        for ep in range(self.episodes):
            steps, survived, _ = self.play_episode(learning=True)
            status = "✓ VICTORY" if survived else "✗ DEAD"
            print(f"Episode {ep+1:2d}: {steps:2d} steps - {status}")
        
        print("\n📊 FINAL TEST RUN:\n")
        steps, survived, history = self.play_episode(learning=False)
        for i, (state, action, reward) in enumerate(history):
            pos, hp, gold = state
            print(f"  Step {i+1}: Room {pos} | HP:{hp} | Action: {action:6s} | Reward: {reward:+3d}")
        print(f"\n🏁 Final: {'ESCAPED!' if survived else 'PERISHED!'} ({steps} moves)")

if __name__ == "__main__":
    game = DungeonGame()
    game.run()
