
class TopWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.virusnum = 0
        self.setWindowTitle("消灭地鼠小游戏")
        self.setWindowIcon(QIcon(r'sucai/图标.jpg'))

class virus(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(160, 120)
        self.setStyleSheet("QPushButton{border-image: url(sucai/地洞2.png)}")
        self.upTime = QTimer()
        self.upTime.timeout.connect(self.up)

        for i in range(25):
            exec("self.virus{0}=virus()".format(i))
        for i in range(5):
            for j in range(5):
                exec("self.imagelayout.addWidget(self.virus{0},{1},{2})".format(t, i, j))
                t += 1

app = QApplication(sys.argv)
Display = TopWindow()
Display.setFixedSize(900, 600)
Display.show()
sys.exit(app.exec_())