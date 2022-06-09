def is_negative_zero(n):
    if n == 0.0:
        return False
    elif n == -0.0:
        return True
    else:
        return False

print(is_negative_zero(-0.0))