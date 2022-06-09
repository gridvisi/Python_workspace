__author__ = 'Administrator'
def digsum(n):
    if(n==0):
        return 0
    if(n%9==0):
        return 9
    else:
        return (n%9)

print("Enter 'x' for exit:");
print("Enter starting and ending number: ");

start = input("Enter start:");
m = []
if start == 'x':
    exit();
else:
    end = input("Enter start:");
    lower_number = int(start);
    upper_number = int(end);
    print("Prime Numbers between the given range:")

    for num in range(lower_number, upper_number+1):
        if num>1:
            for i in range(2, num):
                if(num%i)==0:
                    break;
                else:
                    print(num,digsum(num));
                    m.append(digsum(num))
    #short = {}.fromkeys(m).keys()
print(short)

