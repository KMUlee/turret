from turret import Game
import time
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import *

class Button(QToolButton):

    def __init__(self,callback,text,x,y):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.clicked.connect(callback)
        self.X = x
        self.Y = y
        self.set(text)

    def set(self, text):
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size


class TurretGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.turrets = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer)
        self.num = 0
        self.test = 1
        self.test_2 = 0
        self.turretButton = []
        self.default = [30, [15, 10]]
        self.turretsDisplay = QLineEdit()

        #color
        self.color = ["blue","darkgreen",'red','darkblue','brown','blue green','black','gray']
        #Label
        label = QLabel('Minesweeper!')
        font = label.font()
        font.setPointSize(font.pointSize() + 10)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)

        #Layout
        mainLayout = QVBoxLayout()
        turretLayout = QGridLayout()
        display = QGridLayout()
        SelectLayout  = QHBoxLayout()

        #Line
        self.turretsDisplay.setAlignment(Qt.AlignCenter)
        self.timerDisplay = QLineEdit("00:00")
        self.timerDisplay.setAlignment(Qt.AlignCenter)
        self.turretsDisplay.setReadOnly(True)
        self.timerDisplay.setReadOnly(True)

        #Button
        self.Flag = Button(self.ButtonEvent,"Flag",0,0)
        Easy = Button(self.ButtonEvent,"Easy",0,0)
        Hard = Button(self.ButtonEvent,"Hard",0,0)
        reStart = Button(self.Clear,"START!!", 0, 0)
        self.turretButton = [[0 for j in range(self.default[1][1])] for i in range(self.default[1][0])]
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x] = Button(self.Event, ' ', x, y)
                turretLayout.addWidget(self.turretButton[y][x], y, x)
                self.turretButton[y][x].setStyleSheet("background-color : skyblue")

        self.StartGame()
        SelectLayout.addWidget(Easy)
        SelectLayout.addWidget(self.Flag)
        SelectLayout.addWidget(Hard)
        display.addWidget(self.turretsDisplay,0,0)
        display.addWidget(self.timerDisplay,0,2)
        mainLayout.addWidget(label)
        mainLayout.addWidget(reStart)
        mainLayout.addLayout(SelectLayout)
        mainLayout.addLayout(display)
        mainLayout.addLayout(turretLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Minesweeper Game")

    def StartGame(self):
        # Start
        self.turret = Game()
        self.turret.Setting(self.default[0],self.default[1])
        self.turret.newGame()
        self.timer.stop()
        self.timerDisplay.setText("00:00")
        self.turrets = self.turret.getTurrets()
        self.turrets_copy = self.turret.getTurrets()
        self.turretsDisplay.setText(str(self.turrets))

    def find(self,x,y):
        X = [-1, 0, 1, -1, 1, -1, 0, 1]
        Y = [-1, -1, -1, 0, 0, 1, 1, 1]
        if self.test == 1:
            if self.turretButton[y][x].text() == "F":
                return
            if self.turret.getCoordinate(y, x) == "*":
                self.turretsDisplay.setText("BOOM!!")
                self.Boom()
                self.turretButton[y][x].setStyleSheet("background-color : red")
                return
            if self.turret.getCoordinate(y, x) == "0":
                self.turretButton[y][x].set("")
                self.turretButton[y][x].setStyleSheet("color : black")
                self.turret.setCoordinate(y,x,"")
                self.turretButton[y][x].setEnabled(False)
                for i in range(8):
                    if 0 <= x + X[i] <= self.default[1][1] - 1 and 0 <= y + Y[i] <= self.default[1][0] - 1:
                        self.find(x + X[i], y + Y[i])
            else:
                if self.turretButton[y][x].text() == "":
                    return
                self.turretButton[y][x].set(self.turret.getCoordinate(y,x))
                for i in range(8):
                    if self.turretButton[y][x].text() == str(i+1):
                        self.turretButton[y][x].setStyleSheet("color : "+self.color[i])
                        self.turretButton[y][x].setEnabled(False)
        elif self.test == 0:
            if self.turretButton[y][x].text() == "F":
                self.turretButton[y][x].set(" ")
                self.turretButton[y][x].setStyleSheet("color : red")
                self.turretButton[y][x].setStyleSheet("background-color : skyblue")
                self.turrets += 1
                self.turretsDisplay.setText(str(self.turrets))
            elif self.turretButton[y][x].text() == " ":
                if self.turrets > 0:
                    self.turretButton[y][x].set("F")
                    self.turretButton[y][x].setStyleSheet("color : red")
                    self.turrets -= 1
                    self.turretsDisplay.setText(str(self.turrets))
            self.Check()

    def Event(self):
        if self.test_2 == 0:
            self.start = time.time()
            self.timer.start()
            self.test_2 = 1
        button = self.sender()
        self.find(button.X,button.Y)

    def Check(self):
        self.num = 0
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                if self.turretButton[y][x].text() == 'F' and self.turret.getCoordinate(y,x) == "*":
                    self.num += 1
        if self.num == self.turrets_copy:
            self.turretsDisplay.setText("YOU WIN!!")
            self.Boom()

    def Boom(self):
        self.timer.stop()
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                if self.turret.getCoordinate(y,x) == "0":
                    self.turret.setCoordinate(y,x,"")
                self.turretButton[y][x].set(self.turret.getCoordinate(self.turretButton[y][x].Y, self.turretButton[y][x].X))
                if self.turretButton[y][x].text() == "":
                    self.turretButton[y][x].setStyleSheet("color : black")
                for i in range(8):
                    if self.turretButton[y][x].text() == str(i+1):
                        self.turretButton[y][x].setStyleSheet("color : "+self.color[i])
                self.turretButton[y][x].setEnabled(False)
                if self.turret.getCoordinate(y,x) == "*":
                    self.turretButton[y][x].setStyleSheet("color : black")


    def Clear(self):
        self.test_2 = 0
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x].set(' ')
                self.turretButton[y][x].setStyleSheet("background-color : skyblue")
                self.turretButton[y][x].setEnabled(True)
        self.StartGame()

    def Timer(self):
        end = time.time()
        m, s = divmod(end - self.start, 60)
        time_str = "%02d:%02d" % (m, s)
        self.timerDisplay.setText(time_str)
        if time_str == "59:59":
            self.Boom()

    def ButtonEvent(self):
        button = self.sender()
        key = button.text()
        if key == "Easy":
            self.default = [20,[15,10]]
            self.Clear()
        elif key == "Hard":
            self.default = [30,[15,10]]
            self.Clear()
        elif key == "Flag":
            if self.test == 1:
                self.test = 0
                self.Flag.setStyleSheet("color : red")
            elif self.test == 0:
                self.test =1
                self.Flag.setStyleSheet("color : black")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = TurretGame()
    game.show()
    sys.exit(app.exec_())
