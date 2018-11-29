from turret import Game
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
        self.time = 0
        self.num = 0
        self.nums = 0
        self.turretButton = []
        self.default = [0.25, [15, 10]]
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
        self.timerDisplay = QLineEdit(str(self.time))
        self.timerDisplay.setAlignment(Qt.AlignCenter)
        self.turretsDisplay.setReadOnly(True)
        self.timerDisplay.setReadOnly(True)

        #Button
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
        self.timer.start()
        self.time = 0
        self.turrets = self.turret.getTurrets()
        self.turretsDisplay.setText(str(self.turrets))

    def Event(self):
        button = self.sender()
        key = button.text()
        x = button.X
        y = button.Y
        where = self.turret.getCoordinate(y, x)
        self.turretButton[y][x].set(where)
        self.turretButton[y][x].setStyleSheet("background-color : lightgreen")
        self.turretButton[y][x].setEnabled(False)
        if button.text() == "*":
            self.timer.stop()
            self.turretsDisplay.setText("BOOM!!")
            self.Boom()
        elif button.text() == "0":
            zeroArray = self.RecursiveZero(self.MakeRecusive(self.turret.getTile()),x, y)
            for ys in range(len(zeroArray)):
                for xs in range(len(zeroArray[0])):
                    if zeroArray[ys][xs] == 'K' or zeroArray[ys][xs] == 'P':
                        where2 = self.turret.getCoordinate(ys, xs)
                        self.turretButton[ys][xs].set(where2)
                        if self.turret.getCoordinate(ys,xs) == "0":
                            self.turretButton[ys][xs].setStyleSheet("background-color : snow")
                            self.turretButton[ys][xs].setEnabled(False)
                        else:
                            self.turretButton[ys][xs].setStyleSheet("background-color : lightgreen")
                            self.turretButton[ys][xs].setEnabled(False)
        self.Check()

    def Check(self):
        self.num = 0
        self.nums = 0
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                if self.turretButton[y][x].text() == ' ':
                    self.nums += 1
                    if self.turret.getCoordinate(y,x) == "*":
                        self.num += 1
        if self.nums == self.num == self.turrets:
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
        self.time += 1
        self.timerDisplay.setText(str(self.time))

    def MakeRecusive(self, turret):
        returret = []
        for i in turret:
            recol = []
            for j in i:
                recol.append(j)
            returret.append((recol))
        return returret

    def RecursiveZero(self, turret, x, y):

        copy = turret.copy()

        if copy[y][x] == '0':
            copy[y][x] = 'P'
            if y != len(copy) - 1:
                if copy[y + 1][x] != '0' and copy[y + 1][x] != 'P':
                    copy[y + 1][x] = 'K'
                else:
                    self.RecursiveZero(copy, x, y + 1)
            if x != len(copy[0]) - 1:
                if copy[y][x + 1] != '0' and copy[y][x + 1] != 'P':
                    copy[y][x + 1] = 'K'
                else:
                    self.RecursiveZero(copy, x + 1, y)
            if x != 0:
                if copy[y][x - 1] != '0' and copy[y][x - 1] != 'P':
                    copy[y][x - 1] = 'K'
                else:
                    self.RecursiveZero(copy, x - 1, y)

            if y != 0:
                if copy[y - 1][x] != '0' and copy[y - 1][x] != 'P':
                    copy[y - 1][x] = 'K'
                else:
                    self.RecursiveZero(copy, x, y - 1)
        return copy

    def ButtonEvent(self):
        button = self.sender()
        key = button.text()
        if key == "Easy":
            self.default = [0.1,[15,10]]
            self.Clear()
        elif key == "Hard":
            self.default = [0.25,[15,10]]
            self.Clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = TurretGame()
    game.show()
    sys.exit(app.exec_())
