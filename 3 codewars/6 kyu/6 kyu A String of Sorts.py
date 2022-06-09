'''
https://www.codewars.com/kata/a-string-of-sorts/train/python
sort_string("foos", "of")       == "oofs"
sort_string("string", "gnirts") == "gnirts"
sort_string("banana", "abn")    == "aaabnn"
'''

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda student : student[2]))

def sort_string(st, order):
    return ''.join(sorted(list(st), key=lambda e: list(order).index(e) if e in order else len(order)))
s,ordering = "banana", "abn"
st,order = "foos", "of"
#print('index:',list(order).index(e) if e in order )
print(''.join(sorted(list(st), key=lambda e: list(order).index(e) if e in order else len(order))))
print(sort_string(st,ordering))

#1st solution
def sort_string(s, ordering):
    answer = ''
    for o in ordering:
        answer += o * s.count(o)
        s = s.replace(o,'')
    return answer + s

#2nd solution
def sort_string(s, ordering):
    dct = {c:-i for i,c in enumerate(reversed(ordering))}
    return ''.join(sorted(s,key=lambda c:dct.get(c,1)))

#3rd solution
sort_string=lambda s,o:''.join(sorted(s,key=lambda x,d={c:i for i,c in reversed(list(enumerate(o)))}:d.get(x,len(o))))

