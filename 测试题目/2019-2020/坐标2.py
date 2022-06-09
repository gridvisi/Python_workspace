__author__ = 'Administrator'
import numpy as np
a=np.arange(9).reshape(3,3)
print(a)
print('out:',a[1])
print('out:',a[:,1])
print('out:',a[0,0])
'''
Out[31]:
array([[0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]])

'''
'''
from math import cos, sin, atan2, sqrt, pi ,radians, degrees

def center_geolocation(geolocations):

    x = 0
    y = 0
    z = 0
    lenth = len(geolocations)
    for lon, lat in geolocations:
        lon = radians(float(lon))
        lat = radians(float(lat))

        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / lenth)
    y = float(y / lenth)
    z = float(z / lenth)

    return (degrees(atan2(y, x)), degrees(atan2(z, sqrt(x * x + y * y))))
if __name__ == '__main__':

    locations = [[116.568627,39.994879],[116.564791,39.990511],[116.575012,39.984311]]
'''
