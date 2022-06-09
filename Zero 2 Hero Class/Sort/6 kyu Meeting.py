'''
https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python

John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a
guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
'''
print(sorted([('STAN', 'VICTORIA'),('SCHWARZ', 'ALEX')]))


l = [('STAN', 'MADISON'),('SCHWARZ', 'VICTORIA'),('STAN', 'MEGAN'),('WAHL', 'ALEXIS')]
l.sort()
print(l)

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

s = "AXEX:ADA;Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
def meeting(s):
    s = sorted([tuple(name.split(":")[::-1]) for name in s.split(';')])
    return '(' + ')('.join([(', '.join(name)).upper() for name in s]) + ')'

#[n[0]+n[1] for n in ''.join(str(sorted(s)))]
print(meeting(s))

'''
Testing:
Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn
ACTUAL =
(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(STAN, MADISON)(SCHWARZ, VICTORIA)(STAN, MEGAN)(WAHL, ALEXIS)
EXPECT =
(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)
False


Testing:
Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn
ACTUAL =
(WAHL,ALEXIS)(BELL,JOHN)(SCHWARZ,VICTORIA)(DORNY,ABBA)(META,GRACE)(ARNO,ANN)(STAN,MADISON)(CORNWELL,ALEX)(KERN,LEWIS)(STAN,MEGAN)(KORN,ALEX)
EXPECT =
(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)
False




# Fails try paste
def meeting(s):
    temp,res,re = [],[],[]
    sup = s.upper().split(';')
    for i in sup:
        temp.append(i.split(':'))
    for i, e in enumerate(temp):
        res.append((e[1], e[0]))
    s = sorted(res)
    for i in s:
        re.append(','.join(i))
    return "(" + ')('.join(re) + ")"c

'''