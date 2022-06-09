'''
https://www.codewars.com/kata/5470ae03304c1250b4000e57/train/python

The characters of Chima need your help. Their weapons got mixed up! They need you to write a program that accepts the name of a character in Chima then tells which weapon he/she owns.

For example: for the character "Laval" your program should return the solution "Laval-Shado Valious"

You must complete the following character-weapon pairs:

Laval-Shado Valious,
Cragger-Vengdualize,
Lagravis-Blazeprowlor,
Crominus-Grandorius,
Tormak-Tygafyre,
LiElla-Roarburn.
Return "Not a character" for invalid inputs.
'''

def identify_weapon(character):
    s = ['Laval-Shado Valious',
          'Cragger-Vengdualize',
          'Lagravis-Blazeprowlor',
          'Crominus-Grandorius',
          'Tormak-Tygafyre',
          'LiElla-Roarburn']
    sdict = dict([c.split('-') for c in s])
    return f"{character}-{sdict.get(character,'Not a character')}"
            #注意f里面的含有空格的字符串用单引号
character = 'Cragger'
print(identify_weapon(character))

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

def identify_weapon(character):
    #insert your code here...FOR CHIMA!
    try:
        return character + "-" + {
        "Laval":"Shado Valious", "Cragger":"Vengdualize",
        "Lagravis":"Blazeprowlor","Crominus":"Grandorius",
        "Tormak":"Tygafyre", "LiElla":"Roarburn"
        }[character]
    except:
        return "Not a character"

