'''
https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python


'''

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [i for i in birds if i not in geese]


#2nd
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return list(filter(lambda x: x not in geese, birds))