'''
https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

    larr = list(map(len,strarr))
    mxl = [x+y for x,y in zip(larr[:-1],larr[1:])]
'''

def longest_consec(strarr, k):
    if k > len(strarr) or k < 0:return ""
    anstr = [[''.join(strarr[s:s+k]), len(''.join(strarr[s:s+k]))] for s in range(0,len(strarr))]
    return max(anstr,key=len)[0]

#max(anstr,key=lambda x:x[1])[0]

strarr, k = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2  # --> "abigailtheta"
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2
print(longest_consec(strarr,k))

#similar solve
def longest_consec(strarr, k):
    if k>len(strarr) or k<1 or not strarr:
        return ""
    return max(["".join(strarr[i:i+k]) for i in range(len(strarr))], key=len)


#1st
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

#3rd
def longest_consec(strarr, k):
    # Make sure that k is greater than zero and less that the
    # length of the array of strings. Otherwise return an empty string
    if k <= 0 or k > len(strarr):
        return ''

    # Finding the longest string consisting of k consecutive
    # strings is equivalent to finding the maximum sum of
    # k consecutive elements of an array that represents the
    # lengths of an array of strings.

    # star_lengths represents a list of lengths of the initial
    # array of strings.
    starr_lengths = list(map(len, strarr))
    # Find the maximum sum of k consecutive elements
    # requires keeping a temperary maximum length.
    temp_max_len = 0
    # We also need to keep the position of the first element of
    # each group.
    position = 0

    # Scan the whole list of lengths except the final k elements
    for p in range(len(starr_lengths) - (k - 1)):
        # We need to find the sum of the current set of elements
        # starting at position p
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p + i]

        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position + k]])

#5
def longest_consec(a, k):
    if len(a) == 0 or k > len(a) or k <= 0: return ''
    res=[]
    for n in range(len(a)-k+1):
        for t in range(1,k):
            a[n]+=a[n+t]
    return max(a,key=len)


#7
def longest_consec(strarr, k):
    consec =""
    longest = ""

    for n in range (0,len(strarr)-k+1):
        for i in range(n,n+k):
            consec += strarr[i]
        if len(consec) > len(longest):
            longest = consec
        consec =""
    return longest