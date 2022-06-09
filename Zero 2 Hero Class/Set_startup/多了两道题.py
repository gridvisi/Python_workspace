
#set() 集合
my_fruit = ['watemelon','apple','mango','banana','peach']
for i in my_fruit:
    if i == 'banan':
        print(i)
else:
    print(None)

your_fruit = ['pear','strawberry','pear','mango']
print(my_fruit[::1]) #slice

print('slice-even:',list(range(1,100))[::2])
print([i for i in range(100) if i%2==0])

print(set(my_fruit) & set(your_fruit))

# 最大公约数
# 15 = {3，5，15}
# 9 = {3，9}
factor_15 = {3,5,15}
factor_9 = {3,9}
print(factor_15 & factor_9)

print(sorted(['Alg#bra', '$istory', 'Geom^try', '**english']))
five = {'Sort and Star',
        'Merge two sorted arrays into one',
        'Merging sorted integer arrays (without duplicates)',
        'Sort My Textbooks',
        'Greek Sort'
        }

seven = {'enumerable magic#16'}

#夏克
