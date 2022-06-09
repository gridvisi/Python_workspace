'''
https://www.codewars.com/kata/5888a57cbf87c25c840000c6/train/python

Were you ever interested in the phenomena of astrology, star signs, tarot, voodoo ? (ok not voodoo that's too spooky)...
Task:
Your job for today is to finish the star_sign function by finding the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs vary on different resources so we will use this table to get consistent results:

Aquarius ------ 21 January - 19 February
Pisces --------- 20 February - 20 March
Aries ---------- 21 March - 20 April
Taurus -------- 21 April - 21 May
Gemini -------- 22 May - 21 June
Cancer -------- 22 June - 22 July
Leo ------------- 23 July - 23 August
Virgo ----------- 24 August - 23 September
Libra ----------- 24 September - 23 October
Scorpio -------- 24 October - 22 November
Sagittarius ---- 23 November - 21 December
Capricorn ----- 22 December - 20 January

Test info: 100 random tests (dates range from January 1st 1940 until now)
'''
#处理字符串里的 "---"
inp = '''
Aquarius ------ 21 January - 19 February
Pisces --------- 20 February - 20 March
Aries ---------- 21 March - 20 April
Taurus -------- 21 April - 21 May
Gemini -------- 22 May - 21 June
Cancer -------- 22 June - 22 July
Leo ------------- 23 July - 23 August
Virgo ----------- 24 August - 23 September
Libra ----------- 24 September - 23 October
Scorpio -------- 24 October - 22 November
Sagittarius ---- 23 November - 21 December
Capricorn ----- 22 December - 20 January
'''
import datetime

#Aquarius = [datetime.date(2021, m, n) for m in (1,3) for n in ()

from datetime import date
def star_sign(day):
    limits = ['', 20, 19, 20, 20, 21, 21, 22, 23, 23, 23, 22, 21]
    #d = datetime.datetime(day)
    print('d',d)
    signs = ['Aquarius', 'Pisces', 'Aries',
             'Taurus', 'Gemini', 'Cancer',
             'Leo', 'Virgo', 'Libra', 'Scorpio',
             'Sagittarius', 'Capricorn']

    if d.day > limits[d.month]:
        print(d.month - 1)
        return signs[d.month - 1]
    else:
        return signs[d.month - 2]

d = datetime.datetime(2000, 2, 15)
d = date(2000, 2, 15)
day = date(2000, 2, 15)
print(d)
print(print(d.month, d.day))

signs = ['Aquarius', 'Pisces', 'Aries',
             'Taurus', 'Gemini', 'Cancer',
             'Leo', 'Virgo', 'Libra', 'Scorpio',
             'Sagittarius', 'Capricorn']
print(d.month - 1,signs[d.month - 1])
print(type(d.month), type(d.day))
print('result：',star_sign(date))

#2nd
from datetime import date
def star_sign(d):
    m=d.month-1; d=d.day
    if m==2: s=('Pisces','Aries')[d>20]
    elif m==3: s=('Aries','Taurus')[d>20]
    elif m==4: s=('Taurus','Gemini')[d>21]
    elif m==5: s=('Gemini','Cancer')[d>21]
    elif m==6: s=('Cancer','Leo')[d>22]
    elif m==7: s=('Leo','Virgo')[d>23]
    elif m==8: s=('Virgo','Libra')[d>23]
    elif m==9: s=('Libra','Scorpio')[d>23]
    elif m==10: s=('Scorpio','Sagittarius')[d>22]
    elif m==11: s=('Sagittarius','Capricorn')[d>21]
    elif m==1: s=('Aquarius','Pisces')[d>19]
    else: s=('Capricorn','Aquarius')[d>20]
    return s

#3rd
month_rules = {
    1:  (21, "Capricorn"),
    2:  (20, "Aquarius"),
    3:  (21, "Pisces"),
    4:  (21, "Aries"),
    5:  (22, "Taurus"),
    6:  (22, "Gemini"),
    7:  (23, "Cancer"),
    8:  (24, "Leo"),
    9:  (24, "Virgo"),
    10: (24, "Libra"),
    11: (23, "Scorpio"),
    12: (22, "Sagittarius"),
    13: ("", "Capricorn")
}
def star_sign(date):
    (split_day, sign) = month_rules[date.month]
    return sign if date.day < split_day else month_rules[date.month + 1][1]



#5
from datetime import datetime

signs = (
    ('Capricorn',   22), # 22 December  - 20 January
    ('Aquarius',    21), # 21 January   - 19 February
    ('Pisces',      20), # 20 February  - 20 March
    ('Aries',       21), # 21 March     - 20 April
    ('Taurus',      21), # 21 April     - 21 May
    ('Gemini',      22), # 22 May       - 21 June
    ('Cancer',      22), # 22 June      - 22 July
    ('Leo',         23), # 23 July      - 23 August
    ('Virgo',       24), # 24 August    - 23 September
    ('Libra',       24), # 24 September - 23 October
    ('Scorpio',     24), # 24 October   - 22 November
    ('Sagittarius', 23)  # 23 November  - 21 December
)

def star_sign(date):
    sign, limit = signs[date.month % 12]
    return signs[date.month - 1][0] if date.day < limit else sign


# try？
import dateparser
def star_sign(date):
    # your code here
    pass