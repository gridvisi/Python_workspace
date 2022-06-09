'''
You have an 8-wind compass, like this:

You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise, and negative means counter-clockwise.

Return the direction you will face after the turn.

Examples
"S",  180  -->  "N"
"SE", -45  -->  "E"
"W",  495  -->  "NE"


'''

def direction(facing, turn):
    # your smart code here
    news = {"E":0,"NE":45,"N":90,"NW":135,"W":180,
            "SW":225,"S":270,"SE":315}
    for k,v in news.items():
        if facing == k:
            vt = (v - turn)%360

    return [k for k,v in news.items() if v==vt][0]

facing, turn = "S", 180
print(direction(facing, turn))


DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


def direction(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]