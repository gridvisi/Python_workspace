def xo(s):
    x_num = 0
    o_num = 0
    output = list(s)
    for i in range(len(output)):
        if output[i] == 'x':
            x_num += 1
        elif output[i] == 'o':
            o_num += 1
    if x_num == o_num:
        return 'True expected'
    else:
        return 'False expected'
print(xo('GCxxfdxbExxxxhkxAxJxo'))