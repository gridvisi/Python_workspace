def areYouPlayingBanjo(name):
    name = list(name)
    if name[0] == 'r' or name[0] == 'R':
        name = ''.join(name)
        return name+" plays banjo"
    else:
        name = ''.join(name)
        return name + " does not play banjo"
print(areYouPlayingBanjo("Rii"))