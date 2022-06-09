'''
https://www.codewars.com/kata/whats-in-a-name/train/python
Test.assert_equals(name_in_str("Across the rivers", "chris"), True)
Test.assert_equals(name_in_str("Next to a lake", "chris"), False)
Test.assert_equals(name_in_str("Under a sea", "chris"), False)
Test.assert_equals(name_in_str("A crew that boards the ship", "chris"), False)

Test.assert_equals(name_in_str("thomas","Thomas"),True)
Test.assert_equals(name_in_str("pippippi","Pippi"),True)
'''
str = "A crew that boards the ship"
#str = "Just enough nice friends"
str = "Across the rivers"
str = "Next to a lake"
str = "Under a sea"
name = "chris"
#name = "Jennifer"


#str,name = "thomas","Thomas"

str,name = "A live son", "Allison"
str,name = "Just enough nice friends","Jennifer"
str,name = "pippippi","Pippi"
str,name = "Across the rivers","chris"
str,name = "A crew that boards the ship", "chris"
str,name = "thomas","Thomas"
str,name = "All the bees die on earth, we would die due to not enough food sustain the living","Albert Einstein"


def name_in_str(str, name):
    re,s = '',0
    for i,e in enumerate(str.lower()):
        if e == name[s].lower():
            re += e
            s += 1
            str = str[i+1:]
            #print(re,s)
            if len(re) == len(name) and not re == name.lower():
                return False
            elif len(re) == len(name) and re == name.lower():
                return True
            #if s == len(name) and not re == name.lower(): return False
            #elif s == len(name) and re == name.lower():return True
    print(':',re, s)
    return re == name.lower()

print(name_in_str(str, name))

def name_in_str(str, name):
    it = iter(str.lower())
    print('it:',list(it))
    return all(c in it for c in name.lower())
'''
            s += 1
            name = name[s:]
            str = str[i+1:]
            if s == len(name)-1:
                return re
'''

'''
            re += e
            print(re)
            j += 1
            if j == len(str):
                return re
            elif j < len(str):
                name_rec = name[j:]
                return name_in_str(str[i+1:], name[j:])

'''

'''

    re,s,res = [],0,str
    for j in name:
        for i,e in enumerate(str.lower()):
            if e == j:
                str = str[i+1:]
                name = name[s+1:]
                print(str,i,name,re)
                #if e not in re:
                re.append(e)
    return re,res
'''
'''
    j,re = 0,''
    while j < len(name):
        for i,e in enumerate(str):
            if e == name[j]:
                re += e
                str = str[i + 1:]
                name = name[j:]
                print(str,name,re)
            #else:return False
        j += 1
    return re == name,re

'''