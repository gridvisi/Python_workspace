def no_space(x):
    x = list(x)
    for i in range(x.count(' ')):
        x.remove(' ')
    return ''.join(x)
print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))