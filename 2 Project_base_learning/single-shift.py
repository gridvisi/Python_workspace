alphabet = "abcdefghijklmnopqrstuvwxyz"

def letter_to_number(l):
	return alphabet.find(l)  # index in the alphabet

def number_to_letter(i):
	return alphabet[i%26]    # %26 does the wrap-around

def caesar_shift_single_character(l, amount):
	i = letter_to_number(l)
	if i == -1: # character not found in alphabet
		return ""         # remove it, it's space or punctuation
	else:
		return number_to_letter(i + amount)  # Caesar shift

l,amount = 'china',17
for x in l[::]:
    print(caesar_shift_single_character(x,amount),end="")
print("")
print(letter_to_number('s'))
print(letter_to_number('c'))
