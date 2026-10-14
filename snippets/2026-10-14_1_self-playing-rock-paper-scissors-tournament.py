# Title: Self-Playing Rock-Paper-Scissors Tournament

# A self-playing tournament where AI agents with different strategies compete.
# Interesting because it demonstrates emergent behavior as strategies adapt based on
# opponent history, creating a dynamic metagame without any external input.

import random
from collections import defaultdict

class Agent:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.history = []
        self.opponent_history = []
        self.wins = 0
    
    def play(self):
        if self.strategy == "random":
            return random.choice(["R", "P", "S"])
        elif self.strategy == "copycat" and self.opponent_history:
            return self.opponent_history[-1]
        elif self.strategy == "counter" and self.opponent_history:
            last = self.opponent_history[-1]
            return {"R": "P", "P": "S", "S": "R"}[last]
        elif self.strategy == "cycle":
            cycle = ["R", "P", "S"]
            return cycle[len(self.history) % 3]
        return "R"
    
    def reset_for_match(self):
        self.history = []
        self.opponent_history = []

def beats(move1, move2):
    wins = {"R": "S", "P": "R", "S": "P"}
    if wins[move1] == move2:
        return 1
    elif wins[move2] == move1:
        return -1
    return 0

def play_match(agent1, agent2, rounds=10):
    agent1.reset_for_match()
    agent2.reset_for_match()
    
    for _ in range(rounds):
        move1 = agent1.play()
        move2 = agent2.play()
        
        result = beats(move1, move2)
        if result == 1:
            agent1.wins += 1
        elif result == -1:
            agent2.wins += 1
        
        agent1.history.append(move1)
        agent1.opponent_history.append(move2)
        agent2.history.append(move2)
        agent2.opponent_history.append(move1)

def display_match(agent1, agent2):
    moves1 = "".join(agent1.history)
    moves2 = "".join(agent2.history)
    print(f"{agent1.name:12} vs {agent2.name:12} | {moves1} vs {moves2} | {agent1.wins}-{agent2.wins}")

print("🎮 Rock-Paper-Scissors AI Tournament\n")
print("=" * 70)

agents = [
    Agent("Random", "random"),
    Agent("Copycat", "copycat"),
    Agent("Counter", "counter"),
    Agent("Cycle", "cycle"),
]

print("\nRound 1: Everyone vs Everyone")
print("-" * 70)
for i, agent1 in enumerate(agents):
    for agent2 in agents[i+1:]:
        play_match(agent1, agent2, 10)
        display_match(agent1, agent2)

print("\n" + "=" * 70)
print("Final Standings:")
print("-" * 70)
sorted_agents = sorted(agents, key=lambda a: a.wins, reverse=True)
for rank, agent in enumerate(sorted_agents, 1):
    print(f"{rank}. {agent.name:12} - {agent.wins} wins")

print("\n🏆 Tournament Complete!")
