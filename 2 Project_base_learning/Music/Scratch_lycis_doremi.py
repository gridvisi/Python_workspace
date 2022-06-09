
num = [i for i in range(1,8)]
scratch = [60 + 2*i if i < 3 else 60 + 2*i-1 for i in range(8)]
chords = ['C','D','E','F','G','A','B']

sratch_dict = dict(zip(num,scratch))
print(sratch_dict)

#OUTPUT: {1: 60, 2: 62, 3: 64, 4: 65, 5: 67, 6: 69, 7: 71}

chords = [1,2,3,4,5,5,5,4,3,4,4,4,3,
          2,1,3,1,0,6,6,6,5,4,3,4,4,
          4,3,2,1,3,5,0,6,6,6,5,4,5,
          5,5,4,3,4,4,4,3,2,1,3,1,0]

#ouput = [sratch_dict[i] for i in chords]
#print(ouput)

add = {0:58}
sratch_dict.update(add)
print(sratch_dict)
ouput = [sratch_dict[i] for i in chords]
print(ouput)