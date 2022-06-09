# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:57:05 2019

@author: Mr.Ming
"""

#user
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.__password = password

    def getUserName(self):
        return self.userName

    def setUserName(self, userName):
        self.userName = userName

    def getpassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def __repr__(self):
        return "User{" + "userName=" + self.userName + "}"


# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:13:21 2019

@author: Mr.Mi

书籍module
"""


class Book:
    def __init__(self, Id=None, bookName=None, info=None):
        self.id = Id
        self.bookName = bookName
        self.info = info

    def getId(self):
        return self.id

    def setID(self, Id):
        self.id = Id

    def getBookName(self):
        return self.bookName

    def setBookName(self, bookName):
        self.bookName = bookName

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def __repr__(self):
        return "Book{" + "id=" + str(
            hash(self.id)) + ", bookName='" + self.bookName + "'" + ", info='" + self.info + "'}"


# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:55:46 2019

@author: Mr.Ming
"""


class Order:
    def __init__(self, timer=None, bookName=None):
        self.timer = timer
        self.bookName = bookName

    def getTimer(self):
        return self.timer

    def getBookName(self):
        return self.bookName

    def __repr__(self):
        return "Order{" + "timer=" + self.timer + ", books='" + self.bookName




# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:45:34 2019

@author: Mr.Ming
"""

import time
import uuid
'''

from User import User
from Book import Book
from Order import Order
'''

userList = []
bookList = []
orderList = []

def mian():
    # 数据准备
    userList.append(User(userName = "Louis", password = "123123"))
    userList.append(User(userName = "Angelina", password = "123456"))
    userList.append(User(userName = "Julian", password = "666666"))
    userList.append(User(userName="李晶", password="666666"))

    bookList.append(Book(uuid.uuid3(uuid.NAMESPACE_DNS, 'C Primer Plus'), 'C Primer Plus', 'C语言学习经典'))
    bookList.append(Book(uuid.uuid3(uuid.NAMESPACE_DNS, 'Core Python Application Programming'),'Core Python Application Programming', 'Python学习经典'))
    bookList.append(Book(uuid.uuid3(uuid.NAMESPACE_DNS, '世界上下五千年'), '世界上下五千年', '世界历史'))
    bookList.append(Book(uuid.uuid3(uuid.NAMESPACE_DNS, '何以笙箫默'), '何以笙箫默', '顾漫小说'))
    # 主界面
    # 登录 注册
    print('{:#^30}'.format('欢迎使用图书馆管理系统'))
    print("请选择功能:")
    print("\t◇1.登录")
    print("\t◇2.注册")
    print("\t◇3.退出")
    print(">" * 20 +  "<" * 20)
    loginChoice = input("~$")
    if eval(loginChoice) == 1:
        # 登录
        loginContinue = True
        while loginContinue:
            if login():     # 通过登录函数的返回值判断是否登录成功
                print("登录成功")
                loginContinue = False
            else:
                print("登录失败,请重新登录")
        pass
    elif eval(loginChoice) == 2:
        # 注册
        registe()
        loginContinue = True
        while loginContinue:
            if login():
                print("登录成功")
                loginContinue = False
            else:
                print("登录失败,请重新登录")
        pass
    elif eval(loginChoice) == 3:
        # 退出
        return print("感谢您登录,再见!")
    else:
        print("输入错误")
    # 登录后的主界面
    looding = True
    while looding:
        print("请选择功能:")
        print("\t◇1.查看图书")
        print("\t◇2.用户借阅和借阅记录")
        print("\t◇3.图书管理")
        print("\t◇4.退出")
        print(">" * 20 +  "<" * 20)
        functionChoice = input("~$")
        if eval(functionChoice) == 1:
            # 查看图书
            print(bookList)
        elif eval(functionChoice) == 2:
            # 用户借书和查看借阅记录
            circleLooding = True
            while circleLooding:
                print("请输入执行的操作:")
                print("\t◇1.借书")
                print("\t◇2.借阅记录")
                print("\t◇3.返回主菜单")
                print(">" * 20 +  "<" * 20)
                functionChoice = input("~$")
                if eval(functionChoice) == 1:
                    borrowBook = input("请输入你要借阅的书籍:")
                    for book in bookList:
                        if book.getBookName() == borrowBook:        # 判断需要借阅的书籍是否在书库中
                            orderList.append(Order(time.ctime(), borrowBook))
                            print("借阅成功")
                elif eval(functionChoice) == 2:
                    # 借阅列表
                    print(orderList)
                elif eval(functionChoice) == 3:
                    circleLooding = False
                else:
                    print("输入错误")
        elif eval(functionChoice) == 3:
            # 图书管理
            print("请选择:")
            print("\t◇1.添加书籍")
            print("\t◇2.删除书籍")
            print(">" * 20 +  "<" * 20)
            functionChoice = input("~$")
            if eval(functionChoice) == 1:
                # 添加书籍
                addBook()
            elif eval(functionChoice) == 2:
                # 删除数据
                deleteBook()
            else:
                print("输入错误")
        elif eval(functionChoice) == 4:
            # 退出
            looding = False
            return print("感谢您登录,再见!")
        else:
            print("输入错误")
    pass

def login():
    userName = input("请输入用户名:")
    password = input("请输入密码:")
    for user in userList:
        # 当输入的用户名不为空且用户名和密码和用户对象列表中的数据匹配时返回真(登录成功)
        if userName != "" and user.getUserName() == userName and user.getpassword() == password:
            return True
    return False

def registe():
    userName = input("请输入用户名:")
    password = input("请输入密码:")
    # 防止重复用户名
    for user in userList:
        if user.getUserName == userName:
            print("用户名已存在,注册失败,请换一个")
            registe()
    # 将新增的用户对象添加到用户对象列表
    userList.append(User(userName = userName, password = password))
    print("注册成功")
    pass

def addBook():
    # 添加书籍
    looding = True
    while looding:
        bookName = input("请输入添加的书籍名:")
        bookInfo = input("请输入书籍的描述信息:")
        bookList.append(Book(uuid.uuid3(uuid.NAMESPACE_DNS, bookName), bookName, bookInfo))
        print("是否继续添加:")
        print("\t◇1.继续")
        print("\t◇2.返回主菜单")
        print(">" * 20 +  "<" * 20)
        exitChoice = input("~$")
        if eval(exitChoice) == 2:
            looding = False
            print("添加完毕")
    pass

def deleteBook():
    # 删除书籍
    looding = True
    while looding:
        bookName = input("请输入要删除的书籍名:")
        for i in range(len(bookList)):
            if bookList[i].getBookName() == bookName:
                k = i       # 获取要删除书籍的下标
        bookList.pop(k)
        print("是否继续删除:")
        print("\t◇1.继续")
        print("\t◇2.返回主菜单")
        print(">" * 20 +  "<" * 20)
        exitChoice = input("~$")
        if eval(exitChoice) == 2:
            looding = False
            print("删除完毕")
    pass

mian()

