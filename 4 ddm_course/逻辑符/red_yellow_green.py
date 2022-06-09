# STEM page 63
# 0 stand for power_off,1 stand for power_on

red,yellow,green = 1,0,0
def shift_a(red,yellow,green):
    if red == 1:
        red,green = 0,1

    elif green == 1:
        green,yellow = 0,1

    elif yellow == 1:
        yellow,green = 0,1
    return red, yellow, green
    #return "red:"+f"{red}","yellow:"+f"{yellow}","green:"+f"{green}"

def shift_b(red,yellow,green):
    if yellow == 1:
        yellow,green = 0,1
    else:
        pass
    return "red:"+f"{red}","yellow:"+f"{yellow}","green:"+f"{green}"

print(shift_a(red,yellow,green))


for _ in range(6):
    status = shift_a(red,yellow,green)
    red, yellow, green = status
    print(status)
status = shift_a(red,yellow,green)
print("red:"+f"{red}","yellow:"+f"{yellow}","green:"+f"{green}")


