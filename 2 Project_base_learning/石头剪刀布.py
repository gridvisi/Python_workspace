'''
demonstrate Stone, Stainless, Paper game
Created on 2012-11-1
@author: Eric
'''
import random

# elementA-->DRAW  WIN      LOST
COMPETE_RESULT = {"Stone": ["Stone", "Stainless", "Paper"],
                  "Stainless": ["Stainless", "Paper", "Stone"],
                  "Paper": ["Paper", "Stone", "Stainless"]}
SIGN = {0: "Stone", 1: "Stainless", 2: "Paper"}
RESULTS = {0: "DRAW", 1: "WIN", 2: "LOST"}


def rochambeauGame():
    print('''0:STONE
1:STAINLESS
2:Paper
3:quit
''')
    while True:
        userSign = input("please input your userSign number:")
        if int(userSign) in (1, 2, 3, 0):
            if userSign == 0:
                exit()
            else:
                userSignResults = COMPETE_RESULT[SIGN[int(userSign)]]
                pcSign = SIGN[int(genereteRandomPCSign())]
                print("User Sign:" + SIGN[int(userSign)] + " PC Sign:" + pcSign + " \n####result is: user " + RESULTS[
                    userSignResults.index(pcSign)])
        else:
            print("please input correctly order")


# generate a random number,[0,2]
def genereteRandomPCSign():
    return random.randrange(3)


if __name__ == '__main__':
    rochambeauGame()
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,random

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class GameUi(QDialog):
    def __init__(self,parent=None):

        super(GameUi,self).__init__(parent)

        self.guess_list = ['石头', '剪刀', '布']

        self.guize = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

        self.setWindowTitle(self.tr("石头剪刀布"))

        self.Total = 0

        self.YouWin = 0

        self.YouLose = 0

        #选项按钮
        StonePushButton = QPushButton(self.tr("石头"))

        ScissorsPushButton = QPushButton(self.tr("剪刀"))

        ClothPushButton = QPushButton(self.tr("布"))

        #结果显示
        ResultLabel = QLabel(self.tr("结果："))

        Computer = QLabel(self.tr("电脑："))

        Statistics_Label = QLabel(self.tr("统计"))

        Total_Label = QLabel(self.tr("总局数："))

        self.TotalStat = QLabel()#玩的局数标签

        YouWin_Label = QLabel(self.tr("你赢了："))

        self.YouWinStat = QLabel()#赢得局数标签

        YouLose_Label = QLabel(self.tr("你输了："))

        self.YouLoseStat = QLabel()#你输的局数

        self.Result = QLabel()#结果显示标签

        self.ComputeResult = QLabel()#电脑出什么

        #界面布局
        layout=QGridLayout()

        layout.addWidget(StonePushButton,0,0)

        layout.addWidget(ScissorsPushButton,0,1)

        layout.addWidget(ClothPushButton,0,2)

        layout.addWidget(Computer,1,0)

        layout.addWidget(self.ComputeResult,1,1)

        layout.addWidget(ResultLabel,2,0)

        layout.addWidget(self.Result,2,1)

        layout.addWidget(Statistics_Label,3,1)

        layout.addWidget(Total_Label,4,0)

        layout.addWidget(self.TotalStat,4,1)

        layout.addWidget(YouWin_Label,5,0)

        layout.addWidget(self.YouWinStat,5,1)

        layout.addWidget(YouLose_Label,6,0)

        layout.addWidget(self.YouLoseStat,6,1)


        self.setLayout(layout)

        self.connect(StonePushButton,SIGNAL("clicked()"),self.Stone)
        self.connect(ClothPushButton,SIGNAL("clicked()"),self.Cloth)
        self.connect(ScissorsPushButton,SIGNAL("clicked()"),self.Scissors)

    def Stone(self):
        self.computer = random.choice(self.guess_list)
        self.ComputeResult.setText(self.tr(self.computer))
        self.people='石头'
        self.Total+=1
        self.judge()

    def Scissors(self):
        self.computer = random.choice(self.guess_list)
        self.ComputeResult.setText(self.tr(self.computer))
        self.people='剪刀'
        self.Total+=1
        self.judge()

    def Cloth(self):
        self.computer = random.choice(self.guess_list)
        self.ComputeResult.setText(self.tr(self.computer))
        self.people='布'
        self.Total+=1
        self.judge()

    def judge(self):
        self.TotalStat.setText(str(self.Total))
        if self.people == self.computer:
            self.Result.setText(self.tr("平局"))
        elif [self.computer,self.people] in self.guize:
            self.Result.setText(self.tr("你输了"))
            self.YouLose+=1
            self.YouLoseStat.setText(str(self.YouLose))
        else:
            self.Result.setText(self.tr("你赢了"))
            self.YouWin+=1
            self.YouWinStat.setText(str(self.YouWin))

if __name__=='__main__':
    app = QApplication(sys.argv)
    GUI = GameUi()
    GUI.show()
    app.exec_()
'''