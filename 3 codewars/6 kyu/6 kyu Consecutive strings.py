# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

strarr, k = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2
strarr, k = [], 3
strarr, k = ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15
strarr, k = ["zone", "abigail", "theta", "form", "libe", "zas"], -2
def longest_consec(strarr, k):
    if len(strarr) == 0 or len(strarr) == 1 or k>len(strarr) or k<0:return ""
    #re =[''.join(strarr[i:i+k]) for i in range(len(strarr)-k+1)]
    re = [sum(list(map(len,strarr[i:i + k]))) for i in range(len(strarr) - k + 1)]
    return ''.join(strarr[re.index(max(re)):re.index(max(re))+k])

# 1st solution
def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result
print(longest_consec(strarr, k))

# 2nd solution
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

# 3rd solution
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))

# 4th solution
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