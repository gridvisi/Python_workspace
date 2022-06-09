'''
https://www.codewars.com/kata/5d7d05d070a6f60015c436d1/train/python

get_w(3) # should return:
[
'*   *   *',
' * * * * ',
'  *   *  '
]

get_w(5) # should return:
[
'*       *       *',
' *     * *     * ',
'  *   *   *   *  ',
'   * *     * *   ',
'    *       *    '
]
'''
print("****\n****")
print(["****","****"])
import numpy as np
def get_w(height):
    art = []
    star = (2 * height + height-1 + height-2) * [' ']
    l = len(star)
    print(star,l)
    for i in range(height):
        l = len(star)
        #l[i],l[(l-1)//2-1],l[(l-1)//2+1],l[len(l)-i] = "*","*","*","*"
        # #'str' object does not support item assignment
        #print(l,i)
        centre = l//2
        scope = [i,centre-i,centre+i,l-1-i]
        #print(scope,centre)
        a = "".join(["*" if i in scope else ' ' for i,e in enumerate(star)])
        print(a)
        #a = a +'\n'
        art.append(a)
    return np.array(art)
height = 5
print(get_w(height))

