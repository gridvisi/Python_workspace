def special_number(number):
    number = str(number)
    number = list(number)
    for i in range(len(number)-1,-1,-1):
        if int(number[i]) > 5:
            return "NOT!!"
    return "Special!!"
print(special_number(39))