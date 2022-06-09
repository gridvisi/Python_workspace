'''
https://www.codewars.com/kata/56f6919a6b88de18ff000b36/train/python
你的朋友出去买小狗了（真是生不逢时啊！）......。他带着多只狗回来了，
而你根本不知道该如何回应!

通过修复所提供的功能，你会发现，根据他的狗的数量，你到底应该如何回应。

狗的数量将永远是一个数字，而且总是至少有1条狗。

["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101
'''

#Need to modify code:
#def how_many_dalmatians(n):
#    dogs["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
#    respond =
#    if number <= 10 then  dogs[0] else if (number <= 50 then dogs[1] else (number = 101  dogs[3] else dogs[2]
#return respond

def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    respond = dogs[0] if n <= 10 else dogs[1] if n <= 50 else dogs[3] if n == 101 else dogs[2]
    return respond