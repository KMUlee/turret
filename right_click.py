import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setFixedSize(QtCore.QSize(20, 20))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setFixedSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setFixedSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setFixedSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_1.installEventFilter(self)
        self.pushButton_2.installEventFilter(self)
        self.pushButton_3.installEventFilter(self)
        self.pushButton_4.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                print(obj.objectName(), "Left click")
            elif event.button() == QtCore.Qt.RightButton:
                print(obj.objectName(), "Right click")
            elif event.button() == QtCore.Qt.MiddleButton:
                print(obj.objectName(), "Middle click")
        return QtCore.QObject.event(obj, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())