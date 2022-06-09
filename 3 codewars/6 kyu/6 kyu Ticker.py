'''
https://www.codewars.com/kata/5a959662373c2e761d000183/train/python
当我们使用公共交通工具时，我们可以看到一个简单的显示器和一个自动售票器。它通常提供有关下一站和预期到达时间的信息。
让我们实现一个函数，它将返回一个文本块，显示在固定宽度的显示器上。该功能应以文字显示、宽度显示和勾号作为勾号器的一个步骤。
函数将被多次调用，tick参数不断递增。

一开始，显示器是空的。在第一步中，只有一个字符应该显示在最右边的位置，以此类推。当信息显示时，应将其逐字符显示到左侧位置，
并返回到显示的空白状态。在那个周期之后应该重新开始。
test.describe("Ticker")

test.it("Should be empty display as initial state")
test.assert_equals(ticker('Beautiful is better than ugly.', 10, 0), '          ')

test.it("Should show line from right side")
test.assert_equals(ticker('Beautiful is better than ugly.', 10, 5), '     Beaut')
test.assert_equals(ticker('Beautiful is better than ugly.', 10, 30), 'than ugly.')

test.it("Should fill window with spaces from right side")
test.assert_equals(ticker('Beautiful is better than ugly.', 10, 39), '.         ')

test.it("Should work in cycle")
test.assert_equals(ticker('Beautiful is better than ugly.', 10, 41), '         B')

'''
x = ['']*3
x = ['a','b']
print(x)
text, width, tick = 'Beautiful is better than ugly.', 10, 5
def ticker(text, width, tick):
    t,buff = list(text + ' '*width),['']*width
    st, cycle = tick % len(t),tick//len(text)
    buffer = t[st-width : st] if st >= width else [' ']*(width-st) + list(text[:st])
    return ''.join(buffer)
print(ticker(text, width, tick))

#https://blog.csdn.net/u013300049/article/details/79313979

import itertools
text, width, tick = 'Beautiful is better than ugly.', 10, 41
text = "重庆到北京 speed：350km/h   温度23度"
width,tick = 14,6
def ticker(text, width, tick):
    x = text + ' '*width
    re_text = itertools.cycle(x)
    #print(list(itertools.islice(re_text, 0, 45)))
    if tick < width:
        re = ' '* (width-tick) + x[:tick]
        return re
    re = list(itertools.islice(re_text, abs(tick-width), tick)) #if tick > width else
    return ''.join(re)

def ticker(text, width, tick):
    tick %= len(text) + width
    text = ' ' * width + text + ' ' * width
    return text[tick :  tick + width]

def ticker(text, width, tick):
    return ((' ' * width) + text + (' ' * width)) [tick % (len(text) + width):][:width]
print(ticker(text, width, tick))


#['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
#print(' '*(width//2) + text + ' '*(width//2))
#x = itertools.cycle(' '*(width//2) + text + ' '*(width//2))

'''
LED的宽度设为14，每个字占宽度为2位，两个字母占用1个位。text的第3个参数代表播放到第6个字符，举例与图片相符，
输出结果是播放到第6个字​
例如 text = "重庆到北京，speed：350km/h   温度"
width,tick = 14，6
显示：speed：350km/h
'''
text = "重庆到北京 speed：350km/h   温度23度"
width,tick = 14,6
#width,tick = 14,20
def ticker(text, width, tick):
    tick %= len(text) + width
    text = ' ' * width + text + ' ' * width
    return text[tick :  tick + width]

print(ticker(text, width, tick))

#sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
arr = [5, 3, 2, 8, 1, 4]
def sort_array(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    print(odds)
    return [x if x % 2 == 0 else odds for x in arr]
    #return [x if x%2==0 else odds.pop() for x in arr]
print(sort_array(arr))