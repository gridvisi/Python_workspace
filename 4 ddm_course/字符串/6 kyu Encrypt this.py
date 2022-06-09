'''
https://www.codewars.com/kata/5848565e273af816fb000449/train/python
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''
text = "Hello"
text = "hello world"
text = "a"  #, ""
#text = "Thank you Piotr for all your help"
def encrypt_this(text):
    if len(text) == 1:return ord(text)
    s = ''
    for w in text.split():
        #print(w)
        s += str(ord(w[0])) + w[-1]+w[2:-1] + w[1]+' '
    return s


def encrypt_this(text):
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append(''.join(word))

    return ' '.join(result)
print(encrypt_this(text))


#''.join([str(ord(e)) if i == 0 else e for i,e in enumerate(w[::-1])])