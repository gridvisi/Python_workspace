'''
https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

A child is playing with a ball on the nth floor of a tall building. The height of this floor,
h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its
height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window
(including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Example:
- h = 3, bounce = 0.66, window = 1.5, result is 3
- h = 3, bounce = 1, window = 1.5, result is -1
(Condition 2) not fulfilled).

@test.describe('Tests')
def fixed_tests():
    def testing(h, bounce, window, exp):
        actual = bouncing_ball(h, bounce, window)
        Test.assert_equals(actual, exp)

    @test.it('Fixed Tests')
    def tests():
        testing(2, 0.5, 1, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)
'''

def bouncing_ball(h, bounce, window):
    if h < 0 or abs(bounce) >= 1 or window >= h:return -1
    seen = 0
    while h > window:
        seen += 1
        h *= bounce
        if h > window:
            seen += 1
    return seen
h, bounce, window = 30, 0.66, 1.5 # 15
print(bouncing_ball(h, bounce, window))

#1st
def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1

#2nd
def bouncingBall(h, bounce, window):
    seen = -1
    if 0 < bounce < 1:
        while h > window > 0:
            seen += 2
            h *= bounce
    return seen

