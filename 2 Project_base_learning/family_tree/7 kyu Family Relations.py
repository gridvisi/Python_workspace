'''
https://www.codewars.com/kata/5eaf798e739e39001218a2f4/train/python
https://blog.csdn.net/lanchunhui/article/details/50942382

Test.describe("Basic tests")

family_a = [("Enid", "Susan"), ("Susan", "Deborah")]
Test.assert_equals(relations(family_a, ("Deborah","Enid")), "Grandmother")
Test.assert_equals(relations(family_a, ("Enid","Susan")), "Daughter")


family_b = [('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')]
Test.assert_equals(relations(family_b, ("Judy","Fern")), "Sister")
Test.assert_equals(relations(family_b, ("Deborah","Fern")), "Cousin")
'''
family_list, target_pair = [("Enid", "Susan"), ("Susan", "Deborah")],("Deborah","Enid")
family_list = [('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')]
target_pair = ("Judy","Fern")
target_pair = ('Dianne', 'Judy')
target_pair = ('Deborah', 'Enid')
target_pair = ('Enid','Deborah')
target_pair = ("Deborah","Fern")


def relations(family_list, target_pair):
    tree = dict(zip([p[0] for p in family_list],[[] for i in range(len(family_list))]))
    cousin = []
    for p in family_list:
        if p[0] not in tree.keys():
            tree[p[0]] = [p[1]]
        elif p[0] in tree.keys():
            tree[p[0]].append(p[1])
    print(tree)
    for k,v in tree.items():

        if target_pair[0] in v and target_pair[1] in v:
            return "Sister"

        elif target_pair[0] in k and target_pair[1] in v:
            return "Daughter"

        elif target_pair[0] in k:
            for i in v:
                if target_pair[1] in tree[i]: return "Granddaughter"

        elif target_pair[1] in k:
            for i in v:
                if target_pair[0] in tree[i]: return "Grandmother"

        else:
            if target_pair[0] in v:
                cousin.append(k)
            elif target_pair[1] in v:
                cousin.append(k)
                for v in tree.values():
                    if cousin == v: return "cousin"
print(relations(family_list, target_pair))


#Top 1st
def relations(family_list, target_pair):
    parents = {}
    for parent, child in family_list:
        parents[child] = parent

    a, b = target_pair
    ap = parents.get(a)
    app = parents.get(ap)
    bp = parents.get(b)
    bpp = parents.get(bp)

    if b == ap:
        return 'Mother'
    if b == app:
        return 'Grandmother'
    if a == bp:
        return 'Daughter'
    if a == bpp:
        return 'Granddaughter'
    if ap == bp:
        return 'Sister'
    if app == bpp:
        return 'Cousin'
    if app == bp:
        return 'Aunt'
    if ap == bpp:
        return 'Niece'


#Top 3rd
def relations(f, p):
    def same(a, b): return a(p[0], f) == b(p[1], f)
    if same(ID, P): return "Daughter"
    elif same(P, ID): return "Mother"
    elif same(GP, ID): return "Grandmother"
    elif same(ID, GP): return "Granddaughter"
    elif same(P, P): return "Sister"
    elif same(P, GP): return "Niece"
    elif same(GP, P): return "Aunt"
    elif same(GP, GP): return "Cousin"

def ID(child, _): return child
def P(child, f): return next((p for p, c in f if c == child), None)
def GP(child, f): return P(P(child, f), f)







#树表示为一个二维列表（lists of lists）：
T = [['a, b'], ['c'], ['d', ['e', 'f']]]

class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
t = Tree(Tree('a', 'b'), Tree('c', 'd'))
print(t.right.left)


'''
而对于那些没有内置 list 类型的语言， 我们还有另一种常见的树实现方式，即采取“先子节点，后兄弟节点”的表示法。在这种表示法中，
每一个树节点都有两个用于引用其他节点的“指针”或属性，这似乎与二叉树的情况类似，然而这里，第一个引用指向的是当前节点的第一个子节点，
而第二个引用则是指向的是其兄弟节点。我们对上述代码，稍作修改，将其变成一个多路搜索树（multiway tree）
————————————————
版权声明：本文为CSDN博主「Inside_Zhang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lanchunhui/java/article/details/50942382
'''

class Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next
t = Tree(Tree('a', Tree('b', Tree('c', Tree('d')))))
print(t.kids.next.next.val)

