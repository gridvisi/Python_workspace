'''
https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python

animals = [ 'dog', 'cat', 'elephant' ]
test.assert_equals(list_animals(animals), '1. dog\n2. cat\n3. elephant\n')
'''

def list_animals(animals):
    list = ''
    for i in range(len(animals)): #length
        list += str(i+1) + '. ' + animals[i] + '\n'
    return list

animals = [ 'dog', 'cat', 'elephant' ]
print(animals[1])

print(list_animals(animals))

print(" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ")

'''
res = 0
res = ''
'''
res = []
i = 1
#j = 2
res += [i] # res = res + [i]
#res += [j]
print(res)

def create_array(n):
    res = [] #result <= res
    i = 1
    while i <= n:
        res += [i*2]
        i += 1
        print(i,res)
    return res
n = 10
print(create_array(n))

print(list(range(0,20,2))) #slice
