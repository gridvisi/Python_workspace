
s = 4898
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

'''

def make_readable(s):
    return f'{}:{:02}:{:02}'%(s / 3600, s / 60 % 60, s % 60)
'''


print(make_readable(s))

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

print(make_readable(s))
