import math
from turtle import *

def hearta(k):
    """Calculates the x-coordinate for the heart shape."""
    return 15 * math.sin(k)**3

def heartb(k):
    """Calculates the y-coordinate for the heart shape."""
    return 12 * math.cos(k) - 5 * \
            math.cos(2 * k) - 2 * \
            math.cos(3 * k) - \
            math.cos(4 * k)

# --- Configuration for Slimmer Display (remains the same) ---
# Natural width of the heart (based on hearta): 30 units (from -15 to 15)
# Natural height of the heart (based on heartb): approx. 19.7 units (from -13.5 to 6.2)

# Target aspect ratio: Width / Height = 9 / 14
# We derived: x_scale / y_scale = (9 / 14) * (19.7 / 30) = 177.3 / 420
# Let y_scale = 20 (original y-scale).
# Then x_scale = (177.3 / 420) * 20 = 177.3 / 21
x_scale_factor = 177.3 / 21  # Approximately 8.44
y_scale_factor = 20

# --- Turtle Setup ---
bgcolor("black")  # Set background color to black
pencolor("#f73487") # Set drawing color to a shade of pink/red once

# Set drawing speed. 0 is the fastest animation speed, or you can use "fastest".
# The original code used 1000, which is effectively the same as 0 or "fastest".
speed(0)
# tracer(0) and update() are removed to allow step-by-step drawing.

# --- Draw the Heart ---
# The initial position of the turtle is (0,0).
# The first goto will draw a line from (0,0) to the first point.
# Subsequent points will draw from (0,0) to the current point,
# then from the current point back to (0,0), creating the 'filled' effect.
for i in range(6000):
    # Calculate the scaled coordinates for the current point on the heart's perimeter
    x_coord = hearta(i) * x_scale_factor
    y_coord = heartb(i) * y_scale_factor

    # Draw a line from the current pen position (which will be 0,0 for most iterations)
    # to the new point on the heart's perimeter.
    goto(x_coord, y_coord)

    # Draw a line from the current point on the perimeter back to the origin (0,0).
    # This creates the "filled" look by drawing many radial lines.
    goto(0, 0)

done() # Keep the window open until manually closed