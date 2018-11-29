from turret import Game
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
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
        self.StartGame()


    def StartGame(self):
        # Start
        self.turret = Game()
        self.turret.Setting(0.25, [20,10])
        self.turret.newGame()
        list = self.turret.getArray()
        n = list[0]
        m = list[1]

        # Layout
        turretLayout = QGridLayout()

        # Button
        self.turretButton = [[0 for j in range(m)] for i in range(n)]
        for y in range(n):
            for x in range(m):
                self.turretButton[y][x] = Button(self.Event, x, y)
        for y in range(n):
            for x in range(m):
                turretLayout.addWidget(self.turretButton[y][x], y, x)

        self.setLayout(turretLayout)

        self.setWindowTitle("Turret Game")

    def Event(self):
        button = self.sender()
        button.set(self.turret.getCoordinate(button.Y, button.X))
        if self.turret.getCoordinate(button.Y, button.X) == "*":
            self.Boom()

    def Boom(self):
        print("Boom!!!")
        list = self.turret.getArray()
        n = list[0]
        m = list[1]
        for y in range(n):
            for x in range(m):
                self.turretButton[y][x].set(self.turret.getCoordinate(self.turretButton[y][x].Y, self.turretButton[y][x].X))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = TurretGame()
    game.show()
    sys.exit(app.exec_())

