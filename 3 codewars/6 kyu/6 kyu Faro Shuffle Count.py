'''
https://www.codewars.com/kata/faro-shuffle-count/train/python
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six']  gives
['ace', 'four', 'two', 'five', 'three', 'six' ]
If 8 perfect faro shuffles are performed on a deck of 52 playing cards, the deck is restored to its original order.
Write a function that inputs an integer n and returns an integer representing the number of faro shuffles it takes to restore a deck of n cards to its original order.
Assume n is an even number between 2 and 2000.
FUNDAMENTALSLISTSDATA STRUCTURESITERATORSCONTROL FLOWOBJECT-ORIENTED PROGRAMMINGBASIC LANGUAGE FEATURES
'''

def faro_cycles(n):
    x, cnt = 2, 1
    while x != 1 and n > 3:
        cnt += 1
        x = x*2 % (n-1)
    return cnt
n = 52
print(faro_cycles(n))
print([0,2,4] + [1,3,5])

print(list(range(6)))

def faro_cycles(deck_size):
    arr, count = list(range(deck_size)), 0
    original_arr = arr
    while True:
        arr = arr[0:deck_size:2] + arr[1:deck_size:2]
        count += 1
        if original_arr == arr:
            break
    return count
print(faro_cycles(52))