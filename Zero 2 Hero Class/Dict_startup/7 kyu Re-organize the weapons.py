'''
https://www.codewars.com/kata/5470ae03304c1250b4000e57/train/python

test.assert_equals(identify_weapon("Laval"), "Laval-Shado Valious")
test.assert_equals(identify_weapon("Tormak"), "Tormak-Tygafyre")
test.assert_equals(identify_weapon("G'loona"), "Not a character")
'''
inp = "Laval-Shado Valious,Cragger-Vengdualize,Lagravis-Blazeprowlor,Crominus-Grandorius,Tormak-Tygafyre,LiElla-Roarburn."

inp = inp[:-1].split(",")
print([w.split("-") for w in inp])
print(dict([w.split("-") for w in inp]))


def identify_weapon(character):
    inp = "Laval-Shado Valious,Cragger-Vengdualize,Lagravis-Blazeprowlor,Crominus-Grandorius,Tormak-Tygafyre,LiElla-Roarburn."
    exp = dict([w.split("-") for w in inp[:-1].split(",")])
    return character+'-'+exp.get(character,"Not a character")


#1st
def identify_weapon(character):
    tbl = {
        "Laval": "Laval-Shado Valious",
        "Cragger": "Cragger-Vengdualize",
        "Lagravis": "Lagravis-Blazeprowlor",
        "Crominus": "Crominus-Grandorius",
        "Tormak": "Tormak-Tygafyre",
        "LiElla": "LiElla-Roarburn"
    }

    return tbl.get(character, "Not a character")

family = ['father','mother','brother','sister'] #list
ages = [70,68,45,40]
print(dict(zip(family,ages)))
gender = {'male','female'}

s = 'abc' #str
print(list(s))

print(str(123) == 123, eval(str(123)) + 123)
print(str(123) == 123, int(str(123)) + 123) #integer
print(7/4 , 7//4 , int(7/4), 7%4)



