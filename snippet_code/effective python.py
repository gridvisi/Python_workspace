
#10 enummerate replace range+

flavors = ["vanilla","chocolate","pecan","strawberry"]
for i,flavor in enumerate(flavors):
    print('%d:%s'% (i+1,flavor))

#11 zip 遍历两个迭代器
names = ['cecilia','lise','maria']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

#enummerate simpfy
for i,names in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = names
        max_letters = count

for name,count in zip(names,letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)
# zip 其中一个耗尽，即停止产生新的元组

