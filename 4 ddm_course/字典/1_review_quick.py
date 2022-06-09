
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

guess = ["Rock", "Paper", "Scissors"]
guess_cn = ['石头','布','剪刀']
guess_dict = dict(zip(guess,guess_cn))
guess_dictEN = {value:key for key,value in guess_dict.items()}
#guess_dictEN = dict([(value,key) for key,value in guess_dict.items()])

print(guess_dictEN)

for item in guess_dict.items():
    print('item:',item)

keys = guess_dict.keys()
for key in guess_dict:
    print(key)

for key,value in guess_dict.items():
    print(key,value)

#for key,value in guess_dict:
#    print(key,value)

# dict.get(var1,var2)
names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
   'Arnold': 'Hello Arnold'
    }

print(names.get('Joe', "I don't know who you are!"))
#Hello Joe
print(names.get('Rick', "I don't know who you are!"))
#I don't know who you are!