print("####### 库存书的数量修改函数 ######")


book = '''《学会担当》《注音版红楼梦》《三国演义》《水许传》《太阳溪农场的丽贝卡》《海底两万里》
《草房子》《积极才能成功》《坦克与装甲车》成语故事》《夏洛的网》《中小学公共安全与生命考有(四下)》
《三国演义(白化文)》《综台实,践活动(四下)》《一年级生字墓写本》《句子专项圳练》《道德与法治》、
《木公又玄秘塔》、《五下科等》、《老版高中语文知识手册》、《一年级的马小跳》《宜家IKEA家居册》
《世界儿童周刊1-8》《小哥白尼周刊》《幽黑小读者周刊》《课堂内外周刊》

《小学年级奥数》、《西游记(上)》、《给孩子的诗2》、《详一反三奥数》、《钢铁是怎样炼成的》
《马小跳·侦探小组在行动》、《疯狂学校我们的签班主任》《孔乙己》《阿Q正传》《狂人日记》、
《为了忘却的记念》、《论雷峰塔的倒掉》《大学书法》《岛蛋鬼日记》、《北大门暑夫》、《老人与海》
《彷徨》、《月花夕拾》、《免骨寻踪》、《烙材童话》《三上所写给孩子的名人传记习》、《同桌冤家》、
《洋葱头历险记》。《些成语故事》《科普馆》、《西游记·田文》、《中国神话故事》《作文小状元》。
《人名言》《成语故事》。
《吹牛大王·历险记习》、《假如给我三天光明》。《野草习夏日历险》、《安徒生童话》《少年侦探团》、
《少年侦探团5》《马小跳6年级》《学语文之友》《中华民族是一家人》《中华民方族是一家2》、
《马小北5年级》《马小跳1年级》《马小跳4年级》、《爱我中华》《科科技托起强因梦》、《少年优探团2》、
《鲁鲁龙的礼物》《小贝弟的大梦想》。《一个长上天的大苹果》《是谁在门外》《作文起步》、《优秀作文》
《看图说话》《好词好句》《看图写话》《看图作文》。《日记起步》

'''
c = "abcd , ."
a = c.replace('a', 'z')
print(a)

last_date = "1/2/3"  # 目标为"123"

# 之一：repalce

date = last_date.replace('/', '')
print(date)

mark = ["。", "？", "\n", "、", ","]
ans = book

for dot in mark:
    # print(ans)
    ans = ans.replace(dot, "")
# print("anstring:",ans)

qwe = book.replace("。", "") #
aaa = qwe.replace("？", "")
abc = aaa.replace("\n", "")
ewq = abc.replace("、", "")
print(ewq)
booklist = ewq.split("》")
# booklist.replace
print(booklist)
print(len(booklist))


bookshelf = []
for w in booklist:
    bookshelf.append(w[1:])
print(bookshelf)
bookstock = dict(zip(bookshelf, [2] * len(bookshelf)))

print('所有书库：',bookstock)
#修改字典value：{ key: value} 成对出现
bookstock['水许传'] = bookstock['水许传'] - 1
print('bookstock[水许传]:',bookstock['水许传'])
bookstock['水浒传'] = 5 #追加一本书和数量

#bookstock.pop('') #弹出 ！造成键值和混乱

bookstock.pop('水浒传', "sorry,库里没有你要删除的书")
#print(bookstock['水浒传']) #中断了！！！

print(bookstock.pop('水许传',"sorry,库里没有你要删除的书"))
shandiao = '水许传'
print(bookstock.get(shandiao,f'sorry,库里查不到{shandiao}该书'))

bookstock['水浒传'] = 2
print("水浒传:",bookstock['水浒传'])

print(bookstock)

#输入查询代码：
bookname = input("测试输入准确完整的书名，看剩余的本数：", )
print(bookstock.get(bookname, f"库存里没有《{bookname}》"))

print("####### book module 搜索书函数 ######")


# 查询库存里是否有会员想借的书？
# 模糊查询
# #子函数只干一件事就算模糊查询该书有没有！

def search(bookname): #会员查询一本书：书名
    bool_in = 0 #初始化逻辑判断变量 1， 0 False！ 0= False

    if bookname in bookshelf:
        print(f"库存里有《{bookname}》在bookshelf")
        bool_in = not bool_in  #取反，变成True 或者 1

    elif bookname not in bookshelf:
        #查询的过程，每本书的书名和需要查询的书名字段做 in 判断！！
        # 输入an，但是查询是每次和库存书名比较！
        for book in bookshelf:
            #print(book)
            if bookname in book:
                print("你找的是不是: ", f"《{book}》有{bookstock[book]}本")
                lendorNot = input("你需要借这本书键入 y 否则按空格:",)

                if lendorNot == 'y': bool_in = not bool_in
                else:pass
    return bool_in  #子函数只干一件事就算模糊查询该书有没有！


print("####### book module 借出书并减库存函数 ######")


# module_lend_book
# rank the book which user wanted by inquiry
# module bookWanted
'''
def bookCart(bookWanted={}):
    #print('需要新购书的书名：')
    bookWanted[bookname][0] = bookname
    bookWanted[bookname][1] = 0
    return bookWanted
print('购物车：',bookWantDict(bookWanted={}))
'''



def lend_book(bookname, user):

    if search(bookname) and bookstock[bookname] >= 1:
        lendorNot = input("同意借此书，请输入 1，否则输入 0:")

        if bookstock.get(bookname, '没有这本书') != '没有这本书':
            print(f"显示库存剩余{bookname}共有 {bookstock[bookname]} 本！")
            if lendorNot == '1':
                # 在库存量里减去1
                bookstock[bookname] = bookstock.get(bookname, 0) - 1
                print(f"{bookname}现在剩余：{bookstock[bookname]}本")

                return print(f"《{bookname}》已经借给{user}, 《{bookname}》还剩{bookstock[bookname]}本")

    elif not bookstock.get(bookname) or bookstock[bookname] == 0:
        n = input('是否需要添加入新购书队列 Y or N：',)
        if n == 'Y':
            bookWanted['bookname'][0] = bookname
            bookWanted['bookname'][1] = 1
        else:
            return print(f"{bookname}无法借给{user},{bookname}还剩{bookstock.get(bookname)}本")

bookname, user, bookWanted = bookname,"candy",{"哈利波特":1}
print("************************************")
print("借书流程开始-->")
lend_book(bookname, user, bookWanted={})


#独立性，并且尽量相关性低
# 5次，库里没有，但是有超过5个用户询问，触发购买

#bookstock =
'''

bookwanted = {(k,v) for bookstock.items() if k not in }
inquiryBook = {bookname: 'fei','num':10,
               bookname:"coding",'num':3
               }

def buyNewbook(inquiryBook):
    if BookWanted['inqirynum'] > 5:
        #决定购买
'''





user = input("who are u :",)
lend_book(bookname, user)

#3 module 会员管理系统：
'''
def usersys(person, credit, expire): #手动改写输入的参数：
    # liu同学所有借过的书都放在一个叫bookls 的列表！
    # 刘同学个人信息都放在一个叫user字典里
    # bookls 希望这个变量是从借书的子函数里传过来！！！

    # bookls 从上面函数传过来的
    # 刘同学都借过哪些书？
    bookbag = []
    while True:
        user[person] =  {person:[credit,expire,#bookbag]}

        return user

'''

