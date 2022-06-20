'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1/?page=1&sortBy=submissions

11
1 3 5 8 9 2 6 7 6 8 9
Your Output:
1 1 3
2 4 9
2

Expected Output:
3
'''


class Solution:
    def minJumps(self, arr, n):

        if len(arr) <= 1:
            return 0

        # Return -1 if not possible to jump
        if arr[0] == 0:
            return -1

        # initialization
        maxReach = arr[0]
        step = arr[0]
        jump = 1

        # Start traversing array
        for i in range(1, len(arr)):

            # Check if we have reached the end of the array
            if i == len(arr) - 1:
                return jump

                # updating maxReach
            maxReach = max(maxReach, i + arr[i])

            # we use a step to get to the current index
            step -= 1

            # If no further steps left
            if step == 0:
                #  we must have used a jump
                jump += 1

                # Check if the current index/position  or lesser index
                # is the maximum reach point from the previous indexes
                if i >= maxReach:
                    return -1

                # re-initialize the steps to the amount
                # of steps to reach maxReach from position i.
                step = maxReach - i

        return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = ''.join([str(i) for i in arr])
print(arr)
#ob = Solution()
#ans = ob.minJumps(arr,len(arr))
#print(ans)
#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        #Arr = [int(x) for x in input().split()]
        Arr = [int(x) for x in str(T)]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends  13589267689



'''


class Solution:
	def minJumps(self, arr, n):
            step,s,ans = 1,int(arr[0]),''
            #idx = dict([(i,e) for i,e in enumerate(arr) if i + e == len(arr)])
            while step <= n:
                print(step,s,arr[s])
                if arr[s] == arr[-1]:
                    #ans += str(step)
                    return ans
                else:
                    s += int(arr[s])
                    step += 1
                    ans += str(step) + str(s) + str(arr[s]) + '\n'
                #break
'''