

firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for i in range(len(firsts)):
    print(f"'{firsts[i]} {lasts[i]}'")

'Anna Smith'
'Bob Doe'
'Charles Evans'

firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for first, last in zip(firsts, lasts):
    print(f"'{first} {last}'")

'Anna Smith'
'Bob Doe'
'Charles Evans'

firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for z in zip(firsts, lasts):
    print(z)

('Anna', 'Smith')
('Bob', 'Doe')
('Charles', 'Evans')

firsts = ["Anna", "Bob", "Charles"]
lasts = ["Smith", "Doe", "Evans"]
for z in zip(firsts, lasts):
    first, last = z
    print(f"'{first} {last}'")

'Anna Smith'
'Bob Doe'
'Charles Evans'

firsts = ["Anna", "Bob", "Charles"]
middles = ["Z.", "A.", "G."]
lasts = ["Smith", "Doe", "Evans"]
for z in zip(firsts, middles, lasts):
    print(z)

('Anna', 'Z.', 'Smith')
('Bob', 'A.', 'Doe')
('Charles', 'G.', 'Evans')

prefixes = ["Dr.", "Mr.", "Sir"]
for z in zip(prefixes, firsts, middles, lasts):
    print(z)

('Dr.', 'Anna', 'Z.', 'Smith')
('Mr.', 'Bob', 'A.', 'Doe')
('Sir', 'Charles', 'G.', 'Evans')


'''

此事件发生后，____ 高度重视，立即连夜召开____会议。____立即作出____，
要求组织____，妥善处理___，迅速查清____，严肃追究____；立即组织开展_____，
进一步做好____，举一反三，防止_____。

目前，____情绪稳定。____深感内疚，自责，痛心。 
'''

def template(a,b,c,d,e,f,g,h,i,j,k,l,m):
    return f"此事件发生后，{a} 高度重视，立即连夜召开{b}会议。{c}" \
           f"立即作出{d}，要求组织{e}，妥善处理{f}，迅速查清{g}，" \
           f"严肃追究{h}；立即组织开展{i}，进一步做好{j}，举一反三，" \
           f"防止{k}。目前，{l}情绪稳定。{m}深感内疚，自责，痛心。 "


'''
Python 标准库附带一个模块, 用于读取和写入 CSV 文件。
除其他外，它为您提供类以及当您想要使用 CSV 文件的标题来
读取数据行（如字典）或当您将数据行用作字典时。 
csv DictReaderDictWriter
下面是一个示例，说明如何获取多个字典并将它们写入 CSV 文件：
'''
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})