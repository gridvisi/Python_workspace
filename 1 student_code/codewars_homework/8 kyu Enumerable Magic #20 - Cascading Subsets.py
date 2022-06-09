'''
https://www.codewars.com/kata/545af3d185166a3dec001190/train/python


'''

def each_cons(lst, n):
    # your solution here
    return [lst[i:i+n] for i in range(len(lst)-n+1)]
#[lst[i:i+n] for i in range(len(lst[:-n+1]))]
lst = [3, 5, 8, 13]
print(lst[0:1])
print(each_cons(lst,1))