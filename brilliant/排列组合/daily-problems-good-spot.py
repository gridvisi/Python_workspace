'''
https://brilliant.org/daily-problems/good-spot/

Ada, Bella, Colette, and Delia are about to stand in a row, and Bella and
Colette want to stand next to each other. What fraction of all possible
configurations would satisfy their wish
'''

arr = ['Ada', 'Bella', 'Colette', 'Delia']
print(('Ada', 'Bella', 'Colette', 'Delia').index('Bella'))
from itertools import permutations

arrs = list(permutations(arr,len(arr)))
print(arrs)
ans = []
for line in arrs:
    print(line.index('Bella'),line.index('Colette'))
    if abs(line.index('Bella') - line.index('Colette'))==1:

        ans.append(line)
print(len(ans),ans)


#2nd solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rv = []
        for i in range(len(nums)):
            self.help(nums, i, [], rv)
        return rv

    def help(self, nums, i, path, rv):
        path.append(nums[i])
        if len(nums) == 1:
            rv.append(path)
            return

        sub_nums = nums[0:i] + nums[i + 1:]
        for i in range(len(sub_nums)):
            self.help(sub_nums, i, path + [], rv)