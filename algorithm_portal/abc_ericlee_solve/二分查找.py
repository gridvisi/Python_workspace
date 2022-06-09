'''
cullinan-shenanigans-magic-camera

https://brilliant.org/problems/cullinan-shenanigans-magic-camera/
'''

search_minutes = 24*60
photos = 0
while search_minutes > 10:
    photos += 1
    search_minutes /= 2
print ("Pictures required:", photos)


#https://brilliant.org/problems/you-be-the-detective-1/?group=ayU0CkcMBBov&amp;ref_id=882524

from itertools import product
def possible(satvik,krishna,sharky):
    # Somebody had to do it
    if True not in (satvik,krishna,sharky):
        return False
    # Sharky can't be without Satvik
    if sharky and not satvik:
        return False
    # Krishna can't drive
    if krishna and not (satvik or sharky):
        return False
    return True
satvik_guilty = True
krishna_guilty = True
sharky_guilty = True
for satvik,krishna,sharky in product((True,False),repeat=3):
    if possible(satvik,krishna,sharky):
        if not satvik:
            satvik_guilty = False
        if not krishna:
            krishna_guilty = False
        if not sharky:
            sharky_guilty = False
if satvik_guilty:
    print("SATVIK: GUILTY")
if krishna_guilty:
    print("KRISHNA: GUILTY")
if sharky_guilty:
    print("SHARKY: GUILTY")
if True not in (satvik_guilty,krishna_guilty,sharky_guilty):
    print("You can't prove anything!")