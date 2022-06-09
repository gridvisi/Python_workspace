



print(1, 2, 3, 4, 5,)# 2 3 4 5

les = [str(i) for i in range(10)]

print("\n".join(les))
# 效果等同于 print(1, 2, 3, 4, 5, … ,9,sep="\n")
print("\n".join("Hello World"))


#时、分、秒
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


'''

likes [] // must be "no one likes this" 
likes[]//必须是“没有人喜欢这个” 
likes ["Peter"] // must be "Peter likes this" 
likes[“Peter”]//必须是“Peter likes this” 
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this" 
likes[“Jacob”，“Alex”]//必须是“Jacob and Alex like this” 
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this" 
likes[“Max”，“John”，“Mark”]//必须是“Max，John and Mark like this” 
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this" 
likes[“Alex”，“Jacob”，“Mark”，“Max”]//必须是“Alex，Jacob 和其他两个这样的” 

'''
def likes(names):
    n = len(names)
    return { 0: 'no one likes this',
             1: '{} likes this',
             2: '{} and {} like this',
             3: '{}, {} and {} like this',
             4: '{}, {} and {others} others like this'
             }[min(4, n)].format(*names[:3], others=n-2)