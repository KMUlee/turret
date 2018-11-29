from turret import Game
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy

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
        self.turretButton = []
        self.default = [0.5, [20, 10]]
        self.StartGame()

        #Layout
        mainLayout = QVBoxLayout()
        turretLayout = QGridLayout()

        #Button
        reStart = Button(self.Clear,"START!!", 0, 0)
        mainLayout.addWidget(reStart)
        self.turretButton = [[0 for j in range(self.default[1][1])] for i in range(self.default[1][0])]
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x] = Button(self.Event, '', x, y)
                turretLayout.addWidget(self.turretButton[y][x], y, x)

        mainLayout.addLayout(turretLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Turret Game")


    def StartGame(self):
        # Start
        self.turret = Game()
        self.turret.Setting(self.default[0],self.default[1])
        self.turret.newGame()

    def Event(self):
        button = self.sender()
        button.set(self.turret.getCoordinate(button.Y, button.X))
        Coor = self.turret.getCoordinate(button.Y, button.X)
        if button.text() == "*":
            self.Boom()

    def Boom(self):
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x].set(self.turret.getCoordinate(self.turretButton[y][x].Y, self.turretButton[y][x].X))

    def Clear(self):
        for y in range(self.default[1][0]):
            for x in range(self.default[1][1]):
                self.turretButton[y][x].set('')
        self.StartGame()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = TurretGame()
    game.show()
    sys.exit(app.exec_())