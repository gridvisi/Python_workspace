#https://www.geeksforgeeks.org/decimal-to-binary-using-recursion-and-without-using-power-operator/

'''
Given an integer N, the task is convert and print the binary equaiva;ent of N.
Examples:


Input: N = 13
Output: 1101
Input: N = 15
Output: 1111

Time Complexity: O(logN)
Auxiliary Space: O(logN)

Attention reader! Don’t stop learning now. Get hold of all the important
DSA concepts with the DSA Self Paced Course at a student-friendly price
and become industry ready.

To complete your preparation from learning a language to DS Algo and many more,
please refer Complete Interview Preparation Course.

In case you wish to attend live classes with experts, please refer DSA Live
Classes for Working Professionals and Competitive Programming Live for Students.
'''


# Python3 implementation of the approach

# Recursive function to convert n
# to its binary equivalent
def decimalToBinary(n):
    # Base case
    if (n == 0):
        print("0", end="")
        return

    # Recursive call
    decimalToBinary(n // 2)
    print(n % 2, end="")


# Driver code
if __name__ == "__main__":
    n = 13
    decimalToBinary(n)
