'''
https://brilliant.org/daily-problems/taxicab-distance-1/
'''

def roadmap(start:list,end:list,map=[]):
    x,y = start[-1]
    map.append(start)
    while x < end[0] and y < end[1]:
        if x+1 <= end[0] and y < end[1]:
            start.append([x+1,y])
            #map.append(roadmap(start, end, map))
            return roadmap(start, end, map)

        if x <= end[0] and y+1 < end[1]:
            start.append([x, y+1])
            #map.append(roadmap(start, end, map))
            return roadmap(start, end, map)
    return start,map

start,end = [[0,0]],[3,3]
print(roadmap(start,end,map=[]))