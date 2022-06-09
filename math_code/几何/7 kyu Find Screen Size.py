'''
https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/python

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(find_screen_height(1024, "4:3"), "1024x768")
    test.assert_equals(find_screen_height(1280, "16:9"), "1280x720")
    test.assert_equals(find_screen_height(3840, "32:9"), "3840x1080")
'''

#21st by ericlee
def find_screen_height(width, ratio):
    w,h = width,width * eval(ratio.split(':')[1])/eval(ratio.split(':')[0])
    return f"{w}*{h}"

#1st solution
def find_screen_height(width, ratio):
    a, b = map(int, ratio.split(":"))
    return f"{width}x{int(width / a * b)}"

def find_screen_height(width, ratio):
    return f'{width}x{width * int(ratio.split(":")[1]) // int(ratio.split(":")[0])}'

def find_screen_height(width, ratio):
    a, b = map(int, ratio.split(':'))
    return f'{width}x{width * b // a}'

