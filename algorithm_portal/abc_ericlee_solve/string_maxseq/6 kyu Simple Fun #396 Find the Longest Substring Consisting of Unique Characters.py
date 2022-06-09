'''
6 kyu
Simple Fun #396: Find the Longest Substring Consisting of Unique Characters

https://www.codewars.com/kata/5bcd90808f9726d0f6000091/train/python

test.assert_equals(longest_substring("baacab"), 3,"'cab' is the longest substring.")
test.assert_equals(longest_substring("abcd"), 4,"'abcd' is the longest substring.")
test.assert_equals(longest_substring("hchzvfrkmlnozjk"), 11,"'cchzvfrkmlnoab' is the longest substring.")
test.assert_equals(longest_substring("!@#$%^&^%$#@!"), 7,"'!@#$%^&' is the longest substring.")
test.assert_equals(longest_substring("abcd" * 10000 + "abcde" + "abcd" * 10000), 5,"'abcde' is the longest substring.")
'''
# Top 1st
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
print(longest_substring(s))
'''

def longest_substring(s : str) -> int:
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
            #print(seq[l:r])
            l = r
            r += 1
            s = 1
            #if r == len(seq)-1:
            #    ans.append(seq[l:r])
    ans.append(seq[l:r+1])
    return ans,l,r

'''