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
        self.timer.start(1000)
        self.timer.timeout.connect(self.Timer)
        self.num = 0
        self.test = 1
        self.turretButton = []
        self.default = [0.2, [15, 10]]
        self.turretsDisplay = QLineEdit()
        self.StartGame()

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
        self.timerDisplay = QLineEdit()
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
        self.copy = self.MakeRecusive(self.turret.getTile())
        self.timer.start()
        self.start = time.time()
        self.turrets = self.turret.getTurrets()
        self.turrets_copy = self.turret.getTurrets()
        self.turretsDisplay.setText(str(self.turrets))

    def

    def Event(self):
        button = self.sender()
        key = button.text()
        x = button.X
        y = button.Y
        if self.test == 1:
            if self.turret.getCoordinate(y, x) == "*"
                self.Boom()
            elif self.turret.getCoordinate(y,x) == "0":

        if self.test == 1:
            where = self.turret.getCoordinate(y, x)
            if (button.text() == "F"):
                return
            self.turretButton[y][x].set(where)
            self.turretButton[y][x].setStyleSheet("background-color : lightgreen")
            self.turretButton[y][x].setEnabled(True)
            if button.text() == "*":
                self.timer.stop()
                self.turretsDisplay.setText("BOOM!!")
                self.Boom()
            elif button.text() == "0":
                zeroArray = self.R(self.MakeRecusive(self.turret.getTile()), x, y)
                for ys in range(len(zeroArray)):
                    for xs in range(len(zeroArray[0])):
                        if zeroArray[ys][xs] == 'K' or zeroArray[ys][xs] == 'P':
                            where2 = self.turret.getCoordinate(ys, xs)
                            if self.turretButton[ys][xs].text() == "F":
                                continue
                            self.turretButton[ys][xs].set(where2)
                            if self.turret.getCoordinate(ys, xs) == "0":
                                self.turretButton[ys][xs].setStyleSheet("background-color : snow")
                                self.turretButton[ys][xs].setEnabled(False)
                            else:
                                self.turretButton[ys][xs].setStyleSheet("background-color : lightgreen")
                                self.turretButton[ys][xs].setEnabled(True)

        elif self.test == 0:
            if key == "F":
                self.turretButton[y][x].set(" ")
                self.turretButton[y][x].setStyleSheet("color : red")
                self.turretButton[y][x].setStyleSheet("background-color : skyblue")
                self.turrets += 1
                self.turretsDisplay.setText(str(self.turrets))
            elif key == " ":
                if self.turrets > 0:
                    self.turretButton[y][x].set("F")
                    self.turretButton[y][x].setStyleSheet("color : red")
                    self.turrets -= 1
                    self.turretsDisplay.setText(str(self.turrets))
            self.Check()

    def Check(self):
        self.num = 0
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                if self.turretButton[y][x].text() == 'F' and self.turret.getCoordinate(y,x) == "*":
                    self.num += 1
        if self.num == self.turrets_copy:
            self.timer.stop()
            self.turretsDisplay.setText("YOU WIN!!")
            self.Boom()

    def Boom(self):
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x].set(self.turret.getCoordinate(self.turretButton[y][x].Y, self.turretButton[y][x].X))
                self.turretButton[y][x].setEnabled(False)
                if self.turretButton[y][x].text() == "*":
                    self.turretButton[y][x].setStyleSheet("background-color : red")


    def Clear(self):
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
            self.timer.stop()
            self.Boom()

    def MakeRecusive(self, turret):
        returret = []
        for i in turret:
            recol = []
            for j in i:
                recol.append(j)
            returret.append((recol))
        return returret

    def R(self, tile, x, y):
        X = [-1,0,1,-1,1,-1,0,1]
        Y = [-1,-1,-1,0,0,1,1,1]
        if tile[y][x] == "0":
            tile[y][x] = "P"
            for i in range(8):
                if 0 <= x +X[i] <= self.default[1][1]-1 and 0 <= y + Y[i] <= self.default[1][0]-1 :
                    self.R(tile,x + X[i],y + Y[i])
        else:
            tile[y][x] = "P"
        return tile

    def ButtonEvent(self):
        button = self.sender()
        key = button.text()
        if key == "Easy":
            self.default = [0.1,[15,10]]
            self.Clear()
        elif key == "Hard":
            self.default = [0.2,[15,10]]
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
