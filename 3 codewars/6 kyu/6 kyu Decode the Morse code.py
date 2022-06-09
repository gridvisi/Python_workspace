'''
https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

HEY JUDY = .... . -.-- / .--- ..- -. -.--
'''
#def decodeMorse(morse_code):


# dict of words2morse
dict1 = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-.', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
         'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# dict of morse2words
dict2 = dict(zip(dict1.values(), dict1.keys()))


def encode():
    words = input("Input a sentence you want to endoce, NO PUNCTUATION:").strip().lower()
    for letter in words:
        if letter == ' ':
            print('/', end=' ')
        else:
            print(dict1[letter], end=' ')
    print()


def decode():
    codes = input("Input Morse code you want to decode, ONLY MORSE CODE:").strip().split(" ")
    for sign in codes:
        if sign == '/':
            print(' ', end='')
        else:
            print(dict2[sign], end='')
    print()


def main():
    while 1 == 1:
        choice = input("0:Encode(Words to Morse codes) or 1:Decode(Morse codes to Words).Plase input [0/1]")

        if choice == '0':
            encode()
        elif choice == '1':
            decode()
        else:
            break

if __name__ == "__main__":
    main()

#print(decode())
print(encode())


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_alpha = dict(zip(alpha, morse))

        temp = set()
        for index in words:
            temp_morse = []
            for i in index:
                temp_morse.append(morse_alpha[i])

            s = ''.join(temp_morse)

            temp.add(s)

        return len(temp)

