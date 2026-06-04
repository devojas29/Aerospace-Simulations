# Stanford Aerospace Profile Builder - Project 3
# Simulating different launch angles using loops and math

import numpy as np
import matplotlib.pyplot as plt

print("--- ADVANCED ANGLED LAUNCH SIMULATOR ---")

# Setup our simulation environment
time = np.linspace(0, 15, 300) # 15 seconds flight, 300 steps
g = 9.81                        # Gravity (m/s^2)
v_initial = 150                 # Initial velocity leaving the pad (m/s)

# We want to test three different launch angles: 30°, 45°, and 60°
launch_angles = [30, 45, 60]

plt.figure(figsize=(10, 6))

# LOOPING through each angle to calculate and plot its specific flight path
for angle in launch_angles:
    # Python trigonometry functions require angles in Radians, not Degrees
    theta = np.radians(angle)
    
    # Calculus split: Separate the speed into X (horizontal) and Y (vertical) components
    v_x = v_initial * np.cos(theta)
    v_y = v_initial * np.sin(theta)
    
    # Calculate flight positions over time
    x_positions = v_x * time
    y_positions = (v_y * time) - (0.5 * g * (time**2))
    
    # Ensure the rocket stops when it hits the ground
    y_positions = np.clip(y_positions, 0, None)
    
    # Add this specific flight path to the map
    plt.plot(x_positions, y_positions, label=f'Launch Angle: {angle}°')

# Formatting the engineering chart
plt.title("Rocket Trajectory Variance by Launch Angle", fontsize=14, fontweight='bold')
plt.xlabel("Downrange Distance (meters)", fontsize=11)
plt.ylabel("Altitude (meters)", fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

print("Rendering comparison graph...")
plt.show()  