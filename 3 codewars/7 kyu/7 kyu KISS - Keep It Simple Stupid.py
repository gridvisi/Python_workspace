
'''
https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1/train/python
KISS stands for Keep It Simple Stupid. It is a design principle for keeping things simple rather than complex.
You are the boss of Joe.
Joe is submitting words to you to publish to a blog. He likes to complicate things.
Define a function that determines if Joe's work is simple or complex.
Input will be non emtpy strings with no punctuation.
It is simple if: the length of each word does not exceed the amount of words in the string (See example test cases)

Otherwise it is complex.
KISS是Keep It Simple Stupid的缩写。这是一个保持事物简单而不是复杂的设计原则。
你是乔的老板。
乔是向你提交文字，让你把文字发布到博客上。他喜欢把事情复杂化。
定义一个函数来决定Joe的工作是简单还是复杂。
输入将是没有标点符号的非 emtpy 字符串。
如果：每个单词的长度不超过字符串中的单词数，则为简单。否则很复杂。

test.describe('word count: 5')
test.assert_equals(is_kiss('Joe had a bad day'), "Good work Joe!")
test.assert_equals(is_kiss('Joe had some bad days'), "Good work Joe!")
test.assert_equals(is_kiss('Joe is having no fun'), "Keep It Simple Stupid")
test.assert_equals(is_kiss('Sometimes joe cries for hours'), "Keep It Simple Stupid")
'''
words = 'Sometimes joe cries for hours'
print(''.split(words))
def is_kiss(words):
    if max([len(w) for w in words.split(' ')]) > len(words.split(' ')):
        return "Keep It Simple Stupid"

    else:
        return "Good work Joe!"
print(is_kiss(words))