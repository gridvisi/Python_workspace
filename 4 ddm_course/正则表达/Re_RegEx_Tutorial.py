
import re
Str = "we need to inform him with the latest information"

for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)

Str = "Sat, hat, mat, pat,sad"
allStr = re.findall("[shmp]at", Str)
for i in allStr:
    print(i)

Str = "sat, hat, mat, pat"
someStr = re.findall("[^h-m]at", Str)
for i in someStr:
    print(i)

import re
Food = "hat rat mat pat"
regex = re.compile("[r]at")
Food = regex.sub("food", Food)
print(Food)

randstr = "Here is Edureka"
print(re.search(r"Edureka", randstr))

randstr = "12345"
print("Matches: ", len(re.findall("d{3}", randstr)))


randstr = '''
You Never
Walk Alone
Liverpool FC
'''
print(randstr)
regex = re.compile("")
randstr = regex.sub(" ", randstr)
print(randstr)

import re
email = "ac@aol.com md@.com @seo.com dc@.com"
print("Email Matches: ", len(re.findall("[w._%+-]{1,20}@[w.-]{2,20}.[A-Za-z]{2,3}", email)))

import re

#w = [a - zA - Z0 - 9_]
phn = "412-555-1212"
if re.search("w{3}-w{3}-w{4}", phn):
    print("Valid phone number")

import urllib.request
from re import findall

url = '''<a href= http://www.summet.com/dmsi/html/codesamples/addresses.html">
http://www.summet.com/dmsi/html/codesamples/addresses.html</a>"
'''
response = urllib.request.urlopen(url)

html = response.read()

htmlStr = html.decode()

pdata = findall("(d{3}) d{3}-d{4}", htmlStr)

for item in pdata:
    print(item)


Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''
ages = re.findall(r'd{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*',Nameage)
print(ages,names)
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
print(ageDict)  #{'Janice': '22', 'Theon': '33', 'Gabriel': '44', 'Joey': '21'}

if re.search("inform","we need to inform him with the latest information"):
    print("There is inform")