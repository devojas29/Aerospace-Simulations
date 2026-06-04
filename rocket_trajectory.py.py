# Stanford Aerospace Profile Builder - Project 2
# Plotting a 2D Rocket Trajectory using NumPy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

print("--- GENERATING 2D ROCKET TRAJECTORY SIMULATION ---")

# 1. GENERATING THE DATA WORKSPACE (NumPy)
# We simulate flight time from 0 to 50 seconds, generating 500 precise data steps.
time = np.linspace(0, 50, 500)

# X-axis: Downrange distance (assuming a constant horizontal speed of 120 m/s)
downrange_distance = 120 * time

# Y-axis: Altitude curve (using a quadratic equation to simulate engine acceleration and gravity)
# Equation: Altitude = (Initial_Velocity * t) + (0.5 * Acceleration * t^2) - Gravity_Pull
altitude = (40 * time) + (0.5 * 8 * (time**2)) - (0.5 * 9.8 * (time**2))

# Ensure the rocket doesn't go below ground level (0 meters)
altitude = np.clip(altitude, 0, None)

# 2. CREATING THE VISUAL GRAPH (Matplotlib)
plt.figure(figsize=(10, 6))  # Dimensions of the window

# Plotting the coordinates
plt.plot(downrange_distance, altitude, color='red', linewidth=2.5, label='Rocket Path')

# Adding Academic / Engineering Labels
plt.title("Simulated 2D Rocket Trajectory Profile", fontsize=14, fontweight='bold')
plt.xlabel("Downrange Distance from Launchpad (meters)", fontsize=11)
plt.ylabel("Flight Altitude (meters)", fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)  # Standard engineering background grid
plt.legend()

# 3. DISPLAY THE COMPLETED PLOT
print("Displaying trajectory graph window...")
plt.show()
