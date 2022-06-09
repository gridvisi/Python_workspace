'''
https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

test.assert_equals(areYouPlayingBanjo("martin"), "martin does not play banjo");
test.assert_equals(areYouPlayingBanjo("Rikke"), "Rikke plays banjo");

name + " plays banjo"
name + " does not play banjo"
'''

def areYouPlayingBanjo(name):
    # Implement me!
    return f"{name}"+" plays banjo" if name[0].lower() == 'r' else f"{name}"+" does not play banjo"

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)


def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

def areYouPlayingBanjo(name):
    if name[0] == 'r' or name[0] =='R':
        return ("%s plays banjo"%name)
    else:
        return ("%s does not play banjo"%name)