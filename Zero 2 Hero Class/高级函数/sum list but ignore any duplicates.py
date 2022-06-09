'''
https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python
test.assert_equals(sum_no_duplicates([1, 1, 2, 3]), 5)
test.assert_equals(sum_no_duplicates([1, 1, 2, 2, 3]), 3)
'''


from collections import Counter
def sum_no_duplicates(l):
    keyCount = Counter(l)
    return sum([k for k ,v in keyCount.items() if v== 1])
l = [1, 1, 2, 2, 3]
print(sum_no_duplicates(l))

#2
def sum_no_duplicates(l):
    print(l)
    uniques = []
    dups = []
    for n in l:
        if n not in uniques:
            uniques.append(n)
        else:
            if n not in dups:
                dups.append(n)
    return sum(uniques) - sum(dups)
l = [1, 1, 2, 2, 3]
print(sum_no_duplicates(l))

'''

print(a & b )     #交集 {4, 5}

print(a | b)       #并集 {1, 2, 3, 4, 5, 6, 7, 8}

print(a - b)       #差积 {1, 2, 3}    in  a   but not in b

print(b - a)       #差积 {6,7,8}      in  b   but not a 

print( b ^ a )     #对称 {1, 2, 3, 6, 7, 8}

print(a < b )      #子集 a 是否是b的子集

print(a > b )      #超集 a 是否是b的父集

转载于:https://www.cnblogs.com/linux-error/p/9243351.html

'''
#3 Flag way of thinking NOT WORK!
def sum_no_duplicates(l):
    lsort = sorted(l)
    flag,prev = 0,lsort[0]  # 0 stand for item appear before!! float('info')
    i,j,ans = 0,1,[]
    while j < len(lsort):
        if lsort[i] == lsort[j]:
            i = j + 1
            j = i + 1
        else:
            ans.append(lsort[i])
            #flag = not flag
            i += 1
            j += 1

    return ans
l = [1, 1, 2, 2, 3]
print('3rd flag:',sum_no_duplicates(l))
