#!/usr/bin/env python3
# coding=utf-8

import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/task.png'))
        self.label_img.setScaledContents(True)

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return: pass
        """
        i = 0

        while i < self.tableWidget.rowCount():
            random_num = randint(0, 101)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):

        if validation_of_data(self.tableWidget):
            i = 0
            j = 1

            multiplication_of_k_i = 1
            sum_of_k_i = 0
            sum_of_sin_cos = 0

            while i < self.tableWidget.rowCount():
                item = self.tableWidget.item(i, 0).text()
                if(int(item)>0):
                    sum_of_k_i += int(item)
                if (int(item)<0):
                    multiplication_of_k_i*= int(item)
                difference_of_sin_of_k_and_cos_of_k = (math.sin(
                    int(item))  - math.cos(int(item)) )
                sum_of_sin_cos += difference_of_sin_of_k_and_cos_of_k
                answer = (float(multiplication_of_k_i)+ sum_of_k_i)/ \
                         (sum_of_sin_cos**(1/2.0))

                self.tableWidget.setItem(i, j,
                                         QTableWidgetItem(str(format(answer, ".10f"))))
                i += 1

            self.label_error.setText('')
        else:
            self.label_error.setText('Введены некорректные данные!')

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()


def validation_of_data(table_widget):
    """
    проверяем данные на валидность
    :param table_widget: таблица с числами
    :return: True - данные корректны, False - есть некорректные данные
    """
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False

    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
