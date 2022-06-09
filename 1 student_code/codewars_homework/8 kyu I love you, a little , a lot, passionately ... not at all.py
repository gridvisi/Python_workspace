'''
https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python

Who remembers back to their time in the schoolyard, when girls
would take a flower and tear its petals, saying each of the
following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement,
dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls
would say for a flower of a given number of petals, where
nb_petals > 0.

谁还记得在学校操场上的时候，女孩们会拿着一朵花，撕开它的花瓣，每撕开一片花瓣就说下面的每一句话。

我爱你
一点点
非常爱
热烈地
疯狂地
根本不爱
当最后一片花瓣被撕开时，有兴奋、梦想、澎湃的思想和情感的呐喊。

你在这个卡塔中的目标是确定女孩们会对一朵给定数量的花说哪句话，
其中nb_petals>0


'''
#petals 花瓣
def how_much_i_love_you(nb_petals):
    deep = ['I love you','a little','a lot',
            'passionately','madly','not at all']

    return deep[nb_petals % 6 - 1]

#
def how_much_i_love_you(nb_petals):
    # your code
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]

