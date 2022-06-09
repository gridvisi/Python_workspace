
inputStr = 'i love python'
def getCount(inputStr):
    num_vowels = 0
    for vowels in inputStr:
        num_vowels = vowels.count(vowels)
        num_vowels = num_vowels+1
        #continue
    return num_vowels

print(getCount("a, e, i, o, u"))

'''
Post this in the kata section please, and mark it with a spoiler tag. 
Don't print the result after returning.

请将此贴在“卡塔”部分，并用扰流器标记。返回后不要打印结果。
'''