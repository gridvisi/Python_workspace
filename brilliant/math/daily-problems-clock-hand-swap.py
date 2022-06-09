# https://brilliant.org/daily-problems/clock-hand-swap/
'''
Ivan left his house to meet up with a friend between 3 p.m.
and 4 p.m. When he returned between 7p.m. and 8 p.m.,
he noticed that the minute and hour hands of his kitchen clock
swapped places while he was gone.


round = 360
one hour = 360/12 = 30
one minute = 360/12/60 = 0.5
one second = 360/12/60/60 = 1/120
'''
#we could focus
#Time of go out 3:35-3:40
#Time of return 7:15-8:20

start_h_angel = [3*30 + 30*(s//3600) for s in range(3600)]
start_m_angel =
# 3:00-4:00pm
end_angel = [7*30 + 30*(s//360) for s in range(3600)]
# 7:00-8:00pm