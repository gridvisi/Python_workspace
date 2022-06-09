def make_readable(seconds):
    h = 0
    m = 0
    s = 0
    output = []
    while seconds:
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        seconds -= 1
    if int(h / 10) == 0:
        h = '0'+str(h)+':'
    else:
        h = str(h)+':'
    if int(m /10) == 0:
        m = '0' + str(m) + ':'
    else:
        m = str(m) + ':'
    if int(s /10) == 0:
        s = '0' + str(s)
    else:
        s = str(s)
    output = [h,m,s]
    output = ''.join(output)
    return output
    #return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
print(make_readable(359999))
