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


    def circle_top_button(self):
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

    def square_top_button(self):
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

    def rect_top_button(self):
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


    def circle_bottom_button(self):
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

    def square_bottom_button(self):
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

    def rect_bottom_button(self):
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


    def result_button(self):

        print('button')


app = QtWidgets.QApplication([])
application = CakeCalc()
application.show()

sys.exit(app.exec())