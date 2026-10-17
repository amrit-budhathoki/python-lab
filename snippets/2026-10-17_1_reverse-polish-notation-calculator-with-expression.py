# Title: Reverse Polish Notation Calculator with Expression Reversal

# This program demonstrates a fun cipher/trick: it encodes math expressions
# in Reverse Polish Notation (RPN), then reveals the "trick" by showing how
# the same sequence of numbers read backwards creates a completely different
# valid expression. It's a mathematical palindrome of sorts!

import random
from collections import deque

def evaluate_rpn(tokens):
    """Evaluate an expression in Reverse Polish Notation"""
    stack = deque()
    for token in tokens:
        if token in "+-*/":
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return None
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0] if len(stack) == 1 else None

def find_magic_sequences():
    """Find RPN sequences that work forwards and backwards"""
    magic_tricks = []
    
    # Try different RPN sequences
    for _ in range(1000):
        length = random.randint(3, 7)
        tokens = []
        
        # Build a random valid RPN expression
        for i in range(length):
            if random.random() < 0.6 or len(tokens) < 2:
                tokens.append(str(random.randint(1, 9)))
            else:
                tokens.append(random.choice("+-*"))
        
        result_forward = evaluate_rpn(tokens)
        
        # Try reversing and see if it's also valid
        reversed_tokens = tokens[::-1]
        result_backward = evaluate_rpn(reversed_tokens)
        
        if result_forward is not None and result_backward is not None:
            magic_tricks.append((tokens, result_forward, reversed_tokens, result_backward))
    
    return magic_tricks

def format_rpn(tokens):
    """Convert RPN tokens to a readable string"""
    return " ".join(str(t) for t in tokens)

# Main program
print("=" * 60)
print("RPN CIPHER TRICK: Expressions that Work Backwards Too!")
print("=" * 60)
print()

tricks = find_magic_sequences()

# Show the best ones (where forward and backward results differ)
interesting_tricks = [t for t in tricks if t[1] != t[3]][:5]

if interesting_tricks:
    for i, (forward_tokens, fwd_result, backward_tokens, bwd_result) in enumerate(interesting_tricks, 1):
        print(f"Trick #{i}:")
        print(f"  Forward:  {format_rpn(forward_tokens)}")
        print(f"  Result:   {fwd_result}")
        print()
        print(f"  Reversed: {format_rpn(backward_tokens)}")
        print(f"  Result:   {bwd_result}")
        print()
else:
    print("No magic tricks found this time! The cipher didn't align.")
    print("(Sometimes randomness doesn't cooperate!)")

print("=" * 60)
