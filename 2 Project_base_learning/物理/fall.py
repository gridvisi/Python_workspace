__author__ = 'Administrator'
import math

g = 10.0 #gravity
epsilon = 0.01 #rate of increase of acceleration

#Initially, the ball is coming off a bounce with velocity that would take it to a height of 1 m in a stationary elevator.
initialState = {"vBall": math.sqrt(2 * g), "vElev": 0, "aElev":0} #vBall: ball velocity // vElev: elevator velocity // aElev: elevator acceleration

def update(state):
    # This function uses kinematics to calculate exactly how much time elapses between two consecutive bounces.
    # Then computes vBall, vElev and aElev immediately after the next bounce.
    #
    #Input: the state of the system as the ball is coming off a bounce with the elevator floor
    #Returns: the state immediately after the next bounce. Calling this function repeatedly moves the system forward in time.

    ###Add code HERE to compute the state of the ball immediately before the next bounce###

    beforeCollision = {"vBall": vBall_New, "vElev": vElev_New, "aElev": aElev_New} #state right before the collision with the floor
    afterCollision = bounce(beforeCollision) #apply the effect of the collision on vBall
    return afterCollision

def bounce(state):
    #This function applies the update rule to vBall during an instantaneous elastic collision with the floor.
    return {"vBall": (-state["vBall"] + 2 * state["vElev"]), "vElev": state["vElev"], "aElev": state["aElev"]}

def hmax(state):
    #This function computes the maximum height after a bounce. At tmax, the relative speed vBall-vElev = 0 and the ball reaches its max height.
    tmax = 1 / (epsilon) * (-(g + state["aElev"]) + math.sqrt((g + state["aElev"])**2 + 2 * epsilon * (state["vBall"] - state["vElev"])))

    #Returns the difference between the height of the ball and the elevator floor
    return state["vBall"] * tmax - 0.5 * (g + state["aElev"]) * tmax ** 2 - state["vElev"] * tmax - 1/6 * epsilon * tmax**3

def simulate(state):
    #This function updates the initial state until the acceleration exceeds g/2, then prints the max height of the previous bounce.
    while (state["aElev"] < 0.5 * g):
        prevState = state #Save the previous state of the system
        state = update(state) #Compute the state after the next bounce

    print("The max height is %f" % hmax(prevState))

simulate(initialState)