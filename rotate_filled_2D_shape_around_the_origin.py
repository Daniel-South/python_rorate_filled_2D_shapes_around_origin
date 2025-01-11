"""
FILE:   rotate_filled_2D_shape_around_the_origin.py
TITLE:  Rotate A Filled Shape Around The Origin
AUTHOR: Daniel R. South
DATE:   11 Jan 2025

DESCRIPTION:

Use matplotlib to display a filled 2D shape with one corner at the origin (0,0)
Use matrix multiplication to rotate the shape around the origin
"""

import numpy as np
import matplotlib.pyplot as plt


# Create a 2x2 square with one corner at the origin (0,0)
# The shape is defined by a list of (x,y) points to set the corners
# (0,0), (2,0), (2,2), (0,2), (0,0)
x_values = np.array([0,2,2,0,0])
y_values = np.array([0,0,2,2,0])

print(x_values)
print(y_values)

fig1, axs1 = plt.subplots(1, 1, figsize=(3,3))
axs1.set_title("Original Shape")
axs1.set_aspect('equal')

# Plot the original unrotated shape
axs1.fill(x_values, y_values)
plt.show()

fig2, axs2 = plt.subplots(1, 1, figsize=(8,8))

axs2.set_aspect('equal')

def add_shape_at_degrees(in_degrees, in_clockwise=True):
    coef1 = 1
    coef2 = -1
    if in_clockwise == False:
        coef1 = -1
        coef2 = 1
        
    theta = np.radians(in_degrees)
    print(f"degrees = {in_degrees}, clockwise={in_clockwise}, radians = {round(theta,4)}")
    
    rotation_matrix = np.array([
        [np.sin(theta), coef1 * np.cos(theta)],
        [np.cos(theta), coef2 * np.sin(theta)]])

    #print(rotation_matrix)
    
    # Rotate by vector multiplication

    xy_rotated = np.dot(rotation_matrix, np.vstack([x_values, y_values]))

    x_vals_rotated = xy_rotated[0, :]
    y_vals_rotated = xy_rotated[1, :]

    print("Rotated x values:", list(map(lambda a: round(a,4), x_vals_rotated)))
    print("Rotated y values:", list(map(lambda a: round(a,4), y_vals_rotated)))

    axs2.fill(x_vals_rotated, y_vals_rotated)



axs2.set_title("Orig Shape: Outline; Rotated Shapes: Solids")

# Add the unrotated shape as an outline
axs2.plot(x_values, y_values)

# Add the rotated shapes as solids
add_shape_at_degrees(30)
add_shape_at_degrees(60)
add_shape_at_degrees(120)
add_shape_at_degrees(45, False)

# Display the combined graph

plt.show()
