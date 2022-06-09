'''
https://www.codewars.com/kata/airport-arrivals-slash-departures-number-1/train/javascript
You notice that each flap character is on some kind of a rotor and the order of characters on each rotor is:
ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789
And after a long while you deduce that the display works like this:
Consider a flap display with 3 rotors and one 1 line which currently spells CAT

Step 1 (current rotor is 1)
Flap x 1
Now line says DBU
Step 2 (current rotor is 2)
Flap x 13
Now line says DO)
Step 3 (current rotor is 3)
Flap x 27
Now line says DOG
This can be represented as

lines  // array of strings. Each string is a display line of the initial configuration
rotors // array of array-of-rotor-values. Each array-of-rotor-values is applied to the corresponding
display line
result // array of strings. Each string is a display line of the final configuration
e.g.

lines = ["CAT"]
rotors = [[1,13,27]]
result = ["DOG"]
Kata Task
Given the initial display lines and the rotor moves for each line, determine what the board will say
after it has been fully updated.

For your convenience the characters of each rotor are in the pre-loaded constant ALPHABET which is a
string.
def BEFORE(a):
    print("Before:");
    return pretty_print(a);

def AFTER(a):
    print("After:");
    return pretty_print(a);

test.it('CAT => DOG')
before = BEFORE(["CAT"])
rotors = [[1, 13, 27]];
after = AFTER(flap_display(before, rotors))
expected = ["DOG"]
test.assert_equals(after, expected)

test.it('HELLO => WORLD!')
before = BEFORE(["HELLO "])
rotors = [[15, 49, 50, 48, 43, 13]]
after = AFTER(flap_display(before, rotors))
expected = ["WORLD!"]
test.assert_equals(after, expected)

test.it('CODE => WARS')
before = BEFORE(["CODE"])
rotors = [[20,20,28,0]]
after = AFTER(flap_display(before, rotors))
expected = ["WARS"]
test.assert_equals(after, expected)
'''
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
values, res = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789', []
l, step = len(table), 0
key = [i for i in range(l)]
dic = dict(zip(key, values))
print(dic[1])
x = ')'
for i,e in enumerate(dic):
    if e == x:
        print(x,i)

lines, rotors = 'HELLO ',[15, 49, 50, 48, 43, 13] #'WORLD!'
lines, rotors = 'CAT',[1, 13, 27] #=> DOG'
print(lines[1:])

def flap_display(lines, rotors):
    values,res,s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789',[],''
    l = len(values)
    for e in lines:
        for i,x in enumerate(values):
            if e == x:
                res.append(i)
    arr = list(map(lambda x,y:x + y,[i for i in res],[sum(rotors[0:j+1]) for j in range(len(rotors))]))
    s = [values[i%l] for i in arr]
    return lines + '=>' + ''.join(s)
print(flap_display(lines, rotors))

line = list(lines)
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789')
flap_display = lambda lines, rotors: [
    # Find new string
    ''.join([
        # Get new character by moving index of old
        # by sum of rotor values up to current symbol
        ALPHABET[(ALPHABET.index(smb) + sum(rot[:sid+1])) % len(ALPHABET)]
        # Loop trough each character(smb) and its index(sid(from symbol id))
        for sid, smb in enumerate(line)
    ])
    # Loop trough each line and rotors, assigned to that line
    for line, rot in zip(lines, rotors)
]

print(flap_display(lines, rotors))

'''
lines, rotors = list('HELLO '),[15, 49, 50, 48, 43, 13]
def flap_display(lines, rotors):
    ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789')
    result = []
    for l,r in zip(lines,rotors):
        spun, line = 0, ""
        for c,n in zip(l,r):
            spun += n
            line += ALPHABET[(ALPHABET.index(c)+spun)%len(ALPHABET)]
        result.append(line)
    return result
print(flap_display(lines, rotors))
'''



def flap_display(lines, rotors):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789')
    board = []
    for i, line in enumerate(lines):
        spins = 0
        newline = []
        for letter in line:
            spins += rotors[i].pop(0)
            newline.append(alphabet[(alphabet.index(letter) + spins) % len(alphabet)])
        board.append(''.join(newline))
    return board


'''

def flap_display(lines, rotors):
    values,res = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789',[]
    l,st,arr = len(values),0,''
    key = [i for i in range(l)]
    dic1 = dict(zip(key,values))
    dic2 = dict(zip(values,key))
    for i,x in enumerate(lines):
        re = dic1[(dic2[x] + sum(rotors[:i+1]))%l]
        arr += re
    return lines + '=>' + arr

def flap_display(lines, rotors):
    values,res = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789',[]
    l,st,arr = len(values),0,[]
    key = [i for i in range(l)]
    dic1 = dict(zip(key,values))
    dic2 = dict(zip(values,key))
    print(dic)
    line = lines
    for n in rotors:
        arr = list(map(lambda x:dic1[dic2[x] + n],[x for x in line[st:]]))
        line = arr
        st += 1
        return line,arr

print(flap_display(lines, rotors))

'''