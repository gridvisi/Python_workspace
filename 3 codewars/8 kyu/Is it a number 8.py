def isDigit(string):
    try:
        string = float(string)
        return True
    except ValueError:
        return False
print(isDigit("s2222"))