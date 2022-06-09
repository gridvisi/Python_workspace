'''
https://www.codewars.com/kata/59766edb9bfe7cd5b000006e/train/python
帮助水果包装工分拣出坏苹果。

有7个品种的苹果，都是成对包装，堆放在水果箱里。有些苹果已经变质了。水果包装工要确保将变质的苹果从水果盒中取出或更换。下面是分类。

苹果品种是用数字表示的，1到7

一个水果包装用一个2元数组[4,3]表示。

一个水果包里有一个坏苹果，或一个坏包，用[2,0]或[0,2]表示。

用[0,0]表示一个水果包装中有两个坏苹果，或者说是一个烂包装。

一个水果盒的代表是：

需要满足的条件。

1.一个坏的包装，如果有另一个坏的包装，有一个好的苹果备用，则应更换坏的苹果。否则，坏的包装应被丢弃。

2.果盒中的包装顺序应保留。重新包装是从果箱指数=0的顶部到底部第n个指数发生的。同时注意重新包装时包装中
的水果如何排序。例子如上图INPUT/OUPUT所示。

3.腐烂的包装要丢弃。

4.可以有同品种苹果的包装，如[1,1]，这不是问题。

Test.describe("No good groups")
Test.assert_equals(bad_apples([]), [])
Test.assert_equals(bad_apples([[0, 0], [0, 0]]), [])
Test.assert_equals(bad_apples([[0, 0], [0, 0], [0, 1], [0, 0], [0, 0]]), [])
Test.end_group()

Test.describe("Keep or Discard")
Test.assert_equals(bad_apples([[0, 0], [3, 7], [0, 5]]), [[3, 7]])
Test.assert_equals(bad_apples([[1,3],[7,6],[7,2],[1,3],[2,3],[4,5],[7,6]]), [[1,3],[7,6],[7,2],[1,3],[2,3],[4,5],[7,6]])
Test.assert_equals(bad_apples([[1,2],[6,1],[5,2],[6,3],[1,4],[2,5],[7,6],[0,1]]), [[1,2],[6,1],[5,2],[6,3],[1,4],[2,5],[7,6]])
Test.end_group()

Test.describe("Mix and Match")
Test.assert_equals(bad_apples([[0,0],[1,0],[0,2],[3,0],[4,0],[0,5],[0,6],[7,0]]), [[1,2],[3,4],[5,6]])
Test.assert_equals(bad_apples([[1,3],[7,6],[7,2],[1,3],[0,1],[4,5],[0,3],[7,6]]), [[1,3],[7,6],[7,2],[1,3],[1,3],[4,5],[7,6]])
Test.assert_equals(bad_apples([[1,3],[7,6],[7,2],[0,0],[0,3],[1,3],[1,3],[4,5],[7,6]]), [[1,3],[7,6],[7,2],[1,3],[1,3],[4,5],[7,6]])
Test.end_group()
'''
# [0,1] mix up with [2,0] but [0,2]
#[[1,3],[7,6],[7,2],[1,3],[0,1],[4,5],[0,3],[7,6]]), [[1,3],[7,6],[7,2],[1,3],[1,3],[4,5],[7,6]]
apples = [[0,0],[1,0],[0,2],[3,0],[4,0],[0,5],[0,6],[7,0]]
apples = [[1,3],[7,6],[7,2],[1,3],[0,1],[4,5],[0,3],[7,6]]

def bad_apples(apples):
    #vacant = [i for i in apples if 0 in i]
    ans = []
    avoid = []
    for i,n in enumerate(apples):
        if 0 not in n:
            ans.append(n)
        elif 0 in n and sum(n)!= 0 and i not in avoid:
            j = i+1
            if j == len(apples) - 1:
                return ans
                #print(n,j)

            elif j < len(apples)-1:
                while 0 not in apples[j]:
                    j += 1
                    if j == len(apples)-1:
                        return ans + apples[i+1:]
                n.extend(apples[j])
                #print(n)
                avoid.append(j)
                n = [i for i in n if i!=0]
                ans.append(n)
                #print(n)

    return [i for i in ans if 0 not in i]

apples = [[0, 0], [0, 0], [0, 1], [0, 0], [0, 0]]
apples = [[1,3],[7,6],[7,2],[0,0],[0,3],[1,3],[1,3],[4,5],[7,6]]
#  [[1,3],[7,6],[7,2],[1,3],[1,3],[4,5],[7,6]]

apples = [[7, 3]]
print(bad_apples(apples))

'''
    left = [i for i in apples if i[0]==0]
    right = [i for i in apples if i[1]==0 ]
'''
print(bool(1) ^ bool(0))
a, b = 0, 1
test = []
test.append([a or b])
print(test)


def bad_apples(apples):
    lst, notFull = [], []
    for a,b in apples:
        if (bool(a) ^ bool(b)) and notFull:  lst[notFull.pop()].append(a or b)                  # One bad and partially full box already present: fill it (as second element)
        elif a and b:                        lst.append([a,b])                                  # 2 good ones: keep as they are
        elif a or b:                         notFull.append(len(lst)) ; lst.append([a or b])    # 1 good but no partial box: archive
    if notFull: lst.pop(notFull.pop())                                                          # If 1 not full box remains: remove it
    return lst