
print(any({"1": False, "2": False}))

pairs = { 'word1':0, 'word2':0, 'word3':2000, 'word4':64, 'word5':0, 'wordn':8 }
#print(any(v > 0 for v in pairs.itervalues()))
print(any(v < 0 for v in pairs.values()))