
import random
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

num = input('Good day, how many passwords would you like?')
num = int(num)
length = input('Alright, what about the length?')
length = int(length)

for p in range(num):
  password = ''
  for c in range(length):
    password += random.choice(char)
  print(password)