'''
https://www.codewars.com/kata/5f6d120d40b1c900327b7e22/train/python

@test.describe("Leaderboard climbers")
def tests():
    @test.it("basic tests")
    def basic():
        test.assert_equals(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']), ['Fred', 'John', 'Dave', 'Brian', 'Jim'])
        test.assert_equals(leaderboard_sort(['Bob', 'Larry', 'Kevin', 'Jack', 'Max'], ['Max +3', 'Kevin -1', 'Kevin +3']), ['Bob', 'Kevin', 'Max', 'Larry', 'Jack'])
'''
# key point
# insert exceed len(ls), what happen?

#1st solution
def leaderboard_sort(lbd, changes):
    lbd = lbd[:]
    for name,n in map(str.split, changes):
        n,i = int(n), lbd.index(name)
        lbd.pop(i)
        lbd.insert(i-n,name)
    return lbd

def leaderboard_sort(leaderboard, changes):
    ans = [0]*len(leaderboard)
    #print(ans)
    st = leaderboard
    change = [w.split(' ') for w in changes]
    for w in change:
        if int(w[1]) > 0:
            s = st.index(w[0])+1
            new = st.index(w[0]) - int(w[1])
        elif int(w[1]) < 0:
            s = st.index(w[0])
            new = st.index(w[0]) - int(w[1])+1
        st.insert(new,w[0])
        #print(s,new,st)
        del(st[s])
        #print(st)
    return st

leaderboard = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
#print(leaderboard.insert(3,'John'))
changes = ['Dave +1', 'Fred +4', 'Brian -1']
print(leaderboard_sort(leaderboard, changes))
# ans =  ['Fred', 'John', 'Dave', 'Brian', 'Jim']
'''
def leaderboard_sort(leaderboard, changes):
    st = dict(([e,i] for i,e in enumerate(leaderboard)))
    change = dict(([w.split(' ') for w in changes]))
    return st,change
    

def leaderboard_sort(leaderboard, changes):
    new,s = 0,0
    ans = [0]*len(leaderboard)
    #print(ans)
    st = leaderboard
    change = [w.split(' ') for w in changes]
    for w in change:
        if int(w[1]) > 0:
            if w[0] in st:
                s = st.index(w[0])+1
                new = st.index(w[0]) - int(w[1])
            else:pass
        elif int(w[1]) < 0:
            if w[0] in st:
                s = st.index(w[0])
                new = st.index(w[0]) - int(w[1])+1
            else:pass
        st.insert(new,w[0])
        #print(s,new,st)
        del(st[s])
        #print(st)
    return st

'''

