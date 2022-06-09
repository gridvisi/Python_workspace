# https://www.codewars.com/kata/594c6ad5d909ca19e200002f/train/python
'''

A byte is a sequence of 8 bits. One could imagine
implementing a small set data structure using a single byte. The set would hold at most the elements 0 through 7. The value of each bit in the byte would indicate whether the index of that bit was included in the set.

Consider the following byte, where the index of each bit
is marked below.

Byte: 0 1 1 0 0 1 0 1

Index: 0 1 2 3 4 5 6 7

This byte would represent the set {1, 2, 5, 7}. Similarly,


10101010 ==> {0, 2, 4, 6}

11100000 ==> {0, 1, 2}

Your task is to write a function byte_to_set which takes a
single byte (an integer 0-255), and returns the
corresponding set.
'''

def byte_to_set(byte):
    s = (8 - len(bin(byte)[2:]))*'0' + bin(byte)[2:]
    return {i for i,e in enumerate(s) if e=='1'}

def byte_to_set(byte):
    return [i for i,e in enumerate(bin(byte)[2:]) if e=='1']


def byte_to_set(byte):
  return { i for i in range(8) if (byte & (128 >> i))}

def byte_to_set(byte):
  return {i for i in range(8) if "{0:08b}".format(byte)[i] == "1"}