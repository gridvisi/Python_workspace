'''
https://www.codewars.com/kata/6001a06c6aad37000873b48f/train/python
Your code can be maximum 510 characters long. Oh, and no imports, please!

On the First day of Christmas
My true love sent to me
A partridge in a pear tree.

On the Second day of Christmas
My true love sent to me
Two turtle doves, and
A partridge in a pear tree.

...

On the Twelfth day of Christmas
My true love sent to me
Twelve drummers drumming,
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five gold rings,
Four calling birds,
Three French hens,
Two turtle doves, and
A partridge in a pear tree.

'''



def f():
    x = 'A partridge in a pear tree.'

    s = '''On the First day of Christmas
    My true love sent to me
   
    On the Second day of Christmas
    My true love sent to me
    Two turtle doves, and
    
    ...

    On the Twelfth day of Christmas
    My true love sent to me
    Twelve drummers drumming,
    Eleven pipers piping,
    Ten lords a-leaping,
    Nine ladies dancing,
    Eight maids a-milking,
    Seven swans a-swimming,
    Six geese a-laying,
    Five gold rings,
    Four calling birds,
    Three French hens,
    Two turtle doves, and
    
    '''
    return s

print(f())

#1st
f=lambda:"\n\n".join("On the %s day of Christmas\nMy true love sent to me\n"%"First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth".split()[i]+'\n'.join("Twelve drummers drumming,*Eleven pipers piping,*Ten lords a-leaping,*Nine ladies dancing,*Eight maids a-milking,*Seven swans a-swimming,*Six geese a-laying,*Five gold rings,*Four calling birds,*Three French hens,*Two turtle doves, and*A partridge in a pear tree.".split('*')[11-i:]) for i in range(12))

#2nd
A="""Twelve drummers drumming,
Eleven pipers piping,
Ten lords a-leaping,
Nine ladies dancing,
Eight maids a-milking,
Seven swans a-swimming,
Six geese a-laying,
Five gold rings,
Four calling birds,
Three French hens,
Two turtle doves, and
A partridge in a pear tree.""".split("\n")
B="First,Second,Third,Fourth,Fifth,Sixth,Seventh,Eighth,Ninth,Tenth,Eleventh,Twelfth".split(",")
f=lambda:"\n\n".join(f"On the {B[i]} day of Christmas\nMy true love sent to me\n"+"\n".join(A[-i-1:])for i in range(12))