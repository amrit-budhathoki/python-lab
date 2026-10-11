# Title: Wolfram's Elementary Cellular Automaton

# Explores one of the simplest cellular automata: a 1D rule-based system that
# produces surprisingly complex patterns. Rule 110 is famous for being Turing-complete.
# Watch how a single cell evolves into intricate structures based on simple neighborhood rules.

import random

def evolve(rule_num, state):
    """Apply Wolfram rule to current state, return next generation."""
    rule = format(rule_num, '08b')
    rule_map = {format(i, '03b'): rule[7-i] for i in range(8)}
    
    new_state = ['0'] * len(state)
    for i in range(len(state)):
        left = state[(i - 1) % len(state)]
        center = state[i]
        right = state[(i + 1) % len(state)]
        neighborhood = left + center + right
        new_state[i] = rule_map[neighborhood]
    
    return new_state

def display(state, rule_num):
    """Convert state to displayable characters."""
    return ''.join('█' if cell == '1' else ' ' for cell in state)

def run_automaton(rule_num, generations=30, width=60):
    """Run automaton and display evolution."""
    state = ['0'] * width
    state[width // 2] = '1'
    
    print(f"\nWolfram's Rule {rule_num} (Turing-complete: {rule_num == 110})")
    print("─" * (width + 2))
    
    for gen in range(generations):
        print('│' + display(state, rule_num) + '│')
        state = evolve(rule_num, state)
    
    print("─" * (width + 2))

# Test interesting rules
run_automaton(30)   # Chaotic rule
run_automaton(110)  # Turing-complete rule
run_automaton(184)  # Traffic flow rule
