# Title: Knuth-Morris-Pratt String Matching Algorithm

# The KMP algorithm finds a pattern in text efficiently by using a "failure function"
# to skip unnecessary comparisons. Watch as it builds the failure table and then
# searches through text, showing exactly where pattern matches occur and how many
# comparisons it takes compared to naive search.

def build_failure_table(pattern):
    """Build the KMP failure function that shows how far to backtrack."""
    m = len(pattern)
    table = [0] * m
    j = 0
    
    print(f"Building failure table for pattern: '{pattern}'")
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
        print(f"  Position {i} ('{pattern[i]}'): table[{i}] = {j}")
    
    print(f"Failure table: {table}\n")
    return table

def kmp_search(text, pattern):
    """Search for pattern in text using KMP algorithm."""
    failure_table = build_failure_table(pattern)
    n, m = len(text), len(pattern)
    matches = []
    comparisons = 0
    j = 0
    
    print(f"Searching for '{pattern}' in '{text}'")
    for i in range(n):
        comparisons += 1
        while j > 0 and text[i] != pattern[j]:
            print(f"  Mismatch at text[{i}]='{text[i]}' vs pattern[{j}]='{pattern[j]}', backtrack to {failure_table[j-1]}")
            j = failure_table[j - 1]
            comparisons += 1
        
        if text[i] == pattern[j]:
            print(f"  Match: text[{i}]='{text[i]}' == pattern[{j}]='{pattern[j]}'")
            j += 1
        
        if j == m:
            matches.append(i - m + 1)
            print(f"  ✓ Pattern found at position {i - m + 1}!")
            j = failure_table[j - 1]
    
    return matches, comparisons

# Demo with an interesting case
text = "ababcabababcabab"
pattern = "ababcabab"

print("=" * 50)
print("KMP STRING MATCHING ALGORITHM")
print("=" * 50 + "\n")

matches, comps = kmp_search(text, pattern)

print(f"\n{'=' * 50}")
print(f"Results:")
print(f"  Pattern: '{pattern}'")
print(f"  Text: '{text}'")
print(f"  Matches found at positions: {matches}")
print(f"  Total comparisons: {comps}")
print(f"{'=' * 50}")
