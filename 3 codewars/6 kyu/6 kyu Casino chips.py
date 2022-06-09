#https://www.codewars.com/kata/5e0b72d2d772160011133654/train/python
'''
   test.assert_equals(solve([1,1,1]), 1)
        test.assert_equals(solve([1,2,1]), 2)
        test.assert_equals(solve([4,1,1]), 2)
        test.assert_equals(solve([8,2,8]), 9)
        test.assert_equals(solve([8,1,4]), 5)
        test.assert_equals(solve([7,4,10]), 10)
        test.assert_equals(solve([12,12,12]), 18)
        test.assert_equals(solve([1,23,2]), 3)
'''
#1st solution
def solve(xs):
    x, y, z = sorted(xs)
    return min(x + y, (x + y + z) // 2)
xs = [10,10,10]
xs = [58,20,38]
xs = [58,20,40]
print(solve(xs))

#2nd solution
def score(a,b,c):
    if a+b<c: return a+b
    return (a+b-c)//2+c

def solve(arr):
    a,b,c = arr
    return min(score(a,b,c),score(b,c,a),score(c,a,b))

#3rd solution
def solve(arr):
    c,b,a = sorted(arr)
    return c+b if a >= c+b else a + (c+b-a) // 2


def solve(arr,day=0):

    #print('path:', path_1, path_2, path_3)
    if arr.count(0) == 1:
        print(arr, day)
        return day

    elif sorted(arr) == [0,1,1] or sorted(arr) == [1,1,1]:
        return 1
    elif sorted(arr) == [1,2,1]:
        return 2
    else:
        day += 1
        solve([arr[0]-1, arr[1]-1, arr[2]],day)
        #path_2 = solve([arr[0], arr[1]-1, arr[2]-1],day)
        #path_3 = solve([arr[0]-1, arr[1], arr[2]-1],day)


#arr = [8,1,4]
arr = [12,12,12]
arr = [8,2,8]  #[8,2,8]), 9
arr = [2,2,1]
print('recur',solve(arr,day=0))


# imply: n + min(n-i,i)
mx = max([arr[0] + min(arr[0]-i,i) for i in range(arr[0])])
print('mx:'+f"{arr}",mx)

#arr = [3,3,3] #(2,2,3)->(0,2,1)->(0,1,0) = 4

arr = [12,12,12]
arr = [7,4,10]
arr = [8,1,4]
if arr[0] != arr[1] != arr[2]:print("total equal")
def solve(arr):
    '''

    :param arr: input 3 chip with different color
    :return: moves total by 2 differ color chip per day
    '''
    if arr[0] == arr[1] == arr[2]:
        return max([arr[0] + min(arr[0]-i,i) for i in range(arr[0])])
    # all chips equal with each other

    # [8,2,8] -> [2,2,2] + (8-2)
    # [9,2,8] -> [7,0,8]+(9-2) -> (8-7)+(9-2)
    else:
        if len(set(arr))+1 == len(arr):
            base = min(arr)
            day = max(arr) - base
            day += max([base + min(base-i,i) for i in range(base)])
            return day

        elif len(set(arr)) == len(arr):
            day = "x"
            return day

arr = [8, 2, 8]
arr = [1,23,2]
print('solve('+f"{arr}"+"):",solve(arr))


# If condition 1st
arr = [2,2,2]
print(f"{arr}",max([arr[0] + min(arr[0]-i,i) for i in range(arr[0])]))

# If condition 2nd
arr = [2,3,4]


# if condition 3rd
# pattern with [x+2,x,x+2] like fellow arr
arr = [8, 2, 8]
day = max(arr) - min(arr)
arrs = [min(arr)]*len(arr)
day += max([arrs[0] + min(arrs[0]-i,i) for i in range(arrs[0])])
print(day)


'''
def solve(arr):
    
    #:param arr: input 3 chip with different color
    #:return: moves total by 2 differ color chip per day
    
    if arr[0] == arr[1] == arr[2]:
        return max([arr[0] + min(arr[0]-i,i) for i in range(arr[0])])
    # all chips equal with each other

    elif arr[0] != arr[1] != arr[2]:
        arrs,day = arr,0
        while len(arrs) > 2:
            if len([i for i in arrs if i != 0]) == 0:
                return day
            arrs = [i for i in arrs if i != 0]
            chip = min(arrs)
            print(arrs,day,chip)
            arrs = [i - chip if i==max(arrs) or i==min(arrs) else i for i in arrs]
            day += chip
        return day

    else:
        day = max(arr) - min(arr)
        arrs = [min(arr)]*len(arr)
        day += max([arrs[0] + min(arrs[0]-i,i) for i in range(arrs[0])])
        return day

arr = [8, 2, 8]
print('solve():',solve(arr))
'''

'''
def solve(arr,step=0):
    n = int(''.join([str(i) for i in arr]))
    for i in range(max(arr)):
        arrs = [int(''.join(sorted(list(str(i))))) for i in [n-11,n-110,n-101]]
        if 0 in set(arrs):
            return step            
        else:
            arrs = [i for i in set(arrs)]
            step += 1
        return solve(arr,step)
'''
