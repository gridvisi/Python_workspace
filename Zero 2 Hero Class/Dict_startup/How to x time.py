
'''
how to stop time: kiss
how to travel in time : read
how to escape time :music
how to feel time: write
how to release time: breath
'''

def x_time(act):
    a = ['stop','travel in','escape','feel','release']
    b = ['kiss','read','music','write','breath']
    return f"how to {act} time : {dict(zip(a,b))[act]}"
act = 'escape'
print(x_time(act))