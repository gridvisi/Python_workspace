'''

1、对不起，您换汇需要联系储蓄卡客服，转接过去，
2、储蓄卡客服问需要查看我有没有储蓄卡，
       答：可能办过，但没怎么用，也记不得卡号了，但我是贵行多年的白金卡信用卡                  客户，客户资料应该比较全，可否再查下
        自从，开启迷之对话 ——

3、对不起，先生您查看名下的储蓄卡，也需要开通电话银行
4、Okay，转自动语音，尝试开通电话银行，按提示：
5、输入卡号，身份证号，提示卡号或者密码不对，有点晕
6、平复心情，泡杯茶败火，一百个小心继续输，第8遍放弃
7、再联系客服，只问一个问题：本人贵行预留的手机号码是多少
8、客服回：请先注册电话银行业务
9、我问不注册可以查吗？曾在柜台办过人脸识别或回答个人私密信息
10、不行，转上一级经理,与经理的对话又回到了起点
11、 又提示我回到电话银行注册
        问候内心飘过的一万个草原小骆驼，深吸一口气
12、一字一顿给经理讲：“ 给您免费支个招，贵行发一条营销短信，看到哪部手机收到，就是预留的手机号吗？
13、呵呵呵，对面的经理一阵凌乱：啊这，谢谢您
'''

class User:
    def __int__(self,name,id,phone):
        self.name = name
        self.id = id
        self.phone = phone

    def check_id(self):
        NAME = False
        ID = False
        name = input('您的姓名:')
        if name == self.name:
            print(f"客户的姓名正确")
            NAME = True
        else:
            id = input('您的身份证号：')
            if self.id == id:
                ID = True
                print(f'身份证号码正确！')
                print(f"您现在可以查询的信息：\n"
                      "1.查询卡号"
                      "2.查询预留手机号码"
                      "3.查询还款")
        return NAME,ID

    def checkDebtCard(self)->int: #身份证或者是卡号
        if self.check_id():
            print("您输入密码即可查询还款")
        else:
            return print("您提供的个人信息不正确")

    def smstoPhone(self,phone):
        phoneNo = input('请输入手机号:')
        if self.phone == phoneNo:
            return print('已经发送到您的手机')

# 银行录入用户的信息
zhangmin = User()
zhangmin.name = 'zhangmin'
zhangmin.id = '1234'
zhangmin.phone = '18983086450'

#客户张敏打客服电话
zhangmin.check_id()
zhangmin.checkDebtCard()