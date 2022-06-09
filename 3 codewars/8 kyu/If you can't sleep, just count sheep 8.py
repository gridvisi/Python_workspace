def count_sheep(n):
    output = ""
    for i in range(1,n+1):
        output += str(i)+" sheep..."
    return output
print(count_sheep(4))