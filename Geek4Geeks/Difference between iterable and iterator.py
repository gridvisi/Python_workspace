'''
https://www.geeksforgeeks.org/python-difference-iterable-iterator/
'''

for city in ["Berlin", "Vienna", "Zurich"]:
    print(city)

print("\n")

for city in ("Python", "Perl", "Ruby"):
    print(city)

print("\n")

for char in "Iteration is easy":
    print(char, end=" ")

#Code #2 : Function ‘iterable’ will return True,
# if the object ‘obj’ is an iterable and False otherwise.
# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


#Code #3 : Check object is iterable or not
# Function to check object
# is iterable or not
def iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


# Driver Code
for element in [34, [4, 5], (4, 5),
                {"a": 4}, "dfsdf", 4.5]:
    print(element, " is iterable : ", iterable(element))

