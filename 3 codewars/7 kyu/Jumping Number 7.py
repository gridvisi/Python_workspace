#url
#https://www.codewars.com/kata/jumping-number-special-numbers-series-number-4/train/python
def jumping_number(number):
    if not number // 10: return "Jumping!!"
    else:
        number = list(str(number))
        number.append(int(number[-1])+1)
        for i in range(0,len(number)-1):
            if not int(number[i]) + 1 == int(number[i+1]):
                if not int(number[i]) - 1 == int(number[i+1]):
                    return "Not!!"
        return "Jumping!!"
print(jumping_number(23))