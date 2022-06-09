__author__ = 'Administrator'
'''
for i in range(10000):
    for j in range(10000):
        if i*i+1 == j*j*j-1:
            print(i,j)

i=1
j=1
for i in range (100,100000000):
    if pow(i*i+2, 1/3) == int(pow(i*i+2, 1/3)):
        print(i)
'''


encoding = {'C' : '1', 'G' : '0', 'A' : '00', 'T': '01'}
encoding = {'C' : '1', 'G' : '10', 'A' : '110', 'T': '111'}
def encode(sequence):
    #Create an empty string for the encoding of the sequence
    encoded_string = ""

    #For each letter, append its encoding to the encoded string
    for letter in range(len(sequence)):
        encoded_string += encoding[sequence[letter]]
    return encoded_string

print('CCGT:'+ encode('CCGT'))
print('CCAC:'+ encode('CCAC'))




