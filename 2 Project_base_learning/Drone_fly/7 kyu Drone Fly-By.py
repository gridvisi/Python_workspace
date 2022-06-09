'''
https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python

有一天，我看到一个惊人的视频，一个人通过驾驶无人机飞过一些wifi控制的灯泡，黑掉了这些灯泡。很精彩。

在这个卡塔中，我们将重现这个特技......有点像。

你将得到两个字符串：灯和无人机。灯代表一排灯，目前是关闭的，每个灯都用x表示，当这些灯打开时，
它们应该用o表示。

无人机字符串表示无人机的位置T(有什么更好的建议吗？)和它到此为止的飞行路径=。无人机总是从左到
右飞行，并且总是从这排灯的起点开始。无人机飞过的任何地方，包括它现在的位置，都会导致该位置的灯打开。

返回结果灯的字符串。更清楚的内容请看测试示例。

基本原理字符串阵列
'''


def fly_by(lamps, drone):
    return min(len(drone),len(lamps))*"o"+lamps[len(drone):]

lamps, drone = "xx","==T"
print(fly_by(lamps, drone))


def fly_by(lamps, drone):
    return lamps.replace('x', 'o', drone.count('=') + 1)

def fly_by(lamps, drone):
    l = len(lamps)
    d = len(drone)
    if d >= l:
        return 'o'* l
    return ('o' * d) + ('x' * (l - d))

def fly_by(lamps, drone):
    on = drone.find("T") + 1
    return lamps.replace("x", "o", on)