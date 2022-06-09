'''
In this Kata you need to write the method SharedBits that returns true if 2 integers share at least two '1' bits. For simplicity assume that all numbers are positive

For example int seven = 7; //0111 int ten = 10; //1010 int fifteen = 15; //1111 SharedBits(seven, ten); //false SharedBits(seven, fifteen); //true SharedBits(ten, fifteen); //true

seven and ten share only a single '1' (at index 3)
seven and fifteen share 3 bits (at indexes 1, 2, and 3)
ten and fifteen share 2 bits (at indexes 0 and 2)
Hint: you can do this with just string manipulation, but binary operators will make your life much easier.

FUNDAMENTALSBINARYBITS

https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python

'''
#6th solution by ericlee
def shared_bits(a, b):
    print(bin(a),bin(b))
    print([int(x)&int(y)==1 for x,y in zip(bin(a)[2:],bin(b)[2:])])
    return sum([int(x)&int(y)==1 for x,y in zip(bin(a)[2:][::-1],bin(b)[2:][::-1])]) >= 2

a,b  = 7, 10
print(shared_bits(a, b))

def shared_bits(a, b):
    return bin(a & b).count('1') > 1

def shared_bits(a, b):
    return len(bin(a&b).strip('0b0'))>1