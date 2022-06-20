'''
myobj = Anoject(a=17,b=23,c=42,d=99)
print(myojb.a,
import operator
operator.attrgetter('a","b","c")(my_obj)

'''
class AnOject:
    def __int__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

myobj = AnOject
#myobj(a=17,b=23,c=42,d=99)
myobj.d,myobj.a,myobj.b,myobj.c = 17,23,42,99
a,b,c,d =17,23,42,99
#myobj = [a,b,c,d]
#print(myobj.a,myobj.b,myobj.c)

import operator
s = operator.attrgetter("a","b","c")(myobj)
print(s)