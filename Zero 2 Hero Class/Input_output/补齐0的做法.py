from time import *
if not isinstance(dTime, datetime):
    raise ValueError("not isinstance(dTime, datetime)")
sYMD = dTime.strftime("%Y-%m-%d")
s = '{0:0>2}'.format(dTime.minute)
sMinute = "%d:%s:00" % (dTime.hour, s,)