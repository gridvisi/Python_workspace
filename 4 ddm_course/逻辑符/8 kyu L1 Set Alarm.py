'''
def set_alarm(employed, vacation):
    # Your code here

写一个名为setAlarm的函数，它接收两个参数。第一个参数，employed，只要你有工作就为真，
第二个参数，vacation，只要你在休假就为真。

如果你有工作而不是在休假，函数应该返回true（因为这些情况下你需要设置一个警报）。
否则应该返回false。示例。

setalarm(true, true) -> false
setalarm(false, true) -> false
setalarm(false, false) -> false
setalarm(true, false) -> true
'''

def set_alarm(employed, vacation):
    return False if employed == False or vacation == True else True

employed, vacation = 'true', 'true'
print(set_alarm(employed, vacation))

#1st solution
def set_alarm(employed, vacation):
    return employed and not vacation

def set_alarm(employed, vacation):
    return employed==True and vacation==False

def set_alarm(a, b):
    return a - b == 1

def set_alarm(employed, vacation):
    return employed > vacation