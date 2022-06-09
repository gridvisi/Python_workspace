'''
https://www.codewars.com/kata/binaries/train/python
code("77338855") --> "001111001111011101110001100000011000001101001101"
code("77338")  --> "0011110011110111011100011000"
code("0011121314") --> "1010111111011011011111001100"

decode("001111001111011101110001100000011000001101001101") -> "77338855"
decode("0011110011110111011100011000") -> "77338"
decode("1010111111011011011111001100") -> "0011121314"

code("77338")  --> "001，111，001，111，01，11，01，11，0001，1000"
001 stand for following binaries is 3 digit， so 0001 stand for 4 digit
'''

strng = "77338855"
#strng = "77338"
def code(strng):
    for i in strng:
        x = [(len(bin(int(i)))-3)*'0' + '1' + str(bin(int(i)))[2:] for i in strng]
    return ''.join(x)
#code("77338855") --> "001111001111011101110001100000011000001101001101"
#code("77338")  --> "0011110011110111011100011000"
print(code(strng))

strng = code(strng)
print(int(0b111),int('1010',2),int('0b1010',2))
def decode(strng):
    i,j,res = 0,0,''
    while j+1+j-i+1 <= len(strng):
        while strng[j] != '1':
            j += 1

        res += str(int((strng[j+1:j+1+j-i+1]),2))
        i,j = j+1+j-i+1,j+1+j-i+1
    return res

print(decode(strng))
'''
001 111 0001 0101
 3bit    4bit
Decode = '.join(f'{"0" * (d.bit_length() - 1)}1{d:b}' for d in map(int, s))
'''
s = '00111100010101'
s = '139'
print("www:",''.join(f'{"0" * (d.bit_length() - 1)}1{d:b}'for d in map(int, s)))


def code(s):
    return ''.join(f'{"0" * (d.bit_length() - 1)}1{d:b}' for d in map(int, s))
print('cap',code('2020'))

def decode(s):
    it, n, out = iter(s), 1, []
    for c in it:
        if c == '0':
            n += 1
        else:
            out.append(int(''.join(next(it) for _ in range(n)), 2))
            n = 1
    return ''.join(map(str, out))

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])