'''
https://www.codewars.com/kata/54f9cba3c417224c63000872/train/python

The Monty Hall problem is a probability puzzle base on the American TV show "Let's Make A Deal".

In this show, you would be presented with 3 doors: One with a prize behind it, and two without
(represented with goats).

After choosing a door, the host would open one of the other two doors which didn't include a
prize, and ask the participant if he or she wanted to switch to the third door. Most wouldn't.
One would think you have a fifty-fifty chance of winning after having been shown a false door,
however the math proves that you significantly increase your chances, from 1/3 to 2/3 by
switching.

Further information about this puzzle can be found on
https://en.wikipedia.org/wiki/Monty_Hall_problem.

In this program you are given an array of people who have all guessed on a door from 1-3,
as well as given the door which includes the price. You need to make every person switch to
the other door, and increase their chances of winning. Return the win percentage
(as a rounded int) of all participants.

蒙蒂-霍尔问题是以美国电视节目《我们来做个交易》为基础的概率难题。

在这个节目中，你会看到3扇门。一扇门后面有奖，两扇门没有奖（用山羊代表）。

选择一扇门后，主持人会打开另外两扇不含奖品的门中的一扇，问参与者是否想换到第三扇门。大多数人不会。
人们会认为在被展示了一扇假门之后，你有五成的胜算，然而数学证明，通过转换，你的胜算会大大增加，从1/3增加到2/3。

更多关于这个谜题的信息可以在https://en.wikipedia.org/wiki/Monty_Hall_problem。

在这个程序中，您将会得到一系列的人，他们都猜中了一扇门，从1-3到1-3，同时您还会得到一扇门，
其中包括价格。你需要让每个人都换到另一扇门上，并增加他们的获胜机会。返回所有参与者的胜率（为四舍五入的int）。

test.assert_equals(monty_hall(1, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 71)
test.assert_equals(monty_hall(2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 64)
test.assert_equals(monty_hall(3, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]), 64)

s = [1,2,3].remove(1)
print(s)
print([1,2,3].remove(1))
print(random.choices([1,2,3].remove(1)))
'''
#5th
import random
def monty_hall(correct_door_number, participant_guesses):
    return round([random.choices([i for i in [1,2,3] if i != correct_door_number]) if i == correct_door_number else correct_door_number for i in participant_guesses].count(correct_door_number)/len(participant_guesses),2)
correct_door_number, participant_guesses = 1, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]

print(monty_hall(correct_door_number, participant_guesses))


#1st
def monty_hall(door, guesses):
    return round(100.0 * (len(guesses)-guesses.count(door))/len(guesses))

#2nd
def monty_hall(c, p):
    print(c, p)
    return round((1 - (p.count(c) / len(p))) * 100)

#3rd
def monty_hall(correct_door_number, participant_guesses):
    winners=0
    for x in participant_guesses:
        if x != correct_door_number:
            winners+=1
    return(round((winners / len(participant_guesses))*100))

#4th
def monty_hall(correct, guesses):
    return round(100-100.0*guesses.count(correct)/len(guesses))

#5th
def monty_hall(d, g):
    return round((len(g)-g.count(d))/len(g)*100)