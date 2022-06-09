def format_duration(seconds):
    secstr = ''
    minstr = ''
    houstr = ''
    if not seconds:
        return "now"
    if seconds % 60 == 1:
        secstr = str(seconds % 60) + " second"
    elif seconds % 60 > 1:
        secstr = str(seconds % 60) + " seconds"
    if int(seconds / 60 % 60) == 1:
        minstr = str(int(seconds / 60 % 60)) + " minute"
    elif int(seconds / 60 % 60) > 1:
        minstr = str(int(seconds / 60 % 60)) + " minutes"
    if int(seconds / 3600) == 1:
        houstr = str(int(seconds / 3600)) + " hour"
    elif int(seconds / 3600) > 1:
        houstr = str(int(seconds / 3600)) + " hours"
    if not houstr and not minstr:
        return secstr
    elif not houstr and not secstr:
        return minstr
    elif not minstr and not secstr:
        return houstr
    elif not houstr:
        return minstr + " and " + secstr
    elif not minstr:
        return houstr + " and " + secstr
    elif not secstr:
        return houstr + " and " + minstr
    else:
        return houstr + ", "+ minstr +" and "+secstr

print(format_duration(3662))