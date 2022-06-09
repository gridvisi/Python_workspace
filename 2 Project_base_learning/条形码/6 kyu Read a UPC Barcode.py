'''
https://www.codewars.com/kata/5b7dfd8cbfae24e5f200004d/train/python


test.describe('should convert barcode to digits')

test.it("Campbell's Chicken Noodle Soup")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'), '0 51000 01251 7')

test.it("Hershey's Natural Unsweetened Cocoa")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍ ▍'), '0 34000 05200 4')

test.it("Bob's Red Mill Corn Grits")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍   ▍ ▍▍   ▍ ▍▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍ ▍▍  ▍ ▍'), '0 39978 00125 2')

test.it("Dutch Gold Pure Buckwheat Honey ")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍▍▍▍ ▍  ▍▍  ▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍ ▍▍▍  ▍▍  ▍▍ ▍▍▍  ▍ ▍   ▍  ▍ ▍'), '0 73138 20410 7')

test.it("Black Bear Spicy Brown Mustard")
test.assert_equals(read_barcode('▍ ▍ ▍ ▍▍▍▍ ▍▍▍▍ ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍ ▍ ▍▍▍ ▍  ▍▍  ▍▍ ▍ ▍▍▍  ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍    ▍ ▍'), '6 30003 91455 6')

test.it("Barilla Fideo Cut Spaghetti Pasta")
test.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍▍▍ ▍▍ ▍▍▍   ▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍   ▍  ▍    ▍ ▍    ▍ ▍ ▍'), '0 76808 00073 3')

'''

barcode = '▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'
barcode = '▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍ ▍' #'0 34000 05200 4'

print([int(not(int(i))) for i in '0001101'])
print(bin(int('0b'+'1'*len('0001101'),2) - int('0b'+'0001101',2)))

def read_barcode(barcode):
    l_dict = {'0001101':'0',
              '0011001':'1',
              '0010011':'2',
              '0111101':'3',
              '0100011':'4',
              '0110001':'5',
              '0101111':'6',
              '0111011':'7',
              '0110111':'8',
              '0001011':'9',
              }

    def flip(x):
        return bin(int('0b'+'1'*len(x),2) - int('0b'+x,2))[2:]
    r_dict = dict(zip([flip(k) for k,v in l_dict.items()],[v for k,v in l_dict.items()]))

    print(r_dict)
    re = ['1' if i == '▍' else '0' for i in barcode]
    print(''.join(re),len(re))
    head,tail = ''.join(re[0:3]),''.join(re[-3:])
    left = [l_dict[''.join(x)] for x in [re[i:i+7] for i in range(3,45,7)]]
    right = [r_dict[''.join(x)] for x in [re[i:i+7] for i in range(50,92,7)]]
    res = [e+' ' if i in (0,5,10) else e for i,e in enumerate(left + right)]
    res = '{} {}{}{}{}{} {}{}{}{}{} {}'.format(*left, *right)
    return '{} {}{}{}{}{} {}{}{}{}{} {}'.format(*left, *right)

#+ ''.join(right_bin)+ '0' #''.join(re[:3]) + f'{left}'+f'{right}'+''.join(re[-3:])
print(read_barcode(barcode))

#Top 1st
def read_barcode(barcode):
    binary = f"{barcode[3:45]}{barcode[50:92]}".replace("▍", "1").replace(" ", "0")
    digits = "".join(str([LEFT_HAND, RIGHT_HAND][i > 35][binary[i:i+7]]) for i in range(0, 78, 7))
    return f"{digits[0]} {digits[1:6]} {digits[6:11]} {digits[11]}"

#Top 2nd
tbl = str.maketrans('▍ ', '10')
def read_barcode(barcode):
    txt = barcode.translate(tbl)
    l = (LEFT_HAND[''.join(xs)] for xs in zip(*[iter(txt[3:7*6+3])]*7))
    r = (RIGHT_HAND[''.join(xs)] for xs in zip(*[iter(txt[-7*6-3:-3])]*7))
    return '{} {}{}{}{}{} {}{}{}{}{} {}'.format(*l, *r)

#Top 3rd
def read_barcode(bcode):
    bcode = [['0', '1'][e == '▍'] for e in bcode]
    return ' '.join(scan(bcode[::x], [None, LEFT_HAND, RIGHT_HAND][x], x) for x in [1, -1])

def scan(code, dic, side):
    ret = [str(dic["".join(code[i:i + 7][::side])]) for i in range(3, 45, 7)]
    return f'{ret[0]} {"".join(ret[1:])}'[::side]

'''

    res = f'{head}'+''.join([str(i) for i in left])+''.join([str(i) for i in right])+f'{tail}'

Time: 832ms Passed: 0 Failed: 6 Exit Code: 1
Test Results:
 should convert barcode to digits
 Campbell's Chicken Noodle Soup
'101 000110101100010011001000110100011010001101010101110010110011011011001001110110011010 101' should equal '0 51000 01251 7'
 Hershey's Natural Unsweetened Cocoa
'101 000110101111010100011000110100011010001101010101110010100111011011001110010111001010 101' should equal '0 34000 05200 4'
 Bob's Red Mill Corn Grits
'101 000110101111010001011000101101110110110111010101110010111001011001101101100100111011 101' should equal '0 39978 00125 2'
 Dutch Gold Pure Buckwheat Honey 
'101 000110101110110111101001100101111010110111010101101100111001010111001100110111001010 101' should equal '0 73138 20410 7'
 Black Bear Spicy Brown Mustard
'101 010111101111010001101000110100011010111101010101110100110011010111001001110100111010 101' should equal '6 30003 91455 6'
 Barilla Fideo Cut Spaghetti Pasta
'101 000110101110110101111011011100011010110111010101110010111001011100101000100100001010 101' should equal '0 76808 00073 3'

'''