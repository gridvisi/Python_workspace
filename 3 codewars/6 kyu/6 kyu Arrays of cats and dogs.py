'''
https://www.codewars.com/kata/5a5f48f2880385daac00006c/train/python

solve(['D','C','C','D','C'], 2) = 2, because the dog at index 0 (D0) catches C1 and D3 catches C4.
solve(['C','C','D','D','C','D'], 2) = 3, because D2 catches C0, D3 catches C1 and D5 catches C4.
solve(['C','C','D','D','C','D'], 1) = 2, because D2 catches C1, D3 catches C4. C0 cannot be caught because n == 1.
solve(['D','C','D','D','C'], 1) = 2, too many dogs, so all cats get caught!


'''
arr,n = ['C','C','D','D','C','D'], 2  # = 3
def solve(arr,n):
