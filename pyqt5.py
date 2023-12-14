import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from itertools import permutations

# from PyQt5.uic.properties import QtCore

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.mass = []
        self.words = []

        self.centrw = QWidget()
        self.setCentralWidget(self.centrw)
        self.setWindowTitle("Password generator")
        self.resize(900, 500)
        self.centrw.setStyleSheet("background-color: rgb(38, 38, 38); "
                                  "color: rgb(255, 255, 255);")

        self.btn_info = QPushButton(self)
        self.btn_info.setText("Інформація")
        self.btn_info.setFont(QFont("Arial", 12))
        self.btn_info.setStyleSheet("background-color: rgb(55, 55, 55); "
                                    "color: rgb(255, 255, 255);  "
                                    "font-weight: 700")
        self.btn_info.setMaximumHeight(40)
        self.btn_info.clicked.connect(self.btn_info_cl)

        self.text = QLabel(self)
        self.text.setText("Слова, які можна використовувати")
        self.text.setFont(QFont("Arial", 12))
        self.text.setStyleSheet("color: rgb(255, 255, 255);  "
                                "font-weight: 700;")
        self.text.setMaximumHeight(30)

        self.text_input = QPlainTextEdit(self)
        self.text_input.setFont(QFont("Arial", 14))
        self.text_input.setStyleSheet("background-color: rgb(55, 55, 55); "
                                      "color: rgb(255, 255, 255);  "
                                      "font-weight: 700;")
        self.text_input.setMaximumHeight(120)

        self.btn_clear = QPushButton(self)
        self.btn_clear.setText("Очистити")
        self.btn_clear.setFont(QFont("Arial", 12))
        self.btn_clear.setStyleSheet("background-color: rgb(55, 55, 55); "
                                   "color: rgb(255, 255, 255);  "
                                   "font-weight: 700")
        self.btn_clear.setMaximumHeight(40)
        self.btn_clear.clicked.connect(self.btn_clear_cl)

        self.btn_gen = QPushButton(self)
        self.btn_gen.setText("Генерація")
        self.btn_gen.setFont(QFont("Arial", 12))
        self.btn_gen.setStyleSheet("background-color: rgb(55, 55, 55); "
                                   "color: rgb(255, 255, 255);  "
                                   "font-weight: 700")
        self.btn_gen.setMaximumHeight(40)
        self.btn_gen.clicked.connect(self.btn_gen_cl)

        self.answer = QTextEdit(self)
        self.answer.setFont(QFont("Arial", 12))
        self.answer.setStyleSheet("color: rgb(255, 255, 255);  "
                                  "font-weight: 700;")
        self.answer.setMaximumHeight(130)

        self.g = QGridLayout(self.centrw)
        self.g.addWidget(self.btn_info, 1, 2)
        self.g.addWidget(self.text, 2, 1, 1, 2)
        self.g.addWidget(self.text_input, 3, 1, 1, 2)
        self.g.addWidget(self.btn_clear, 4, 1)
        self.g.addWidget(self.btn_gen, 4, 2)
        self.g.addWidget(self.answer, 5, 1, 1, 2)


    def btn_info_cl(self):
        w = Info()
        w.exec_()

    def btn_clear_cl(self):
        self.text_input.clear()
        self.answer.clear()
        self.words.clear()

    def btn_gen_cl(self):
        text = self.text_input.toPlainText()
        self.mass = text.split()

        min_el_pass = 8
        for i in range(1, min_el_pass, +1):
            slova = permutations(self.mass, i)

            for comb in slova:
                word = ''.join(comb)
                if len(word) >= min_el_pass:
                    self.words.append(word)

        ewq = ",    ".join(self.words)
        self.answer.setText(f'Кількість сгенерованих паролів: {len(self.words)} \n {ewq}')

class Info(QDialog):
    def __init__(self):
        super(Info, self).__init__()

        layout = QVBoxLayout(self)
        self.setWindowTitle("Інформація")
        self.resize(400, 250)
        self.setStyleSheet("background-color: rgb(38, 38, 38); "
                                  "color: rgb(255, 255, 255);")
        text_ = "Ця програма генерує паролі. Вона в хаотичному стані розcтавляє введені вами слова, не розділяючи їх."

        self.text = QLabel(self)
        self.text.setFont(QFont("Arial", 12))
        self.text.setStyleSheet("color: rgb(255, 255, 255);"
                                  "font-weight: 700;")
        self.text.setWordWrap(True)
        self.text.setText(text_)

        layout.addWidget(self.text)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    w = Window()
    w.show()
    sys.exit(app.exec_())

"""
- мкс к-сть ел у паролі вводить користувач
"""
