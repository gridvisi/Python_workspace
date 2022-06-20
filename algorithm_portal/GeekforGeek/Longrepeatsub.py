# Function to find LRS of substrings `X[0…m-1]`, `X[0…n-1]`
def LRS(X, m, n, lookup):
    # if the end of either sequence is reached,
    # return an empty string
    if m == 0 or n == 0:
        return ''

    # if characters at index `m` and `n` matches and the index are different
    if X[m - 1] == X[n - 1] and m != n:
        return LRS(X, m - 1, n - 1, lookup) + X[m - 1]
    else:
        # otherwise, if characters at index `m` and `n` don't match
        if lookup[m - 1][n] > lookup[m][n - 1]:
            return LRS(X, m - 1, n, lookup)
        else:
            return LRS(X, m, n - 1, lookup)


# Function to fill the lookup table by finding the length of LRS
# of substring `X[0…n-1]`
def LRSLength(X, lookup):
    # Fill the lookup table in a bottom-up manner.
    # The first row and first column of the lookup table are already 0.
    for i in range(1, len(X) + 1):
        for j in range(1, len(X) + 1):
            # if characters at index `i` and `j` matches
            # and the index are different
            if X[i - 1] == X[j - 1] and i != j:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # otherwise, if characters at index `i` and `j` are different
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


if __name__ == '__main__':
    X = 'ATACTCGGA'
    X = 'AAATAAATTTCTACGGAA'
    # lookup[i][j] stores the length of LRS of substring `X[0…i-1]` and `X[0…j-1]`
    lookup = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]

    # fill lookup table
    LRSLength(X, lookup)

    # find the longest repeating subsequence
    print(LRS(X, len(X), len(X), lookup))