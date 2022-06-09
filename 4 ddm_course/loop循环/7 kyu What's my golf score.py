'''
I have the par value for each hole on a golf course and my stroke score on each hole. I have them stored as strings, because I wrote them down on a sheet of paper. Right now, I'm using those strings to calculate my golf score by hand: take the difference between my actual score and the par of the hole, and add up the results for all 18 holes.

For example:

If I took 7 shots on a hole where the par was 5, my score would be: 7 - 5 = 2
If I got a hole-in-one where the par was 4, my score would be: 1 - 4 = -3.
Doing all this math by hand is really hard! Can you help make my life easier?

Task Overview
Complete the function which accepts two strings and calculates the golf score of a game. Both strings will be of length 18, and each character in the string will be a number between 1 and 9 inclusive.

FUNDAMENTALSSTRINGSARRAYSNUMBERSINTEGERSLOOPSCONTROL FLOWBASIC LANGUAGE FEATURESCONDITIONAL STATEMENTS

'''

def golf_score_calculator(par_string, score_string):
    return sum([int(x) - int(y) for x,y in zip(score_string,par_string)])

#list(map(lambda x,y:[int(x) - int(y) for x,y in (score_string,par_string)]))

par_string, score_string ='443454444344544443', '353445334534445344'

print(golf_score_calculator(par_string, score_string))

#1st solution
def golf_score_calculator(par, score):
    return sum(int(b) - int(a) for a, b in zip(par, score))

#2nd solution
def golf_score_calculator(par, score):
    return sum(map(int, score)) - sum(map(int, par))