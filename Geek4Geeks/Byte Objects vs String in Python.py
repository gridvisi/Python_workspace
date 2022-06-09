# Python code to demonstrate String encoding
# https://www.geeksforgeeks.org/byte-objects-vs-string-python/

# initialising a String
a = 'GeeksforGeeks'

# initialising a byte object
c = b'GeeksforGeeks'
print(a,c)

# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d = a.encode('ASCII')

# checking if a is converted to bytes or not
if (d == c):
    print("Encoding successful")
else:
    print("Encoding Unsuccessful")