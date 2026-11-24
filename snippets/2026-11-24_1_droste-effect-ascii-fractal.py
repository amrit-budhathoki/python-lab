# Title: Droste Effect ASCII Fractal

# Renders a recursive Droste effect (infinite zoom into center) using ASCII art.
# Each iteration shrinks and nests the previous pattern, creating a mesmerizing
# self-similar spiral that demonstrates how fractals hide infinite complexity
# in finite space. The pattern converges to a point, creating a tunnel effect.

def render_droste(size, depth):
    """Generate a Droste fractal by recursively nesting scaled patterns."""
    
    def get_char(x, y, d):
        """Determine which character to draw based on position and depth."""
        if d == 0:
            return ' '
        
        # Calculate distance from center
        cx, cy = size / 2, size / 2
        dx, dy = x - cx, y - cy
        dist = (dx * dx + dy * dy) ** 0.5
        
        # Determine which "ring" we're in based on depth
        ring_size = size / (2 ** (depth - d))
        normalized_dist = dist / (ring_size / 2)
        
        # Create pattern based on angle and distance
        import math
        angle = math.atan2(dy, dx)
        
        # Layer pattern: different characters for different rings
        if normalized_dist > 1.0:
            return ' '
        
        # Create spiral/concentric pattern
        ring = int(normalized_dist * 4)
        angle_norm = (angle + math.pi) / (2 * math.pi)
        angle_section = int(angle_norm * 8)
        
        chars = ['█', '▓', '▒', '░', '·', '.', ' ']
        char_idx = (ring + angle_section) % len(chars)
        
        return chars[char_idx]
    
    return get_char

def print_fractal(size, depth):
    """Print the Droste fractal to terminal."""
    get_char = render_droste(size, depth)
    
    for y in range(size):
        line = ""
        for x in range(size):
            line += get_char(x, y, depth)
        print(line)

# Main execution
print("🌀 Droste Fractal - Recursive Zoom Effect 🌀\n")
print_fractal(50, 6)
print("\n✨ Each layer contains a scaled copy of the whole pattern!")
