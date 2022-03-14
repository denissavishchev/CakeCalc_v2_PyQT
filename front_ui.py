
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 340, 620))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius: 10;\n"
"    background-image: url(img/bg.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.circle_top = QtWidgets.QPushButton(self.frame)
        self.circle_top.setGeometry(QtCore.QRect(10, 70, 100, 100))
        self.circle_top.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.circle_top.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.circle_top.setIcon(icon)
        self.circle_top.setIconSize(QtCore.QSize(100, 100))
        self.circle_top.setObjectName("circle_top")
        self.square_top = QtWidgets.QPushButton(self.frame)
        self.square_top.setGeometry(QtCore.QRect(120, 70, 100, 100))
        self.square_top.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.square_top.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.square_top.setIcon(icon1)
        self.square_top.setIconSize(QtCore.QSize(80, 80))
        self.square_top.setObjectName("square_top")
        self.rect_top = QtWidgets.QPushButton(self.frame)
        self.rect_top.setGeometry(QtCore.QRect(230, 70, 100, 100))
        self.rect_top.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.rect_top.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/rect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rect_top.setIcon(icon2)
        self.rect_top.setIconSize(QtCore.QSize(85, 85))
        self.rect_top.setObjectName("rect_top")
        self.circle_bottom = QtWidgets.QPushButton(self.frame)
        self.circle_bottom.setGeometry(QtCore.QRect(10, 300, 100, 100))
        self.circle_bottom.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.circle_bottom.setText("")
        self.circle_bottom.setIcon(icon)
        self.circle_bottom.setIconSize(QtCore.QSize(100, 100))
        self.circle_bottom.setObjectName("circle_bottom")
        self.square_bottom = QtWidgets.QPushButton(self.frame)
        self.square_bottom.setGeometry(QtCore.QRect(120, 300, 100, 100))
        self.square_bottom.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.square_bottom.setText("")
        self.square_bottom.setIcon(icon1)
        self.square_bottom.setIconSize(QtCore.QSize(80, 80))
        self.square_bottom.setObjectName("square_bottom")
        self.rect_bottom = QtWidgets.QPushButton(self.frame)
        self.rect_bottom.setGeometry(QtCore.QRect(230, 300, 100, 100))
        self.rect_bottom.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"}")
        self.rect_bottom.setText("")
        self.rect_bottom.setIcon(icon2)
        self.rect_bottom.setIconSize(QtCore.QSize(85, 85))
        self.rect_bottom.setObjectName("rect_bottom")
        self.inputLT = QtWidgets.QLineEdit(self.frame)
        self.inputLT.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.inputLT.setAutoFillBackground(False)
        self.inputLT.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(17,52,82,.8);\n"
"    color: rgba(255,255,255,1);\n"
"    border-radius: 10;\n"
"    border: 5px solid rgba(17,52,82,.5);\n"
"}\n"
"")
        self.inputLT.setText("")
        self.inputLT.setFrame(True)
        self.inputLT.setObjectName("inputLT")
        self.inputRT = QtWidgets.QLineEdit(self.frame)
        self.inputRT.setGeometry(QtCore.QRect(180, 220, 151, 31))
        self.inputRT.setAutoFillBackground(False)
        self.inputRT.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(17,52,82,.8);\n"
"    color: rgba(255,255,255,1);\n"
"    border-radius: 10;\n"
"    border: 5px solid rgba(17,52,82,.5);\n"
"}\n"
"")
        self.inputRT.setText("")
        self.inputRT.setFrame(True)
        self.inputRT.setObjectName("inputRT")
        self.inputLD = QtWidgets.QLineEdit(self.frame)
        self.inputLD.setGeometry(QtCore.QRect(10, 450, 151, 31))
        self.inputLD.setAutoFillBackground(False)
        self.inputLD.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(17,52,82,.8);\n"
"    color: rgba(255,255,255,1);\n"
"    border-radius: 10;\n"
"    border: 5px solid rgba(17,52,82,.5);\n"
"}\n"
"")
        self.inputLD.setText("")
        self.inputLD.setFrame(True)
        self.inputLD.setObjectName("inputLD")
        self.inputRD = QtWidgets.QLineEdit(self.frame)
        self.inputRD.setGeometry(QtCore.QRect(180, 450, 151, 31))
        self.inputRD.setAutoFillBackground(False)
        self.inputRD.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(17,52,82,.8);\n"
"    color: rgba(255,255,255,1);\n"
"    border-radius: 10;\n"
"    border: 5px solid rgba(17,52,82,.5);\n"
"}\n"
"")
        self.inputRD.setText("")
        self.inputRD.setFrame(True)
        self.inputRD.setObjectName("inputRD")
        self.result = QtWidgets.QPushButton(self.frame)
        self.result.setGeometry(QtCore.QRect(70, 520, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        self.result.setFont(font)
        self.result.setStyleSheet("QPushButton {\n"
"    border-radius: 15;\n"
"    background-color: rgba(17,52,82,.8);\n"
"    border: 10px solid rgba(17,52,82,.5);\n"
"    color: rgba(255,255,255,1);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(17,52,82,.9);\n"
"    border: 1px solid rgba(255,255,255,.5);\n"
"    color: rgba(255,255,255,.5);\n"
"}")
        self.result.setIconSize(QtCore.QSize(80, 80))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputLT.setPlaceholderText(_translate("MainWindow", "Diameter"))
        self.inputRT.setPlaceholderText(_translate("MainWindow", "Diameter"))
        self.inputLD.setPlaceholderText(_translate("MainWindow", "Diameter"))
        self.inputRD.setPlaceholderText(_translate("MainWindow", "Diameter"))
        self.result.setText(_translate("MainWindow", "Result"))
# import bg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
