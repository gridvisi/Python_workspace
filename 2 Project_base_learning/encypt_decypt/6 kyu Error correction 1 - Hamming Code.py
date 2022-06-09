'''
Translations appreciated

Background information
The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works. In this Kata we will implement the Hamming Code with bit length 3, this has some advantages and disadvantages:

✓ Compared to other versions of hamming code, we can correct more mistakes
✓ It's simple to implement
x The size of the input triples
Task 1: Encode function:
First of all we have to implement the encode function, which is pretty easy, just follow the steps below.

Steps:

convert every letter of our text to ASCII value
convert ASCII value to 8-bit binary string
replace every "0" with "000" and every "1" with "111"
Let's do an example:

We have to convert the string hey to hamming code sequence.

First convert it to ASCII values:
104 for h, 101 for e and 121 for y.


2. Now we convert the ASCII values to a 8-bit binary string:
104 -> 01101000, 101 -> 01100101 and 121 -> 01111001

if we concat the binaries we get 011010000110010101111001


3. Now we replace every "0" with "000" and every "1" with "111":
011010000110010101111001 -> 000111111000111000000000000111111000000111000111000111111111111000000111

That's it good job!

Task 2: Decode function:
Now we have to check if there happened any mistakes and correct them. Errors will only be a bit flip and not a loose of bits, so the length of the input string is always divisible by 3.

example:

111 --> 101 this can and will happen
111 --> 11 this won't happen
The length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

Steps:

Split the string of 0 and 1 in groups of three characters example: "000", "111"
Check if an error occurred: If no error occurred the group is "000" or "111", then replace "000" with "0" and "111" with 1 If an error occurred the group is for example "001" or "100" or "101" and so on... Replace this group with the character that occurs most often. example: "010" -> "0" , "110" -> "1"
Now take a group of 8 characters and convert that binary number to decimal ASCII value
Convert the ASCII value to a char and well done you made it :)
Look at this example carefully to understand it better:

We got a bit sequence:

100111111000111001000010000111111000000111001111000111110110111000010111

First we split the bit sequence into groups of three:

100, 111, 111, 000, 111, 001 ....

Every group with the most "0" becomes "0" and every group with the most "1" becomes "1":

100 -> 0 Because there are two 0 and only one 1

111 -> 1 Because there are zero 0 and three 1

111 -> 1 Because there are zero 0 and three 1

000 -> 0 Because there are three 0 and zero 1

111 -> 1 Because there are zero 0 and three 1

001 -> 0 Because there are two 0 and one 1

Now concat all 0 and 1 to get 011010000110010101111001

We split this string into groups of eight: 01101000, 01100101 and 01111001.

And now convert it back to letters:

01101000 is binary representation of 104, which is ASCII value of h

01100101 is binary representation of 101, which is ASCII value of e

01111001 is binary representation of 121, which is ASCII value of y

Now we got our word hey !
任务2：解码函数。
现在我们要检查是否发生了错误并加以纠正。错误只会是位的翻转而不是位的松动，所以输入字符串的长度总是被3所除。

例如

111 -->101 这可能也会发生
111 --> 11 这不会发生
输入字符串的长度也总是被24整除，这样你就可以将其转换为ASCII值。

步骤：将0和1的字符串分成三组。

把0和1的字符串分成三组，例如： "000", "111"
检查是否有错误发生。如果没有发生错误，这组是 "000 "或 "111"，那么就把 "000 "改为 "0"，把 "111 "改为 "1 "如果发生错误，这组是例如 "001 "或 "100 "或 "101"，以此类推。用最常出现的字符替换这组字符，例如："010"->"0"，"111"->"1"。"010" -> "0" , "110" -> "1"
现在取一组8个字符，并将二进制数转换为十进制ASCII值。
将ASCII值转换为一个char，你做得很好:)
仔细看这个例子，可以更好地理解它。

我们得到一个比特序列：

100111111000111001000010000111111000000111001111000111110110111000010111

首先我们将位序列分成三组。

100, 111, 111, 000, 111, 001 ....

每一组中 "0 "最多的变成 "0"，每一组中 "1 "最多的变成 "1"。

100 -> 0 因为有两个 "0 "而只有一个 "1

111 -> 1 因为有0个0和3个1。

111 -> 1 因为有0个0和3个1。

000 -> 0 因为有三个0和零1

111 -> 1 因为有0个0和3个1。

001 -> 0 因为有两个0和一个1。

现在把所有的0和1连起来，得到011010000110010101111001。

我们把这个字符串分成八组：01101000、01100101和01111001。

而现在将其转换回字母。

01101000是104的二进制表示，也就是h的ASCII值。

01100101是101的二进制表示，是e的ASCII值。

01111001是121的二进制表示，即y的ASCII值。

现在，我们得到了我们的字，哎！

通过www.DeepL.com/Translator（免费版）翻译
'''
#Steps:
#convert every letter of our text to ASCII value
#convert ASCII value to 8-bit binary string
#replace every "0" with "000" and every "1" with "111"
strng = 'hey'
#101001011101

#19th solution by ericlee
def encode(strng):
    # asc = ''.join([str(bin(ord(i))).replace('b','') for i in strng])
    asc = ''.join([str(bin(ord(i)))[2:].rjust(8, '0') for i in strng])
    #return asc
    return ''.join(['000' if i == '0' else '111' for i in asc])

print(encode(strng))

bits = "000111111000111000000000000111111000000111000111000111111111111000000111"
def decode(bits):
    #sl = [str(int(bits[i:i+3].count('1') > bits[i:i+3].count('0'))) for i in range(0,len(bits),3)]
    bit = [int(i) for i in bits]
    sl = [str(int(sum(bit[i:i+3])>1)) for i in range(0,len(bit),3)]
    print(sl)
    return ''.join([chr(int(''.join(sl)[i:i+8],2)) for i in range(0,len(sl),8)])
print(decode(bits))

print(int(True))

#1st solution
def encode(stg):
    return "".join(digit * 3 for char in stg for digit in f"{ord(char):08b}")


def decode(binary):
    reduced = (get_digit(triplet) for triplet in chunks(binary, 3))
    return "".join(get_char(byte) for byte in chunks("".join(reduced), 8))


def chunks(seq, size):
    return (seq[i:i + size] for i in range(0, len(seq), size))

def get_digit(triplet):
    return max(triplet, key=triplet.count)

def get_char(byte):
    return chr(int(byte, 2))

#18th solution
encode = lambda string: ''.join([i*3 for i in ''.join([str(bin(ord(i)))[2:].rjust(8, '0') for i in string])])
decode = lambda bits: ''.join([chr(int(''.join(['1' if i > 1 else '0' for i in [sum([int(j) for j in list(k)]) for k in [bits[i:i+3] for i in range(0, len(bits), 3)]]])[i:i+8], 2)) for i in range(0, len(''.join(['1' if i > 1 else '0' for i in [sum([int(j) for j in list(k)]) for k in [bits[i:i+3] for i in range(0, len(bits), 3)]]])), 8)])