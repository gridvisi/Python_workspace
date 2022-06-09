'''
https://www.geeksforgeeks.org/generating-all-possible-subsequences-using-recursion/

ven an array. The task is to generate and print all of the possible subsequences of the given array using recursion.

Examples:

Input : [1, 2, 3]
Output : [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]

Input : [1, 2]
Output : [2], [1], [1, 2]
'''


# Python3 code to print all possible
# subsequences for given array using
# recursion

# Recursive function to print all
# possible subsequences for given array
def printSubsequences(arr, index, subarr):
    # Print the subsequence when reach
    # the leaf of recursion tree
    if index == len(arr):

        # Condition to avoid printing
        # empty subsequence
        if len(subarr) != 0:
            print(subarr)

    else:
        # Subsequence without including
        # the element at current index
        printSubsequences(arr, index + 1, subarr)

        # Subsequence including the element
        # at current index
        printSubsequences(arr, index + 1,
                          subarr + [arr[index]])

    return


arr = [1, 2, 3]

printSubsequences(arr, 0, [])