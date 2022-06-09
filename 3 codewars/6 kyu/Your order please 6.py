def zeros(n):
    temp = 1
    for i in range(1,n+1):
        temp *= i
    temp = str(temp)
    temp = list(temp)
    output = 0
    i = len(temp)-1
    while True:
        if temp[i] != 0:
            print(output)
        elif temp[i] == 0:
            output+=1
        i-=1

print(zeros(30))