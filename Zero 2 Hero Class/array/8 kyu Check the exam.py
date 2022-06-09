'''
https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python
第一个输入数组是考试正确答案的密钥，比如["a"、"a"、"b"、"d"]。第二个包含学生提交的答案。

两个数组不为空，长度相同。返回这个答案数组的得分，每一个正确答案给+4，每一个错误答案给-1，
每一个空白答案给+0，用一个空字符串表示（在C语言中使用空格字符）。

如果分数<0，返回0。

The first input array is the key to the correct answers to an exam,
like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this
array of answers, giving +4 for each correct answer, -1 for each incorrect answer,
and +0 for each blank answer, represented as an empty string (in C the space character
 is used).

If the score < 0, return 0.
'''


def check_exam(arr1, arr2):
    #ans = [x==y for x in arr1 for y in arr2]  Wrong
    #ans = [4*(x == y) if x == y and y != "" else -1 for x,y in zip(arr1,arr2)]
    ans = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i] and arr2[i] != "":
            ans += 4
        elif arr2[i] == "":
            ans += 0
        elif arr1[i] != arr2[i] and arr2[i] != "":
            ans -= 1
    return max([0,ans])
arr1, arr2 = ["a", "a", "c", "b"], ["a", "a", "b",  ""]
print(check_exam(arr1, arr2))

#1st solution
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))