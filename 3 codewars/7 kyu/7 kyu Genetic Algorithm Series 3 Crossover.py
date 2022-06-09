
# https://www.codewars.com/kata/567d71b93f8a50f461000019/train/python

def crossover(chromo1, chromo2,index):
    return [chromo1[:index]+chromo2[index:],chromo2[:index]+chromo1[index:]]

chromo1, chromo2, index = "111000", "000110", 3
print(crossover(chromo1, chromo2,index))