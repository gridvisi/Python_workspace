__author__ = 'Administrator'
import math
sim_dt = 0.0001      # step size for simulation
x = 1.00  #
y = 0.0000  # initial position
vx = 0
vy = 0.0000 # initial velocity
g = 10.000 #  acceleration due to gravity

m = 1.00  # mass of object
k = 10.00  # spring constant
L0 = 1.00  # neutral length of spring
t = 0.0000 # start the timer

while x > 0:
    new_t = t + sim_dt    #Calculate distance to origin
    r = math.sqrt(x*x + y*y)
    L = r - L0

    # Calculate forces
    Fspr = -k*L
    Fg = m*g
    Fx = Fspr * x/r
    Fy = Fspr * y/r + Fg

    #Calculate acceleration
    ax = Fx/m
    ay = Fy/m

    #Simple numerical integration
    dt = new_t - t
    new_vx = vx + ax*dt
    new_vy = vy + ay*dt
    new_x = x + (vx+new_vx)/2 * dt
    new_y = y + (vy+new_vy)/2 * dt

    # Get ready for the next step
    x = new_x; y = new_y
    vx = new_vx; vy = new_vy
    t = new_t
print(y)

