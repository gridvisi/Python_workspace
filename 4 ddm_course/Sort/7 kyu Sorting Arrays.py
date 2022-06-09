'''
https://www.codewars.com/kata/57fe864854685b1c420002e0/train/javascript

var a1 = ['giraffe', 'orangutan', 'impala', 'elephant', 'rhino'];
var a2 = ['rattlesnake', 'eagle', 'geko', 'iguana', 'octopus'];

returns ['geko', 'octopus', 'iguana', 'eagle', 'rattlesnake']
'''

arr1 = ['giraffe', 'orangutan', 'impala', 'elephant', 'rhino']
arr2 = ['rattlesnake', 'eagle', 'geko', 'iguana', 'octopus']

def sortFirst(arr1,arr2):
    ans = []
    for i in arr1:
        for j in arr2:
            if i[0] == j[0]:
                ans.append(j)
    return ans
print(sortFirst(arr1,arr2))

