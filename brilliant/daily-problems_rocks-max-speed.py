'''
https://brilliant.org/daily-problems/rocks-max-speed/
'''


rock = 9
rock_weight = 1
mass_weight = 4 * rock_weight
throw = 9
speed = 1
depart_speed = 13
#since first throw hint mass_weight : rock_weigth = 8/4 + 1 : 1/4 = 12:1
#due to people increase 1 m/s while the first rock reach 12 times 1, so that
# depart_speed = 1 + 12 = 13 m/s, maintain constant depart_speed in every throw rock

for i in range(throw):
    speed += 13 * (1*rock_weight/((rock - i)*rock_weight + 4 * rock_weight))
print(speed)