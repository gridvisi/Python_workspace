def is_valid_IP(string):
    string = list(string)
    temp = []
    if len(string) < 7 or len(string) >15:
        return False
    for i in range(len(string)):
        if ord(str(string[i])) <46 or ord(str(string[i])) > 57:
            return False
    for i in range(1,len(string)):
        for j in range(0,string[i] == '.'):
            temp.append(string[i])
        
        temp = []

    return True

print(is_valid_IP('12.255.56.1'))
