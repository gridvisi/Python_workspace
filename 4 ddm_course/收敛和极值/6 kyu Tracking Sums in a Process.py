'''
https://www.codewars.com/kata/56dbb6603e5dd6543c00098d/train/python

#[5, 3, 6, 10, 5, 2, 2, 1] (34) ----> [5, 3, 6, 10, 2, 1] ----> (27) ------>
[10, 6, 5, 3, 2, 1]  ----> [4, 1, 2, 1, 1] (9) -----> [4, 1, 2] (7)
'''
# set depulicate - sort - deduce - set

arr = [5, 3, 6, 10, 5, 2, 2, 1]
def track_sum(arr):
    result = []
    arrs= sorted([i for i in set(arr)],reverse=True)
    ans = [x-y for x,y in zip(arrs[:-1],arrs[1:])]
    return set(ans) #[[], []]
print(track_sum(arr))