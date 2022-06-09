
import string
print(string.ascii_letters)

print(chr(int('0b11111111',2)))
s = string.ascii_letters
word = string.ascii_letters + '.,!:'
ls = [(ord(i)) for i in word]
scope = max(ls),min(ls)
print(scope)

def bin_encode(word):
    st = [bin(ord(i)) for i in word]
    print([bin(ord(i)) for i in word])
    ver_bit = bin(sum([ord(i) for i in word])%2)
    check_end = bin(255)  #'11111111'

    return ''.join(st) + f'{check_end}' + f'{int(check_end,2)}'
word = ' Aazabc.,!:python ZZZ PYTHON'
word = 'I love python!'
#word = string.ascii_letters + '.,!:'
print(bin_encode(word))
scope = min([ord(i) for i in word]),max([ord(i) for i in word])
print(scope,bin(scope[1]))

#校验位最后两位，0的个数

text = bin_encode(word)

#text = '0b10010010b1000000b11011000b11011110b11101100b11001010b1000000b11100000b11110010b11101000b11010000b11011110b11011100b1011100b1'
def bin_decode(text):
    st = [chr(int('0b'+str(i),2)) for i in text[2:-3].split('0b')]
    veri_bit = text[-3:]
    check_veri = bin(sum([ord(i) for i in st])%2)
    return ''.join(st),veri_bit==check_veri,veri_bit,check_veri
#print(bin_decode(text))

def bin_decode(text):
    check_end = [[i,i+10] for i in range(0,len(text),10) if text[i:i+10] == bin(255)]
    print(check_end)
    st = [chr(int('0b'+str(i),2)) for i in text[2:-3].split('0b')]
    return ''.join(st),check_end
print(bin_decode(text))