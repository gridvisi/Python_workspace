'''
https://www.codewars.com/kata/the-poet-and-the-pendulum/train/python
Notes
Array/list size is at least *3*** .

In Even array size , The minimum element should be moved to (n-1)/2 index (considering that indexes start from 0)

Repetition of numbers in the array/list could occur , So (duplications are included when Arranging).

Input >> Output Examples:
pendulum ([6, 6, 8 ,5 ,10]) ==> [10, 6, 5, 6, 8]
Explanation:
Since , 5 is the The Smallest element of the list of integers , came in The center position of array/list

The Higher than smallest is 6 goes to the right of 5 .

The Next higher number goes to the left of minimum number and So on .

Remeber , Duplications are included when Arranging , Don't Delete Them .

pendulum ([-9, -2, -10, -6]) ==> [-6, -10, -9, -2]
Explanation:
Since , -10 is the The Smallest element of the list of integers , came in The center position of array/list

The Higher than smallest is -9 goes to the right of it .

The Next higher number goes to the left of -10 , and So on .

Remeber , In Even array size , The minimum element moved to (n-1)/2 index (considering that indexes start from 0) .

pendulum ([11, -16, -18, 13, -11, -12, 3, 18 ]) ==> [13, 3, -12, -18, -16, -11,
'''
values = [11, -16, -18, 13, -11, -12, 3, 18 ]
sort_v = sorted(values)
print(sort_v)
def pendulum(values):
    sort_v = sorted(values)
    re_left,re_right = [],sort_v
    for i in range(2,int(len(values)),2):
        re_left.append(sort_v[i])
        re_left = sorted(re_left,reverse=True)

        re_right.remove(sort_v[i])
    return re_left + re_right

print(pendulum(values))

'''
re = [0] * (len(values))
    sort_v = sorted(values)
    re[int(len(values)/2)] = sort_v[0]
    index = [[i,-i] for i in range(int(len(values)/2))]
    sort_v.insert(0,sort_v[i])
        sort_v.remove(sort_v[i])
    print(index,sort_v,re)
    i = 0
    while int(len(values)/2) - (-1)**i*i < len(values) :
        re[int(len(values)/2) + (-1)**i*(-i)] = sort_v[i]
        i += 1
'''

