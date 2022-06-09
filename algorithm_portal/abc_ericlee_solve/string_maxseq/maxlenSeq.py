
# https://www.codewars.com/kata/5bcd90808f9726d0f6000091/train/python

def longest_substring(s):
    last_idx = {}
    start_idx = max_len = 0
    for i in range(0, len(s)):
        if s[i] in last_idx:
            start_idx = max(start_idx, last_idx[s[i]] + 1)
        max_len = max(max_len, i-start_idx + 1)
        last_idx[s[i]] = i
    return max_len,last_idx
s = "hchzvfrkmlnozjk"
s = 'abbcd'
print('1st solution:',longest_substring(s))

seq = s
# dict solve Maxseq
def maxseq(seq):
    last_idx = seq[0]
    #start_idx = max_len = 0
    maxSrg = [last_idx]
    for i,e in enumerate(seq[1:]):
        #print(maxSrg,last_idx)
        #if e not in last_idx:
        if ord(e) != ord(last_idx[-1])+1:
            last_idx = e
        else:
            last_idx += e
            if len(last_idx) > len(max(maxSrg,key=len)):
                maxSrg.clear()
                maxSrg.append(last_idx)

            elif len(last_idx) == len(max(maxSrg,key=len)):
                maxSrg.append(last_idx)
    return maxSrg,last_idx
seq = 'cdeffggfghijkaabcdecabccdd'
seq = '34567885678910111212345'
print('No.0 solution:',maxseq(seq))


def maxseq(seq):
    ans = []
    l,r = 0,1
    s = 1
    for _ in range(len(seq[:-1])):
        print("test 2:", l, r, s)
        if ord(seq[l]) + s != ord(seq[r]):
            l = r
            r += 1
            #s = 1
        elif ord(seq[l]) + s == ord(seq[r]):
            ans.append(seq[l:r])
            print('2~',seq[l:r])
            s += 1
            r += 1
            s = 1
        ans.append(seq[l:r])
    return ans,l,r
print('2nd solution:',maxseq(seq))



'''
3rd solution
'''
seq = "abcdefxxghijklmvntop5qa"
print([((ord(seq[l]) + 1,ord(seq[l])) for l in range(len(seq)))])
print([ord(seq[l]) for l in range(len(seq))])
def maxseq(seq):
    ans = []
    l,r = 0,1
    s = 1
    while l <= r and r < len(seq)-1:
        #print("test:", l, r, s)
        if ord(seq[l]) + s == ord(seq[r]):
            s += 1
            r += 1
        else:
            ans.append(seq[l:r])
            l = r
            r += 1
            s = 1
    ans.append(seq[l:r+1])
    return ans,l,r
seq = 'abbcd'
print('3rd solution',maxseq(seq))

