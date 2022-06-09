#https://www.codewars.com/kata/5376b901424ed4f8c20002b7/solutions


def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def iterative_closest(arr):
    n = len(arr)
    mini = ((arr[0], arr[1]), distance(arr[0], arr[1]))
    for i in range(n - 1):
        for j in range(i + 1, n):
            dij = distance(arr[i], arr[j])
            if dij < mini[1]:
                mini = ((arr[i], arr[j]), dij)
    return mini


def recursive_closest(arr):
    n = len(arr)
    if n <= 3:
        # if the array is less than 3 items
        # use the naive method
        return iterative_closest(arr)

    # divide the row into two parts
    # and search the closest pair of points in each
    mid = n // 2
    ml, mr = recursive_closest(arr[:mid]), recursive_closest(arr[mid:])

    # the closest pair is the one having the minimum
    # distance in both parts
    mlr = ml if ml[1] < mr[1] else mr

    # Now we have to combine the results from
    # the two parts

    # find the points that are close to the median point
    arr1 = [pt for pt in arr if abs(pt[0] - arr[mid][0]) < mlr[1]]
    arr1.sort(key=lambda pt: pt[1])  # sort it by Y coordinates
    # foreach of the points search within the next 7 points
    # which have the lowest distance
    n1 = len(arr1)
    for i in range(n1 - 1):
        for j in range(1, min(7, n1 - i)):
            dij = distance(arr1[i], arr1[i + j])
            if dij < mlr[1]:
                mlr = ((arr1[i], arr1[i + j]), dij)
    return mlr


def closest_pair(points):
    arr = sorted(points)
    return recursive_closest(arr)[0]


from scipy.spatial import cKDTree as KDT


#TOP 4th
def closest_pair(points):
    tree = KDT(points)
    record = None
    nn = tree.query(points, k=2)
    for i, dist in enumerate(nn[0]):
        if not record or record[0] > dist[1]:
            record = [dist[1], points[i], points[nn[1][i][1]]]
    return (record[1], tuple(record[2]))