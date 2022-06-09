'''
https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/python

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]

output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
'''

def toCsvText(array) :
    opt = ''
    for s in array:
        opt += ','.join([str(i) for i in s])+ " "
    return "\n".join(opt[:-1].split(' '))
array =  [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]
print(toCsvText(array))

#1st
def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)

