
for letter in 'Django':
    if letter == 'D':
        continue
    print("Current Letter: " + letter)


# Case 2nd
'''
103

I like to use continue in loops where there are a lot of contitions to be fulfilled before you get "down to business". So instead of code like this:

for x, y in zip(a, b):
    if x > y:
        z = calculate_z(x, y)
        if y - z < x:
            y = min(y, z)
            if x ** 2 - y ** 2 > 0:
                lots()
                of()
                code()
                here()
I get code like this:

for x, y in zip(a, b):
    if x <= y:
        continue
    z = calculate_z(x, y)
    if y - z >= x:
        continue
    y = min(y, z)
    if x ** 2 - y ** 2 <= 0:
        continue
    lots()
    of()
    code()
    here()
    
By doing it this way I avoid very deeply nested code. Also, it is easy to optimize the 
loop by eliminating the most frequently occurring cases first, so that I only have to 
deal with the infrequent but important cases (e.g. divisor is 0) when there is no other 
showstopper.
'''

import random
for i in range(20):
    x = random.randint(-5,5)
    if x == 0: continue
    print(1/x)


#Case 3rd
def filter_out_colors(elements):
  colors = ['red', 'green']
  result = []
  for element in elements:
    if element in colors:
       continue # skip the element
    # You can do whatever here
    result.append(element)
  return result

print(filter_out_colors(['lemon', 'orange', 'red', 'pear']))
 # ['lemon', 'orange', 'pear']


#Case 4th

# List of times at which git commits were done.
# Formatted in hour, minutes in tuples.
# Note the last one has some fantasy.
commit_times = [(8,20), (9,30), (11, 45), (15, 50), (17, 45), (27, 132)]

for time in commit_times:
    hour = time[0]
    minutes = time[1]

    # If the hour is not between 0 and 24
    # and the minutes not between 0 and 59 then we know something is wrong.
    # Then we don't want to use this value,
    # we skip directly to the next iteration in the loop.
    if not (0 <= hour <= 24 and 0 <= minutes <= 59):
        continue

    # From here you know the time format in the tuples is reliable.
    # Apply some logic based on time.
    print("Someone commited at {h}:{m}".format(h=hour, m=minutes))