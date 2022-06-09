# https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python
# https://blog.csdn.net/brucewong0516/article/details/82701561?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
text = "sense Does to That Make you?"
text = "hey You, Sort me !Already!"
def capitals_first(text):
    cap = [w for w in text.split() if w[0].istitle()]
    low = [w for w in text.split() if w[0].islower()]

    return ' '.join(cap+low)

print(capitals_first(text))

print('&%$!1Her'[0].istitle())
print('&%$!1Her'.istitle())

'''
# s 代表字符串
s.isalnum() #所有字符都是数字或者字母
s.isalpha() #所有字符都是字母
s.isdigit() #所有字符都是数字
s.islower() #所有字符都是小写
s.isupper() #所有字符都是大写
s.istitle() #所有单词都是首字母大写，像标题
s.isspace() #所有字符都是空白字符、\t、\n

   cap = sorted(''.join(w) for w in (text.split(' ')) if w[0].isupper())
    print(text)
    low = sorted(''.join(w) for w in (text.split(' ')) if w[0].lower())
    return cap,low,' '.join(sorted(text.split(' '),reverse = True))
'''
#ap = sorted([w if w[0].isupper()==True else w for w in (text.split(' '))],reverse=True)