#https://www.geeksforgeeks.org/g-fact-35-truncate-in-python/


# Python program to show output of floor(), ceil()
# truncate() for a positive number.
import math

print (math.floor(3.5)) # floor
print (math.trunc(3.5)) # work as floor
print (math.ceil(3.5))  # ceil

print(math.pi)
print (math.floor(math.pi)) # floor
print (math.trunc(math.pi)) # work as floor
print (math.ceil(math.pi))  # ceil

# Python program to show output of floor(), ceil()
# truncate() for a negative number.
import math
print (math.floor(-3.5)) # floor
print (math.trunc(-3.5)) # work as ceil
print (math.ceil(-3.5))  # ceil