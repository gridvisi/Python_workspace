'''
https://www.geeksforgeeks.org/english-dictionary-application-using-python/?ref=rp

重要的是，输出不应该因不同的情况而变化，如同一文本的大写和小写输入应该相同，
即rain或Rain或RaIn应该产生相同的输出。此外，如果用户在拼写单词时出错，它应
该返回与输入的单词相关的近似单词，或者打印一个用户友好的信息，说明该单词不存在。
'''
# Import the modules required
import json
from difflib import get_close_matches

# Loading data from json file
# in python dictionary
data = json.load(open("dictionary.json"))

def translate(w):
    # converts to lower case
    w = w.lower()

    if w in data:
        return data[w]
    # for getting close matches of word
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Driver code
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input('Press ENTER to exit')

