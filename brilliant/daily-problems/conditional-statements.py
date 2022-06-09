'''
https://brilliant.org/daily-problems/conditional-statements/


'''

red, green, blue = 0, 0, 0
for i in range(-10,11):
    if i > 6 - i*i:
        if i*i < 3 - 2*i:
            red += 1
        else:
            green += 1
    else:
        blue += 1
print(red,green,blue)

#Output:0 15 6


#2nd

red = 0
green = 0
blue = 0
for x in range( -10, 11 ):
    if ( x > ( 6 - x*x ) ):
        if ( x*x < ( 3 - 2*x ) ):
            print( x, "\tRED" )
            red += 1
        else:
            print( x, "\tGREEN" )
            green += 1
    else:
        print( x, "\tBLUE" )
        blue += 1

print( "red:", red, ", green:", green, ", blue:", blue )

#3rd
print(sum((1 for x in range(-10,11) if x > 6-x**2 and x**2 < 3-2*x)))
#0


#4th
def the_program(x):
    if x > 6 - x**2:
        if x**2 < 2 - 2*x:
            print("RED")
        else:
            print("GREEN")
    else:
        print("BLUE")

for x in range(-10, 11):
    the_program(x)

