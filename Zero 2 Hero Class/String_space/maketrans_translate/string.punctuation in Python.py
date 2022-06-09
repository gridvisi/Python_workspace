# https://www.geeksforgeeks.org/string-punctuation-in-python/

#code_1
# import string library function
import string

# Storing the sets of punctuation in variable result
result = string.punctuation

# Printing the punctuation values
print(result)

#code_2
# import string library function
import string

# An input string.
Sentence = "Hey, Geeks !, How are you?"

for i in Sentence:

    # checking whether the char is punctuation.
    if i in string.punctuation:
        # Printing the punctuation values
        print("Punctuation: " + i)


#