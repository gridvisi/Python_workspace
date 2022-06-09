'''
https://www.codewars.com/kata/5a036ecb2b651d696f00007c/train/python

The aim of this kata is to write function drawACross / draw_a_cross which returns a cross shape with 'x' characters on a square grid of size and height of our sole input n. All non-'x' characters in the grid should be filled with a space character (" ").

For example for drawACross(7) / draw_a_cross(7), the function should draw the following grid:

x     x
 x   x
  x x
   x
  x x
 x   x
x     x
The arms of the cross must only intersect through one central 'x' character, and start in the
corner of the grid, so for even values of n, return "Centered cross not possible!"
'''
print(len('x     x'))
def draw_a_cross(n):
    return "".join([f"{' '*i}{'*'}{' '*(n-2*i-2)}{'*'}{' '*i}\n" for i in range(n)])
n = 7
print(draw_a_cross(n))


#7th solve by ericlee
def draw_a_cross(n):
    ans = ''
    if n%2==0 and n>3:
        return 'Centered cross not possible!'
    elif n <= 3:
        return 'Not possible to draw cross for grids less than 3x3!'
    else:
        for i in range(n):
            start = [" "] * n
            start[i],start[n-i-1] = "x","x"
            ans += ''.join(start) +"\n"
        return ans[:-1]
n = 7
print(draw_a_cross(n))

'x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x\n'
'x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x'


#1st
def draw_a_cross(n: int) -> str:
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"

    if n % 2 == 0:
        return "Centered cross not possible!"

    lines = [('x' + ' ' * i + 'x').center(n) for i in range(n - 2, 0, -2)]
    return '\n'.join(lines + ['x'.center(n)] + lines[::-1])

#3rd
def draw_a_cross(n):
    if n<3:     return "Not possible to draw cross for grids less than 3x3!"
    if not n%2: return "Centered cross not possible!"
    half = [ f'x{ " "*(n-2*i-2) }x'.center(n) for i in range(n//2)]
    return "\n".join([*half, 'x'.center(n), *reversed(half) ])

