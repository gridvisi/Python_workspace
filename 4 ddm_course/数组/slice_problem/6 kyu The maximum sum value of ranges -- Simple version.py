'''
When no more interesting kata can be resolved, I just choose to create the new kata,
to solve their own, to enjoy the process --myjinxin2015 said

Description:
For example:

 Given arr = [1,-2,3,4,-5,-4,3,2,1],
       range = [[1,3],[0,4],[6,8]]
 should return 6

 calculation process:
 range[1,3] = arr[1]+arr[2]+arr[3] = 5
 range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
 range[6,8] = arr[6]+arr[7]+arr[8] = 6
 So the maximum sum value is 6
Note:
arr/$a always has at least 5 elements;
range/$range/ranges always has at least 1 element;
All inputs are valid;
This is a simple version, if you want some challenge, please try the challenge version.
Some Examples
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3],[0,4],[6,8]]) === 6
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3]]) === 5
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,4],[2,5]]) === 0

st.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3],[0,4],[6,8]]), 6)
Test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3]]), 5)
Test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]), 0)
Test.assert_equals(max_sum([11,-22,31,34,-45,-46,35,32,21], [[1,4],[0,3],[6,8],[0,8]]), 88)
'''
#6th solution by ericlee
def max_sum(arr,ranges):
    return max([sum(arr[idx[0]:idx[1]+1]) for idx in ranges])

arr,ranges = [11,-22,31,34,-45,-46,35,32,21], [[1,4],[0,3],[6,8],[0,8]]
print(max_sum(arr,ranges))

#1st solution
def max_sum(arr, ranges):
    return max( sum(arr[start:stop+1]) for start, stop in ranges )

def max_sum(arr,ranges):
    return max(sum(arr[start:end+1]) for start, end in ranges)