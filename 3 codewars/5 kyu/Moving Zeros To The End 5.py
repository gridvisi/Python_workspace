def move_zeros(array):
    count = array.count('0')
    print(array.count('0'))
    for i in range(count):
        array.remove('0')
    for i in range(count):
        array.append(0)
    return array
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))