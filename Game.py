from turret import Game
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy

class Button(QToolButton):

    def __init__(self,callback,x,y):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.clicked.connect(callback)
        self.X = x
        self.Y = y

    def set(self, text):
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 10)
        size.setWidth(max(size.width(), size.height()))
        return size

    def getCoordinate(self):
        pass



class TurretGame(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.default = [0.1, [20, 10]]
        self.StartGame()

        #Layout
        mainLayout = QVBoxLayout()

        #Button
        reStart = Button(self.Clear, 0, 0)
        reStart.set("START!!")
        mainLayout.addWidget(reStart)

        mainLayout.addLayout(self.turretLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Turret Game")


    def StartGame(self):
        # Start
        self.turret = Game()
        self.turret.Setting(self.default[0],self.default[1])
        self.turret.newGame()
        list = self.turret.getArray()
        n = list[0]
        m = list[1]

        # Layout
        self.turretLayout = QGridLayout()

        # Button
        self.turretButton = [[0 for j in range(m)] for i in range(n)]
        for y in range(n):
            for x in range(m):
                self.turretButton[y][x] = Button(self.Event, x, y)
        for y in range(n):
            for x in range(m):
                self.turretLayout.addWidget(self.turretButton[y][x], y, x)


    def Event(self):
        button = self.sender()
        button.set(self.turret.getCoordinate(button.Y, button.X))
        Coor = self.turret.getCoordinate(button.Y, button.X)
        if self.turret.getCoordinate(button.Y, button.X) == "*":
            self.Boom()


    def find(self,x,y):
        if self.turret.getCoordinate(x, y) == "0":
            self.find(x,y)
        self.turretButton[y][x].set(self.turret.getCoordinate(x, y))




    def Boom(self):
        list = self.turret.getArray()
        n = list[0]
        m = list[1]
        for y in range(n):
            for x in range(m):
                self.turretButton[y][x].set(self.turret.getCoordinate(self.turretButton[y][x].Y, self.turretButton[y][x].X))

    def Clear(self):
        list = self.turret.getArray()
        n = list[0]
        m = list[1]
        for y in range(n):
            for x in range(m):
                self.turretButton[y][x].set('')
                self.turretButton[y][x].setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = TurretGame()
    game.show()
    sys.exit(app.exec_())

