'''
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

Test.describe("Sample Test Cases")

Test.it("Simple Tests")
Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
'''
import re
def solution(args):
    i,j = 0,1
    ans = []
    conseq = list(range(min(args),max(args)+1))
    #stnd = [min(args),max(args)+1]
    #ans = ','.join([str(i) if i in args else '' for i in conseq])
    #res = re.sub(r'[,]','-',ans)
    sl = [i if i in args else '' for i in conseq]
    sl = [str(i) for i in sl]
    sl.append('')
    pro, temp = [], []
    for i in sl:
        if not i == '':
            temp.append(i)
        else:
            if not len(temp) == 0:
                pro.append(temp)
                temp = []
    opt = ""
    for i in pro:
        if len(i) >= 3:
            opt += i[0]+'-'+i[-1]+','
        elif len(i) == 2:
            opt += i[0]+','+i[1]+','
        else:
            opt += i[0]+','
    return opt[:-1]

args = [-3,-2,-1,2,10,15,16,18,19,20]
# args = [1,2,3,4,5]
print(solution(args))

#1st solution
def solution(args):
    out = []
    beg = end = args[0]
    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)

'''
    while i < j < len(ans):
        if ans[i] == ',' and ans[i+1] != ',':
            j = i+1
            j += 1
            

'''

def solution(args):
    i,j = 0,1
    ans = []
    conseq = list(range(min(args),max(args)+1))
    stnd = [min(args),max(args)+1]
    st = stnd[0]
    #for i in args:
    res = ''
    while i <= len(args):
        if args[i] == st and i < len(args)-1:
            res += str(args[i])
            st += 1

        else:
            st = args[i]
            st += 1
            res += ',' + str(args[i])
        #res += str(ans[0])+ str(ans[-1])
        print(res, st, i)
        i += 1
    #ans = ','.join([str(i) if i in args else '' for i in conseq])
    #res = re.sub(r'[,]','-',ans)
        if i == len(args):
            return res


#1st solution
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)

#2nd solution
def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b+1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)