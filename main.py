# import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

from Main_Window import Ui_MainWindow


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.setupUi(self)
        self.combo.currentIndexChanged.connect(self.chng)

        self.table.setColumnCount(4)  # Set three columns
        self.table.setRowCount(40)
        self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Дата", "Стоимость"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

        self.table.setColumnWidth(0, 180)
        self.table.setColumnWidth(1, 180)
        self.table.setColumnWidth(2, 180)
        self.table.setColumnWidth(3, 180)

        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

        for i in range(40):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('Куртка', Qt.AlignCenter))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem('Одежда', Qt.AlignCenter))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem('12-3-2023', Qt.AlignCenter))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem('5000', Qt.AlignCenter))

        self.group_box.addWidget(self.table)
        self.frame.setLayout(self.group_box)

    def chng(self):

        if self.combo.currentIndex() == 0:
            self.table.setColumnCount(4)  # Set three columns
            self.table.setRowCount(40)
            self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Дата", "Стоимость"])

            self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
            self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

            self.table.setColumnWidth(0, 180)
            self.table.setColumnWidth(1, 180)
            self.table.setColumnWidth(2, 180)
            self.table.setColumnWidth(3, 180)

            self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

            for i in range(40):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('Куртка', Qt.AlignCenter))
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem('Одежда', Qt.AlignCenter))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem('12-3-2023', Qt.AlignCenter))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem('5000', Qt.AlignCenter))

            self.group_box.addWidget(self.table)
            self.frame.setLayout(self.group_box)

        elif self.combo.currentIndex() == 1:
            self.table.setColumnCount(4)  # Set three columns
            self.table.setRowCount(40)
            self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Дата", "Стоимость"])

            self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
            self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

            self.table.setColumnWidth(0, 180)
            self.table.setColumnWidth(1, 180)
            self.table.setColumnWidth(2, 180)
            self.table.setColumnWidth(3, 180)

            self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

            for i in range(40):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem('Носки', Qt.AlignCenter))
                self.table.setItem(i, 1, QtWidgets.QTableWidgetItem('Одежда', Qt.AlignCenter))
                self.table.setItem(i, 2, QtWidgets.QTableWidgetItem('12-3-2023', Qt.AlignCenter))
                self.table.setItem(i, 3, QtWidgets.QTableWidgetItem('300', Qt.AlignCenter))

            self.group_box.addWidget(self.table)
            self.frame.setLayout(self.group_box)

    def get_last_id(self):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        per1 = cur.execute('''SELECT * FROM Control_money;''')

        a = cur.fetchall()[-1][0]
        return a

    def add_transaction(self, name, category, date, cost):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )
        cur = con.cursor()
        last_id = int(get_last_id()) + 1
        cur.execute("INSERT INTO Control_money (id, name, category, date, cost) VALUES (%s, %s, %s, %s, %s)",
                    (last_id, name, category, date, int(cost),))

        con.commit()
        con.close()

    def sort_by_cost(self):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        # per = cur.execute('''CREATE  table Control_money( id INTEGER, name VARCHAR(50), category VARCHAR(50), cost INTEGER);''')
        # per = cur.execute(
        #    '''INSERT INTO Control_money (id, name, category, cost) VALUES ('1', 'куртка', 'одежда', '7000');''')
        per = cur.execute('''SELECT name, category, date, cost FROM Control_money ORDER BY cost''')

        a = cur.fetchall()
        con.commit()
        con.close()
        print(a)
        return a

    def sort_by_cost_reverse(self):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        # per = cur.execute('''CREATE  table Control_money( id INTEGER, name VARCHAR(50), category VARCHAR(50), cost INTEGER);''')
        # per = cur.execute(
        #    '''INSERT INTO Control_money (id, name, category, cost) VALUES ('1', 'куртка', 'одежда', '7000');''')
        per = cur.execute('''SELECT name, category, date, cost FROM Control_money ORDER BY cost DESC''')

        a = cur.fetchall()
        con.commit()
        con.close()
        print(a)
        return a


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec())
