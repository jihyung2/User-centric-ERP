# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from tkinter import *
from tkinter import messagebox
from PyQt5.QtCore import QCoreApplication

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_OtherWindow(object):

    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 56, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 56, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(110, 90, 221, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_PW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PW.setGeometry(QtCore.QRect(110, 130, 221, 20))
        self.lineEdit_PW.setObjectName("lineEdit_PW")
        self.pushButton_OK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OK.setGeometry(QtCore.QRect(100, 200, 81, 41))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_SIGNUP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SIGNUP.setGeometry(QtCore.QRect(250, 200, 81, 41))
        self.pushButton_SIGNUP.setObjectName("pushButton_SIGNUP")

        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        self.pushButton_OK.clicked.connect(self.login) # type: ignore
        self.pushButton_SIGNUP.clicked.connect(OtherWindow.close) # type: ignore

        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.label.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\"> 회원가입</span></p></body></html>"))
        self.label_2.setText(_translate("OtherWindow", "아이디"))
        self.label_3.setText(_translate("OtherWindow", "비밀번호"))
        self.pushButton_OK.setText(_translate("OtherWindow", "확인"))
        self.pushButton_SIGNUP.setText(_translate("OtherWindow", "취소"))


    def login(self):

        text = self.lineEdit_ID.text()
        text1 = self.lineEdit_PW.text()

        db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8', port=3306)


        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id FROM `idpw` WHERE id = %s", text)
        result = cursor.fetchone()

        if text == "" or text1 == "":
            messagebox.showerror('오류', '아이디와 비밀번호를 입력해주세요')

        elif result is not None:
            messagebox.showerror('오류', '아이디 중복')

        else:  # 에러 없을 시 작동
            messagebox.showinfo('성공', '회원가입 성공!')
            insert_data = [[text, text1]]
            insert_sql = "INSERT INTO `idpw` VALUES (%s, %s)"
            cursor.executemany(insert_sql, insert_data)
            cursor.execute("CREATE TABLE "+text+"ani (ani_name CHAR(50), ani_time DATE, ani_num INT(11), ani_jil CHAR(50))")
            cursor.execute("CREATE TABLE "+text+"plant (su_name CHAR(50), su_time DATE, su_kg INT(11))")
        db.commit()
        db.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())