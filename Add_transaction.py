# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_transaction.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 442)
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(360, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox1 = QtWidgets.QComboBox(Dialog)
        self.comboBox1.setGeometry(QtCore.QRect(360, 190, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox1.setFont(font)
        self.comboBox1.setObjectName("comboBox")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(630, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color: red")
        self.label_5.hide()

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(200, 300, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color: red")
        self.label_6.hide()

        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(360, 260, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.subButton = QtWidgets.QPushButton(Dialog)
        self.subButton.setGeometry(QtCore.QRect(420, 370, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.subButton.setFont(font)
        self.subButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая транзакция"))
        self.label.setText(_translate("Dialog", "Новая транзакция"))
        self.label_2.setText(_translate("Dialog", "Напишите название покупки:"))
        self.comboBox1.setItemText(0, _translate("Dialog", "Пополнение"))
        self.comboBox1.setItemText(1, _translate("Dialog", "Одежда"))
        self.comboBox1.setItemText(2, _translate("Dialog", "Продукты"))
        self.comboBox1.setItemText(3, _translate("Dialog", "Транспорт"))
        self.comboBox1.setItemText(4, _translate("Dialog", "Медицина"))
        self.comboBox1.setItemText(5, _translate("Dialog", "Подарки"))
        self.comboBox1.setItemText(6, _translate("Dialog", "Образование"))
        self.comboBox1.setItemText(7, _translate("Dialog", "Электроника"))
        self.comboBox1.setItemText(8, _translate("Dialog", "Развлечения"))
        self.comboBox1.setItemText(9, _translate("Dialog", "Подписки"))
        self.comboBox1.setItemText(10, _translate("Dialog", "Прочее"))
        self.label_3.setText(_translate("Dialog", "Добавте категорию:"))
        self.label_4.setText(_translate("Dialog", "Введите стоимость:"))
        self.label_5.setText(_translate("Dialog", "Введите имя!!!"))
        self.label_6.setText(_translate("Dialog", "Введите цену!!!"))
        self.subButton.setText(_translate("Dialog", "Добавить транзакцию"))
