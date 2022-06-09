import string
str = "the quick brown fox jumps over a lazy dog"
alpha = string.ascii_letters[:26] + " "
print(" " in alpha)
res = [e for e in alpha if e not in str]
print(res,res == [])

'''
for e in alpha:
    #print(e)
    if e in str.lower():
        print('-')
    elif e not in str:
        print(e)
'''



str,name = "Just enough nice friends","Jennifer"
#str,name = "A crew that boards the ship", "chris"
#str,name = "A live son", "Allison"
#str,name = "Just enough nice friends","Jennifer"
#str,name = "pippippi","Pippi"
#str,name = "Across the rivers","chris"
def name_in_str(str, name):
    it = iter(str.lower())

    return all(c in it for c in name.lower())
print(name_in_str(str, name))

'''
 print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
'''