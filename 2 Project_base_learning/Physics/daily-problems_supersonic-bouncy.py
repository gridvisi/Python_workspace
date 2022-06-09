#https://brilliant.org/daily-problems/supersonic-bouncy/

def number_of_balls(v_0, v_max):
    """
    Calculates the numbers of balls required to achieve v_max
    """
    res_v = 2*v_0+v_0
    num_balls = 2
    while res_v < v_max:
        res_v = 2*res_v+v_0
        num_balls += 1
    return num_balls


V_MAX = 343
FIRTS_BALL_SPEED = 1


print("The minimum number of balls required to exceed the speed"
      " {}km/h is {}. ".format(V_MAX, number_of_balls(FIRTS_BALL_SPEED, V_MAX)))