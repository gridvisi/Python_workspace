
'''
https://www.codewars.com/kata/v-a-p-o-r-c-o-d-e/train/python
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())
'''
s = "Lets go to the movies"
print()
def vaporcode(s):
    ls = [i + '  ' for i in s.upper() if i != ' ']
    return ''.join(ls).strip(' ')
print(vaporcode(s))

def vaporcode(s):
    return "  ".join(s.replace(" ", "").upper())