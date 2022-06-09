'''
https://www.geeksforgeeks.org/print-all-subsequences-of-a-string-using-arraylist/

Examples:


Input: str = “abc”
Output: a b ab c ac bc abc
Input: str = “geek”
Output: g e ge e ge ee gee k gk ek gek ek gek eek geek

'''


# Python implementation of the approach

# Utility function to print the contents
# of the ArrayList
def printArrayList(arrL):
    arrL.remove("")
    print(*arrL, sep=" ")


# Function to returns the arraylist which contains
# all the sub-sequences of str
def getSequence(Str):
    # If string is empty
    if (len(Str) == 0):
        # Return an empty arraylist
        empty = []
        empty.append("")
        return empty

    # Take first character of str
    ch = Str[0]

    # Take sub-string starting from the
    # second character
    subStr = Str[1:]

    # Recurvise call for all the sub-sequences
    # starting from the second character
    subSequences = getSequence(subStr)

    # Add first character from str in the beginning
    # of every character from the sub-sequences
    # and then store it into the resultant arraylist
    res = []

    for val in subSequences:
        res.append(val)
        res.append(ch + val)

    # Return the resultant arraylist
    return res


# Driver code
Str = "geek"
printArrayList(getSequence(Str))


#Alternate Solution: One by one fix characters and recursively
# generate all subsets starting from them.

# Python3 implementation of the approach

# Function to print all the sub-sequences
# of a string
def printSubSeq(sub, ans):
    if (len(sub) == 0):
        print(ans, end=" ")
        return

    # First character of sub
    ch = sub[0]

    # Sub-string starting from second
    # character of sub
    ros = sub[1:]

    # Excluding first character
    printSubSeq(ros, ans)

    # Including first character
    printSubSeq(ros, ans + ch)


Str = "abc"
printSubSeq(Str, "")

# This code iscontributed by divyeshrabadiya07
