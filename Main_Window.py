# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(24)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        a = main.sort_by_cost()

        group_box = QtWidgets.QVBoxLayout()

        self.table = QtWidgets.QTableWidget()  # Create a table
        self.table.setFont(QtGui.QFont('MS Shell Dlg', 14))
        self.table.setColumnCount(3)  # Set three columns
        self.table.setRowCount(len(a))
        self.table.setHorizontalHeaderLabels(["Имя", "Категория", "Стоимость"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)

        for i in range(len(a)):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(a[i][0]), Qt.AlignCenter))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a[i][1]), Qt.AlignCenter))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(a[i][2]), Qt.AlignCenter))

        group_box.addWidget(self.table)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setLayout(group_box)
        self.scrollArea.setGeometry(QtCore.QRect(110, 150, 561, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedHeight(280)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(24)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(632, 451, 111, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.addButton.setFont(font)
        self.addButton.setMouseTracking(False)
        self.addButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addButton.setObjectName("addButton")

        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(132, 451, 150, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.updateButton.setFont(font)
        self.updateButton.setMouseTracking(False)
        self.updateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.updateButton.setObjectName("updateButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(620, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 120, 131, 21))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(29, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(470, 120, 131, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Контроль денег"))
        self.label.setText(_translate("MainWindow", " Контроль денег"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.updateButton.setText(_translate("MainWindow", "Обновить"))
        self.checkBox.setText(_translate("MainWindow", "Отсортировать"))
        self.label_2.setText(_translate("MainWindow", "Поиск по дате:"))
        self.label_3.setText(_translate("MainWindow", "Поиск по категории:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
