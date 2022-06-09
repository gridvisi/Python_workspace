'''
https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
'''

def str_count(strng, letter):
    return strng.count(letter)

#2nd
strCount = str.count

#3rd
def str_count(strng, letter):
    counter = 0

    for chr in strng:
        if chr == letter:
            counter += 1

    return counter