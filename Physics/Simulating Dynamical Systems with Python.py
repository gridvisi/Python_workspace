'''
https://towardsdatascience.com/a-beginners-guide-to-simulating-dynamical-systems-with-python-a29bc27ad9b1
'''

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Input constants
m = 1 # mass (kg)
L = 1 # length (m)
b = 0 # damping value (kg/m^2-s)
g = 9.81 # gravity (m/s^2)
delta_t = 0.02 # time step size (seconds)
t_max = 10 # max sim time (seconds)
theta1_0 = np.pi/2 # initial angle (radians)
theta2_0 = 0 # initial angular velocity (rad/s)
theta_init = (theta1_0, theta2_0)
# Get timesteps
t = np.linspace(0, t_max, t_max/delta_t)