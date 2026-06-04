# Stanford Aerospace Profile Builder - Project 1
# Using numerical differentiation to find a rocket's velocity

# Let's simulate a rocket's altitude (in meters) at 4 different seconds.
# Time (seconds)
t0, t1, t2, t3 = 0, 1, 2, 3

# Altitude (meters) - Notice the rocket is speeding up!
alt0 = 0
alt1 = 15
alt2 = 60
alt3 = 135

print("--- ROCKET FLIGHT DATA ANALYSIS ---")

# --- CALCULUS IN ACTION: DIFFERENTIATION ---
# Velocity is the change in altitude divided by the change in time: (alt_new - alt_old) / (t_new - t_old)

# 1. Velocity between second 0 and 1
velocity_1 = (alt1 - alt0) / (t1 - t0)
print(f"Velocity from 0s to 1s: {velocity_1} meters/second")

# 2. Velocity between second 1 and 2
velocity_2 = (alt2 - alt1) / (t2 - t1)
print(f"Velocity from 1s to 2s: {velocity_2} meters/second")

# 3. Velocity between second 2 and 3
velocity_3 = (alt3 - alt2) / (t3 - t2)
print(f"Velocity from 2s to 3s: {velocity_3} meters/second")


# --- STEPPING IT UP: ACCELERATION ---
# Acceleration is the derivative of velocity (change in velocity / change in time)

accel_1 = (velocity_2 - velocity_1) / (t2 - t1)
accel_2 = (velocity_3 - velocity_2) / (t3 - t2)

print("\n--- ACCELERATION ANALYSIS ---")
print(f"Rocket Acceleration rate 1: {accel_1} m/s^2")
print(f"Rocket Acceleration rate 2: {accel_2} m/s^2")

if accel_2 > accel_1:
    print("\nResult: The rocket engines are producing positive net thrust!")
