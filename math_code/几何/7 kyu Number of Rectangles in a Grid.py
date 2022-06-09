'''
https://www.codewars.com/kata/556cebcf7c58da564a000045/train/python

ven a grid of size m x n, calculate the total number of rectangles contained in this rectangle. All integer sizes and positions are counted.

Examples:

numberOfRectangles(3, 2) == 18
numberOfRectangles(4, 4) == 100
Here is how the 3x2 grid works (Thanks to GiacomoSorbi for the idea):

1 rectangle of size 3x2:

[][][]
[][][]
2 rectangles of size 3x1:

[][][]
4 rectangles of size 2x1:

[][]
2 rectangles of size 2x2

[][]
[][]
3 rectangles of size 1x2:

[]
[]
6 rectangles of size 1x1:

[]
As you can see (1 + 2 + 4 + 2 + 3 + 6) = 18, and is the solution for the 3x2 grid.

There is a very simple solution to this!
'''
def number_of_rectangles(m, n):
    return n*m*(n+1)*(m+1)/4


def number_of_rectangles(m, n):
    # Note that the number of subrectangles of each size is symmetric
    # to their areas. So that we can sum the areas of various
    # subrectanges.

    # return sum(a * b for a in range(1, m + 1) for b in range(1, n + 1))

    # This can be refactored to:

    # return sum(range(1, m + 1)) * sum(range(1, n + 1))

    # And we can compute the sums of ranges analytically
    # just as Gauss in the school in order to go from
    # O(max(N,M)) complexity to O(1)!

    # sum(range(1, n + 1)) == (n + 1) * n / 2

    # R = (m + 1) * m / 2 * (n + 1) * n / 2

    # After a simplification:

    return ((m + 1) * m * (n + 1) * n) / 4


def number_of_rectangles(m, n):
    if m==1 and n==1:return 1
    if m==1 and n==2:return 3
    if m==2 and n==1:return 3
    if m==2 and n==2:return 9
    return number_of_rectangles(m-1,n)

'''
def number_of_rectangles(m, n):
    cunt = m * n
    mleap,nleap = 1,1
    while mleap < m and nleap < n:
        mleap = 1
        for i in range(0,m+1,mleap):
            nleap = 1
            for j in range(0,n+1,nleap):
                cunt += 1
            nleap += 1
        mleap += 1
    return cunt
'''