
encoding = {'C' : '1', 'G' : '0', 'A' : '00', 'T': '01'}
def encode(sequence):
  #生成一个空的字符串
    encoded_string = ""
    #追加字符到空的字符串
    for letter in range(len(sequence)):
        encoded_string += encoding[sequence[letter]]
    return encoded_string
print('CCGT:'+ encode('CCGT'))
print('CCAC:'+ encode('CCAC'))