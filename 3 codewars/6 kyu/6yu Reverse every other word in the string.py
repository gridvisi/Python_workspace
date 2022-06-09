'''
https://www.codewars.com/kata/reverse-every-other-word-in-the-string/train/python
est.assert_equals(reverse_alternate("Did it work?"), "Did ti work?")
Test.assert_equals(reverse_alternate("I really hope it works this time..."), "I yllaer hope ti works siht time...")
Test.assert_equals(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
Test.assert_equals(reverse_alternate("Have a beer"), "Have a beer")
Test.assert_equals(reverse_alternate(""), "")
'''
string = "Reverse this string, please!"
string = 'this is not tset '
string = 'This       si a  test  '
string = ''
#print(string.split(' ')[1][::-1],len(string.split(' ')))

def reverse_alternate(string):
    if len(string) == 0:
        return ''
    else:
        str_rev = ' '.join(string.split()).split(' ')
        for x in range(len(str_rev)):
            if x % 2 == 1:
                print(x, str_rev [x])
                str_rev[x] = str_rev[x][::-1]
            print(str_rev)
        return ' '.join(str_rev)

def reverse_alternate(string):
    return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))

def reverse_alternate(s):
  words = s.split()
  words[1::2] = [word[::-1] for word in words[1::2]]
  return ' '.join(words)
print(reverse_alternate(string))

m = 7
if m % 2 == 1:
    print(m)
else:print(m-1)

