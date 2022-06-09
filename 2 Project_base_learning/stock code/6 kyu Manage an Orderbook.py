'''
https://www.codewars.com/kata/5f3e7df1e0be5a00018a008c/train/python

    def test_add_message_1():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 1)]), "1@1 : 0@0")
    @test.it("Add Message 2")
    def test_add_message_2():
        test.assert_equals(print_tob([('a', 's', 1, 1, 1)]), "0@0 : 1@1")
    @test.it("Add Message 3")
    def test_add_message_3():
        test.assert_equals(print_tob([('a', 'b', 1, 2, 2), ('a', 'b', 2, 1, 1)]), "2@2 : 0@0")
    @test.it("Add Message 4")
    def test_add_message_4():
        test.assert_equals(print_tob([('a', 'b', 1, 2, 2), ('a', 'b', 2, 1, 1)]), "2@2 : 0@0")
    @test.it("Add Message 5")
    def test_add_message_5():
        test.assert_equals(print_tob([('a', 's', 1, 1, 1), ('a', 's', 2, 2, 2)]), "0@0 : 1@1")
    @test.it("Add Message 6")
    def test_add_message_6():
        test.assert_equals(print_tob([('a', 's', 1, 2, 2), ('a', 's', 2, 1, 1)]), "0@0 : 1@1")
    @test.it("Add Message 7")
    def test_add_message_7():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 4), ('a', 's', 2, 1, 30), ('a', 'b', 3, 5, 1), ('a', 's', 4, 2, 70), ('a', 's', 5, 5, 40), ('a', 's', 6, 5, 40),
                                      ('a', 'b', 7, 4, 6), ('a', 'b', 8, 6, 6), ('a', 'b', 9, 2, 6), ('a', 's', 10, 2, 30), ]), "12@6 : 3@30")

    @test.it("Cancel Message 1")
    def test_cancel_message_1():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 1), ('c', 1)]), "0@0 : 0@0")
    @test.it("Cancel Message 2")
    def test_cancel_message_2():
        test.assert_equals(print_tob([('a', 's', 1, 1, 1), ('c', 1)]), "0@0 : 0@0")
    @test.it("Cancel Message 3")
    def test_cancel_message_3():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 1), ('a', 'b', 2, 1, 2), ('c', 1)]), "1@2 : 0@0")
    @test.it("Cancel Message 4")
    def test_cancel_message_4():
        test.assert_equals(print_tob([('a', 's', 1, 1, 1), ('a', 's', 2, 1, 2), ('c', 2)]), "0@0 : 1@1")
    @test.it("Cancel Message 5")
    def test_cancel_message_5():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 1), ('a', 'b', 2, 1, 2), ('a', 'b', 3, 1, 2), ('c', 2)]), "1@2 : 0@0")
    @test.it("Cancel Message 6")
    def test_cancel_message_6():
        test.assert_equals(print_tob([('a', 's', 1, 1, 1), ('a', 's', 2, 1, 2), ('a', 's', 3, 2, 1), ('c', 1)]), "0@0 : 2@1")
    @test.it("Cancel Message 7")
    def test_cancel_message_7():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 1), ('a', 'b', 2, 1, 2), ('a', 's', 3, 2, 10), ('a', 's', 4, 2, 11), ('c', 2), ('c', 4)]), "1@1 : 2@10")
    @test.it("Cancel Message 8")
    def test_cancel_message_8():
        test.assert_equals(print_tob([('a', 'b', 1, 1, 4), ('a', 's', 2, 1, 30), ('a', 'b', 3, 5, 1), ('a', 's', 4, 2, 70), ('a', 's', 5, 5, 40), ('a', 's', 6, 5, 40),
                                      ('c', 2), ('c', 5), ('a', 'b', 7, 4, 6), ('a', 'b', 8, 6, 6), ('c', 7), ('a', 'b', 9, 2, 6), ('c', 3), ('a', 's', 10, 2, 30)]), "8@6 : 2@30")
'''

#8th by ericlee
def print_tob(feed):
    book = {'buy': [0, 0], 'sell': [0, float("inf")]}  # 'id':0 float("info")
    valid, qt = [], []

    # filter all the cancel order id
    for q in feed:
        if q[0] != 'c':
            valid.append(q)
        qt.append(q[1])

    # compare price with perior id, the bigger record append
    for t in valid:
        if t[2] not in qt and t[1] == 'b':
            if t[4] > book['buy'][1]:
                book['buy'] = [t[3], t[4]]
            elif t[4] == book['buy'][1]:
                book['buy'][0] += t[3]

        elif t[2] not in qt and t[1] == 's':
            if t[4] < book['sell'][1]:
                book['sell'] = t[3], t[4]
    print(book['sell'])
    if book['sell'][1] == float("inf"): book['sell'] = [0,0]
    return f"{'@'.join(map(str,book['buy']))} : {'@'.join(map(str,book['sell']))}"

feed = [('a', 'b', 1, 1, 1), ('a', 'b', 2, 1, 2), ('c', 1)] # "1@2 : 0@0"

#feed = [('a', 'b', 1, 1, 4), ('a', 's', 2, 1, 30), ('a', 'b', 3, 5, 1), ('a', 's', 4, 2, 70), ('a', 's', 5, 5, 40), ('a', 's', 6, 5, 40),
#          ('c', 2), ('c', 5), ('a', 'b', 7, 4, 6), ('a', 'b', 8, 6, 6), ('c', 7), ('a', 'b', 9, 2, 6), ('c', 3), ('a', 's', 10, 2, 30)]
#, "8@6 : 2@30")

print(print_tob(feed))


#1st
from collections import defaultdict


def print_tob(feed):
    memo = {}
    for order in feed:
        if order[0] == 'c':
            del memo[order[1]]
        else:
            memo[order[2]] = (order[1], order[3], order[4])

    res = defaultdict(lambda: defaultdict(int))
    for side, quantity, price in memo.values():
        res[side][price] += quantity

    a, b = max(res['b'].items(), default=(0, 0))
    c, d = min(res['s'].items(), default=(0, 0))

    return f"{b}@{a} : {d}@{c}"

#2nd
from collections import defaultdict


class Book(dict):
    def a(self, *data): self[data[1]] = data

    def c(self, id):    del self[id]

    def buildDict(self):
        d = {'s': defaultdict(int), 'b': defaultdict(int)}
        for typ, _, n, p in self.values(): d[typ][p] += n
        return d

    def __str__(self):
        d = self.buildDict()
        buyItem = max(d['b'].items(), key=lambda it: it[0], default=(0, 0))
        sellItem = min(d['s'].items(), key=lambda it: it[0], default=(0, 0))
        return "{1}@{0} : {3}@{2}".format(*buyItem, *sellItem)


def print_tob(feed):
    book = Book()
    for kind, *data in feed: getattr(book, kind)(*data)
    return str(book)