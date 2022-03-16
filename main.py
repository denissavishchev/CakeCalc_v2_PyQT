import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from front_ui import Ui_MainWindow

class CakeCalc(QtWidgets.QMainWindow):
    def __init__(self):
        super(CakeCalc, self).__init__()
        self.front_ui = Ui_MainWindow()
        self.front_ui.setupUi(self)
        self.init_UI()



    def init_UI(self):
        self.setWindowTitle('CakeCalculator')
        self.setWindowIcon(QIcon('img/circle.png'))
        self.front_ui.result.clicked.connect(self.result_button)

        self.front_ui.circle_top.clicked.connect(self.circle_top_button)
        self.front_ui.square_top.clicked.connect(self.square_top_button)
        self.front_ui.rect_top.clicked.connect(self.rect_top_button)

        self.front_ui.circle_bottom.clicked.connect(self.circle_bottom_button)
        self.front_ui.square_bottom.clicked.connect(self.square_bottom_button)
        self.front_ui.rect_bottom.clicked.connect(self.rect_bottom_button)

    top = 0
    bot = 0

    def circle_top_button(self):
        self.top = 1
        self.front_ui.circle_top.setStyleSheet("QPushButton{\n"
                                                "    border-radius: 15;\n"
                                                "    background-color: rgba(17,52,82,.9);\n"
                                                "    border: 2px solid rgba(255,255,255,.5);\n""}")
        self.front_ui.square_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.rect_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")

        self.front_ui.inputRT.setHidden(True)
        self.front_ui.inputLT.setPlaceholderText('Diameter')

    def square_top_button(self):
        self.top = 2
        self.front_ui.circle_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.square_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.9);\n"
                                               "    border: 2px solid rgba(255,255,255,.5);\n""}")
        self.front_ui.rect_top.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15;\n"
                                             "    background-color: rgba(17,52,82,.8);\n"
                                             "    border: 10px solid rgba(17,52,82,.5);\n""}")

        self.front_ui.inputRT.setHidden(True)
        self.front_ui.inputLT.setPlaceholderText('Side length')

    def rect_top_button(self):
        self.top = 3
        self.front_ui.circle_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.square_top.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.rect_top.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15;\n"
                                             "    background-color: rgba(17,52,82,.9);\n"
                                             "    border: 2px solid rgba(255,255,255,.5);\n""}")

        self.front_ui.inputRT.setHidden(False)
        self.front_ui.inputLT.setPlaceholderText('Length')
        self.front_ui.inputRT.setPlaceholderText('Height')


    def circle_bottom_button(self):
        self.bot = 1
        self.front_ui.circle_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.9);\n"
                                               "    border: 2px solid rgba(255,255,255,.5);\n""}")
        self.front_ui.square_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.rect_bottom.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15;\n"
                                             "    background-color: rgba(17,52,82,.8);\n"
                                             "    border: 10px solid rgba(17,52,82,.5);\n""}")

        self.front_ui.inputRD.setHidden(True)
        self.front_ui.inputLD.setPlaceholderText('Diameter')

    def square_bottom_button(self):
        self.bot = 2
        self.front_ui.circle_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.square_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.9);\n"
                                               "    border: 2px solid rgba(255,255,255,.5);\n""}")
        self.front_ui.rect_bottom.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15;\n"
                                             "    background-color: rgba(17,52,82,.8);\n"
                                             "    border: 10px solid rgba(17,52,82,.5);\n""}")

        self.front_ui.inputRD.setHidden(True)
        self.front_ui.inputLD.setPlaceholderText('Side length')

    def rect_bottom_button(self):
        self.bot = 3
        self.front_ui.circle_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.square_bottom.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 15;\n"
                                               "    background-color: rgba(17,52,82,.8);\n"
                                               "    border: 10px solid rgba(17,52,82,.5);\n""}")
        self.front_ui.rect_bottom.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 15;\n"
                                             "    background-color: rgba(17,52,82,.9);\n"
                                             "    border: 2px solid rgba(255,255,255,.5);\n""}")

        self.front_ui.inputRD.setHidden(False)
        self.front_ui.inputLD.setPlaceholderText('Length')
        self.front_ui.inputRD.setPlaceholderText('Height')



    def result_button(self):
        LT = self.front_ui.inputLT.text()
        RT = self.front_ui.inputRT.text()
        LD = self.front_ui.inputLD.text()
        RD = self.front_ui.inputRD.text()
        resultField = '???'
        try:
            if self.top == 1 and self.bot == 1:
                resultField = str(round(float(LD) * (float(LD)) / (float(LT) * (float(LT))), 4))
            elif self.top == 1 and self.bot == 2:
                resultField = str(round((((float(LD)) * (float(LD))) / ((((float(LT)) / 2) * ((float(LT)) / 2)) * 3.1415)), 4))
            elif self.top == 1 and self.bot == 3:
                resultField = str(round((((float(LD)) * (float(RD))) / ((((float(LT)) / 2) * ((float(LT)) / 2)) * 3.1415)), 4))

            elif self.top == 2 and self.bot == 1:
                resultField = str(round((((((float(LD)) / 2) * ((float(LD)) / 2)) * 3.1415)) / ((float(LT)) * (float(LT))), 4))
            elif self.top == 2 and self.bot == 2:
                resultField = str(round((((float(LD)) * (float(LD))) / ((float(LT)) * (float(LT)))), 4))
            elif self.top == 2 and self.bot == 3:
                resultField = str(round((((float(LD)) * (float(RD))) / ((float(LT)) * (float(LT)))), 4))

            elif self.top == 3 and self.bot == 1:
                resultField = str(round((((((float(LD)) / 2) * ((float(LD)) / 2)) * 3.1415)) / ((float(LT)) * (float(RT))), 4))
            elif self.top == 3 and self.bot == 2:
                resultField = str(round((((float(LD)) * (float(LD))) / ((float(LT)) * (float(RT)))), 4))
            elif self.top == 3 and self.bot == 3:
                resultField = str(round((((float(LD)) * (float(RD))) / ((float(LT)) * (float(RT)))), 4))
        except:
            resultField = 'Empty Fields'
        self.front_ui.nameLabel_2.setText(str(resultField))


app = QtWidgets.QApplication([])
application = CakeCalc()
application.show()

sys.exit(app.exec())