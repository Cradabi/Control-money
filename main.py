import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
import datetime

from Main_Window import Ui_MainWindow
from Add_transaction import Ui_Dialog
import qdarktheme


class SecondWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.subButton.clicked.connect(self.submit)

    def submit(self):
        self.label_5.hide()
        self.label_6.hide()
        self.text1 = self.textEdit.text()
        self.text2 = self.textEdit_2.text()
        self.combotext = self.comboBox1.currentText()
        print(self.text1, self.text2, self.combotext)
        if self.text1 == '' and self.text2 == '':
            self.label_5.show()
            self.label_6.show()
        elif self.text1 == '':
            self.label_5.show()
        elif self.text2 == '':
            self.label_6.show()
        else:
            try:
                self.int_text_2 = int(self.text2)
                if self.combotext == "Пополнение":
                    if self.int_text_2 >= 0:
                        datetime_obj = datetime.date.today()
                        self.add_transaction(self.text1, self.combotext, datetime_obj, self.int_text_2)
                    else:
                        datetime_obj = datetime.date.today()
                        self.add_transaction(self.text1, self.combotext, datetime_obj, self.int_text_2*(-1))
                else:
                    if self.int_text_2 <= 0:
                        datetime_obj = datetime.date.today()
                        self.add_transaction(self.text1, self.combotext, datetime_obj, self.int_text_2)
                    else:
                        datetime_obj = datetime.date.today()
                        self.add_transaction(self.text1, self.combotext, datetime_obj, self.int_text_2*(-1))
                if application.searching_category != '':
                    s_c = application.searching_category.lower()
                    s_c = s_c.capitalize()
                    application.a = application.search_by_category(s_c)
                    application.chng()
                elif application.searching_date != '':
                    application.a = application.search_by_date(application.searching_date)
                    application.chng()
                else:
                    application.a = application.sort_by_cost()
                    application.chng()
                self.textEdit.setText('')
                self.textEdit_2.setText('')
                self.close()
            except:
                self.label_6.setText("Введите положительное число!!!")
                self.label_6.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.submit()

    def get_last_id(self):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )
        cur = con.cursor()
        per1 = cur.execute('''SELECT * FROM control_money;''')
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
        last_id = int(self.get_last_id()) + 1
        cur.execute("INSERT INTO control_money (id, name, category, date, cost) VALUES (%s, %s, %s, %s, %s)",
                    (last_id, name, category, date, int(cost),))

        con.commit()
        con.close()


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.s = SecondWindow()
        self.balance = 0

        self.searching_date = ''
        self.searching_category = ''

        self.setupUi(self)
        self.addButton.clicked.connect(self.show_add_window)
        self.clear_sortbutton.clicked.connect(self.clear_sorting)

        self.a = self.sort_by_cost()

        self.combo.currentIndexChanged.connect(self.chng)
        self.chng()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            if self.textEdit.text() != '' and self.textEdit_2.text() != '':
                self.label_5.show()
            elif self.textEdit_2.text() != '':
                self.label_5.hide()
                print('sbn')
                s_c = self.textEdit_2.text().lower()
                s_c = s_c.capitalize()
                self.a = self.search_by_category(s_c)
                self.searching_category = self.textEdit_2.text()
                self.clear_sortbutton.show()
                self.chng()
            elif self.textEdit.text() != '':
                print('sbn2')
                self.label_5.hide()
                try:
                    self.a = self.search_by_date(self.textEdit.text())
                    self.searching_date = self.textEdit.text()
                    self.clear_sortbutton.show()
                    self.chng()
                except:
                    print("sdgx")
                    self.label_5.setText("Вы ввели некорректную дату")
                    self.label_5.show()
        elif event.key() == Qt.Key_Backspace:
            try:
                row_index = self.table.currentIndex().row()
                x = []
                for i in range(4):
                    x.append(self.table.item(row_index, i).text())
                print(x)
                self.table.removeRow(row_index)
                self.delete_transaction(x[0], x[1], x[3])
                if self.searching_category != '':
                    s_c = self.searching_category.lower()
                    s_c = s_c.capitalize()
                    self.a = self.search_by_category(s_c)
                    self.chng()
                elif self.searching_date != '':
                    self.a = self.search_by_date(self.searching_date)
                    self.chng()
                else:
                    self.a = self.sort_by_cost()
                    self.chng()
            except:
                pass
        elif event.key() == Qt.Key_Control:
            if self.theme == 'light':
                qdarktheme.setup_theme('dark')
                self.theme = 'dark'
            elif self.theme == 'dark':
                qdarktheme.setup_theme('light')
                self.theme = 'light'

    def show_add_window(self):
        self.s.show()

    def clear_sorting(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.clear_sortbutton.hide()
        self.searching_date = ''
        self.searching_category = ''
        self.a = self.sort_by_cost()
        self.chng()

    def delete_transaction(self, name, category, cost):
        print("delete")
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        per = cur.execute('''DELETE FROM control_money WHERE name = %s AND  category = %s''',
                          (name, category,))
        con.commit()
        con.close()

    def search_by_category(self, category):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        per = cur.execute('''SELECT name, category, date, cost FROM control_money WHERE category = %s ORDER BY cost''',
                          (category,))

        a = cur.fetchall()
        con.commit()
        con.close()
        return a

    def search_by_date(self, date):
        print(date)
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        per = cur.execute('''SELECT name, category, date, cost FROM control_money WHERE date = %s ORDER BY cost''',
                          (date,))

        a = cur.fetchall()
        con.commit()
        con.close()
        return a

    def chng(self):
        print(self.combo.currentIndex())
        self.balance = 0
        if self.combo.currentIndex() == 0:
            self.table.setColumnCount(4)  # Set three columns
            self.table.setRowCount(len(self.a))
            self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Дата", "Стоимость"])

            self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
            self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

            self.table.setColumnWidth(0, 174)
            self.table.setColumnWidth(1, 175)
            self.table.setColumnWidth(2, 175)
            self.table.setColumnWidth(3, 175)

            self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

            for i in range(len(self.a)):
                item1 = QtWidgets.QTableWidgetItem(str(self.a[i][0]))
                item1.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 0, item1)

                item2 = QtWidgets.QTableWidgetItem(str(self.a[i][1]))
                item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 1, item2)

                item3 = QtWidgets.QTableWidgetItem(str(self.a[i][2]))
                item3.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 2, item3)

                item4 = QtWidgets.QTableWidgetItem(str(self.a[i][3]))
                item4.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 3, item4)
                self.balance += self.a[i][3]

            self.group_box.addWidget(self.table)
            self.frame.setLayout(self.group_box)
            self.label_6.setText("Текущий баланс: " + str(self.balance))

        elif self.combo.currentIndex() == 1:
            self.a.reverse()
            self.table.setColumnCount(4)  # Set three columns
            self.table.setRowCount(len(self.a))
            self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Дата", "Стоимость"])

            self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
            self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

            self.table.setColumnWidth(0, 174)
            self.table.setColumnWidth(1, 175)
            self.table.setColumnWidth(2, 175)
            self.table.setColumnWidth(3, 175)

            self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
            self.table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)

            for i in range(len(self.a)):
                item1 = QtWidgets.QTableWidgetItem(str(self.a[i][0]))
                item1.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 0, item1)

                item2 = QtWidgets.QTableWidgetItem(str(self.a[i][1]))
                item2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 1, item2)

                item3 = QtWidgets.QTableWidgetItem(str(self.a[i][2]))
                item3.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 2, item3)

                item4 = QtWidgets.QTableWidgetItem(str(self.a[i][3]))
                item4.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.AlignHCenter)
                self.table.setItem(i, 3, item4)
                self.balance += self.a[i][3]
            self.group_box.addWidget(self.table)
            self.frame.setLayout(self.group_box)
            self.label_6.setText("Текущий баланс: " + str(self.balance))
            self.a.reverse()

    def get_last_id(self):
        con = psycopg2.connect(
            database='testuser',
            user='postgres',
            password='MaximRozov24',
            host='localhost',
            port='5432'
        )

        cur = con.cursor()
        per1 = cur.execute('''SELECT * FROM control_money;''')
        a = cur.fetchall()[-1][0]
        con.commit()
        con.close()
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
        last_id = int(self.get_last_id()) + 1
        cur.execute("INSERT INTO control_money (id, name, category, date, cost) VALUES (%s, %s, %s, %s, %s)",
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
        per = cur.execute('''SELECT name, category, date, cost FROM control_money ORDER BY cost''')
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
