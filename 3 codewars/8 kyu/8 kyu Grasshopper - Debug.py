'''
https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/python

Debug celsius converter
Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.
Find the errors in the code to get the celsius converter working properly.
To convert fahrenheit to celsius:
celsius = (fahrenheit - 32) * (5/9)
Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.
调试摄氏度转换器
你的朋友要出国去美国旅行，所以他写了一个程序来将华氏度转换为摄氏度。不幸的是，他的代码有一些错误。
找出代码中的错误，让摄氏度转换器正常工作。
将华氏度转换为摄氏度。
摄氏度 = (华氏 - 32) * (5/9)
请记住，通常当前天气条件下的温度是以整数给出的。温度传感器有可能以更高的精度报告温度，
例如精确到最近的十分之一。但仪器误差使得这种精度对许多类型的温度测量传感器来说都不可靠。
'''

print(round(1/3,1))


def weather_info(temp):
    c: convert(temp)
    if (c > 0):
        return (c + " is freezing temperature")
    else:
        return (c + " is above freezing temperature")

def convertToCelsius(temperature):
    #var
    celsius = (temperature) - 32 + (5 / 9)
    return temperature
