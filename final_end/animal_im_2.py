# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Erp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
import pymysql
from tkinter.tix import Select
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from tkinter import *
from tkinter import messagebox


rice_stack = 0
casaba_stack = 0
banana_stack = 0
sim_list = [0]  # rice, casaba, banana
name_list = ['rice', 'cassava', 'banana']
data_dic = {name: [] for name in name_list}
data_list = []


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 121, 591))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.rice_container = QtWidgets.QGroupBox(self.centralwidget)
        self.rice_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.rice_container.setObjectName("rice_container")
        self.rice_exit = QtWidgets.QPushButton(self.rice_container)
        self.rice_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.rice_exit.setObjectName("rice_exit")
        self.rice_Dateedit = QtWidgets.QDateEdit(self.rice_container)
        self.rice_Dateedit.setGeometry(QtCore.QRect(40, 90, 126, 25))
        self.rice_Dateedit.setObjectName("rice_Dateedit")
        self.rice_Dateedit.setDate(QDate.currentDate())
        self.rice_area_label = QtWidgets.QLabel(self.rice_container)
        self.rice_area_label.setGeometry(QtCore.QRect(40, 120, 120, 30))
        self.rice_area_label.setObjectName("rice_area_label")
        self.rice_lineedit = QtWidgets.QLineEdit(self.rice_container)
        self.rice_lineedit.setGeometry(QtCore.QRect(40, 150, 101, 25))
        self.rice_lineedit.setObjectName("rice_lineedit")
        self.rice_pushbutton = QtWidgets.QPushButton(self.rice_container)
        self.rice_pushbutton.setGeometry(QtCore.QRect(138, 203, 41, 31))
        self.rice_pushbutton.setObjectName("rice_pushbutton")
        self.cow_RadioButton = QtWidgets.QRadioButton(self.rice_container)
        self.cow_RadioButton.setGeometry(QtCore.QRect(40, 210, 85, 20))
        self.cow_RadioButton.setObjectName("RadioButton")
        self.cow_RadioButton_2 = QtWidgets.QRadioButton(self.rice_container)
        self.cow_RadioButton_2.setGeometry(QtCore.QRect(90, 210, 85, 20))
        self.cow_RadioButton_2.setObjectName("RadioButton_2")
        self.cow_label_3 = QtWidgets.QLabel(self.rice_container)
        self.cow_label_3.setGeometry(QtCore.QRect(40, 185, 100, 16))
        self.cow_label_3.setObjectName("cow_label_3")
        self.rice_result_label = QtWidgets.QLabel(self.rice_container)
        self.rice_result_label.setGeometry(QtCore.QRect(10, 180, 201, 381))
        self.rice_result_label.setObjectName("rice_result_label")
        self.casaba_container = QtWidgets.QGroupBox(self.centralwidget)
        self.casaba_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.casaba_container.setObjectName("casaba_container")
        self.ck_RadioButton = QtWidgets.QRadioButton(self.casaba_container)
        self.ck_RadioButton.setGeometry(QtCore.QRect(40, 210, 85, 20))
        self.ck_RadioButton.setObjectName("RadioButton")
        self.ck_RadioButton_2 = QtWidgets.QRadioButton(self.casaba_container)
        self.ck_RadioButton_2.setGeometry(QtCore.QRect(90, 210, 85, 20))
        self.ck_RadioButton_2.setObjectName("RadioButton_2")
        self.ck_label_3 = QtWidgets.QLabel(self.casaba_container)
        self.ck_label_3.setGeometry(QtCore.QRect(40, 185, 100, 16))
        self.ck_label_3.setObjectName("ck_label_3")
        self.casaba_exit = QtWidgets.QPushButton(self.casaba_container)
        self.casaba_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.casaba_exit.setObjectName("casaba_exit")
        self.casaba_Dateedit = QtWidgets.QDateEdit(self.casaba_container)
        self.casaba_Dateedit.setGeometry(QtCore.QRect(40, 90, 126, 25))
        self.casaba_Dateedit.setObjectName("casaba_Dateedit")
        self.casaba_Dateedit.setDate(QDate.currentDate())
        self.casaba_area_label = QtWidgets.QLabel(self.casaba_container)
        self.casaba_area_label.setGeometry(QtCore.QRect(40, 120, 120, 30))
        self.casaba_area_label.setObjectName("casaba_area_label")
        self.casaba_lineedit = QtWidgets.QLineEdit(self.casaba_container)
        self.casaba_lineedit.setGeometry(QtCore.QRect(40, 150, 101, 25))
        self.casaba_lineedit.setObjectName("casaba_lineedit")
        self.casaba_pushbutton = QtWidgets.QPushButton(self.casaba_container)
        self.casaba_pushbutton.setGeometry(QtCore.QRect(138, 203, 41, 31))
        self.casaba_pushbutton.setObjectName("casaba_pushbutton")
        self.casaba_result_label = QtWidgets.QLabel(self.casaba_container)
        self.casaba_result_label.setGeometry(QtCore.QRect(10, 170, 201, 381))
        self.casaba_result_label.setObjectName("casaba_result_label")
        self.banana_container = QtWidgets.QGroupBox(self.centralwidget)
        self.banana_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.banana_container.setObjectName("banana_container")
        self.banana_exit = QtWidgets.QPushButton(self.banana_container)
        self.banana_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.banana_exit.setObjectName("banana_exit")
        self.banana_Dateedit = QtWidgets.QDateEdit(self.banana_container)
        self.banana_Dateedit.setGeometry(QtCore.QRect(40, 90, 126, 25))
        self.banana_Dateedit.setObjectName("banana_Dateedit")
        self.banana_Dateedit.setDate(QDate.currentDate())
        self.banana_area_label = QtWidgets.QLabel(self.banana_container)
        self.banana_area_label.setGeometry(QtCore.QRect(40, 120, 120, 30))
        self.banana_area_label.setObjectName("banana_area_label")
        self.pig_RadioButton = QtWidgets.QRadioButton(self.banana_container)
        self.pig_RadioButton.setGeometry(QtCore.QRect(40, 210, 85, 20))
        self.pig_RadioButton.setObjectName("RadioButton")
        self.pig_RadioButton_2 = QtWidgets.QRadioButton(self.banana_container)
        self.pig_RadioButton_2.setGeometry(QtCore.QRect(90, 210, 85, 20))
        self.pig_RadioButton_2.setObjectName("RadioButton_2")
        self.pig_label_3 = QtWidgets.QLabel(self.banana_container)
        self.pig_label_3.setGeometry(QtCore.QRect(40, 185, 100, 16))
        self.pig_label_3.setObjectName("ck_label_3")
        self.banana_lineedit = QtWidgets.QLineEdit(self.banana_container)
        self.banana_lineedit.setGeometry(QtCore.QRect(40, 150, 101, 25))
        self.banana_lineedit.setObjectName("banana_lineedit")
        self.banana_pushbutton = QtWidgets.QPushButton(self.banana_container)
        self.banana_pushbutton.setGeometry(QtCore.QRect(138, 203, 41, 31))
        self.banana_pushbutton.setObjectName("banana_pushbutton")
        self.banana_result_label = QtWidgets.QLabel(self.banana_container)
        self.banana_result_label.setGeometry(QtCore.QRect(10, 170, 201, 381))
        self.banana_result_label.setObjectName("banana_result_label")
        self.farm_produce_container = QtWidgets.QGroupBox(self.centralwidget)
        self.farm_produce_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.farm_produce_container.setObjectName("farm_produce_container")
        self.farm_produce_combobox = QtWidgets.QComboBox(self.farm_produce_container)
        self.farm_produce_combobox.setGeometry(QtCore.QRect(70, 0, 101, 24))
        self.farm_produce_combobox.setObjectName("farm_produce_combobox")
        self.farm_produce_label = QtWidgets.QLabel(self.farm_produce_container)
        self.farm_produce_label.setGeometry(QtCore.QRect(10, 40, 201, 511))
        self.farm_produce_label.setObjectName("farm_produce_label")
        self.farm_produce_label.setAlignment(Qt.AlignCenter)
        self.rice_result_name = QtWidgets.QTextEdit(self. farm_produce_container)
        self.rice_result_name.setGeometry(QtCore.QRect(0, 30, 60, 381))
        self.rice_result_name.setObjectName("rice_result_name")
        self.rice_result_time = QtWidgets.QTextEdit(self.farm_produce_container)
        self.rice_result_time.setGeometry(QtCore.QRect(60, 30, 70, 381))
        self.rice_result_time.setObjectName("rice_result_time")
        self.rice_result_kg = QtWidgets.QTextEdit(self.farm_produce_container)
        self.rice_result_kg.setGeometry(QtCore.QRect(130, 30, 50, 381))
        self.rice_result_kg.setObjectName("rice_result_kg")
        self.rice_result_jil = QtWidgets.QTextEdit(self.farm_produce_container)
        self.rice_result_jil.setGeometry(QtCore.QRect(180, 30, 40, 381))
        self.rice_result_jil.setObjectName("rice_result_jil")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##############
        #   ACTION   #
        ##############
        self.farm_produce_container.setHidden(True)
        self.rice_container.setHidden(True)
        self.casaba_container.setHidden(True)
        self.banana_container.setHidden(True)


        self.treeWidget.clicked.connect(self.tree_onClick)
        self.rice_pushbutton.clicked.connect(self.rice_push_Button)
        self.casaba_pushbutton.clicked.connect(self.casaba_push_Button)
        self.banana_pushbutton.clicked.connect(self.banana_push_Button)
        self.farm_produce_combobox.currentIndexChanged.connect(self.farm_produce_OnClick)
        self.rice_exit.clicked.connect(MainWindow.close)
        self.casaba_exit.clicked.connect(MainWindow.close)
        self.banana_exit.clicked.connect(MainWindow.close)

    # 트리위젯 소분류 클릭 시, 해당 컨테이너 호출 함수(재클릭 시, 결과 라벨 숨김)

    def tree_onClick(self):
        getSelected = self.treeWidget.currentItem()
        if getSelected:
            print(getSelected.text(0))
            if (getSelected.text(0) == '가축'):
                self.farm_produce_container.setHidden(False)
                self.rice_container.setHidden(True)
                self.casaba_container.setHidden(True)
                self.banana_container.setHidden(True)

            elif (getSelected.text(0) == '소'):
                self.rice_container.setHidden(False)
                self.rice_result_label.setHidden(True)
                self.casaba_container.setHidden(True)
                self.banana_container.setHidden(True)
                self.farm_produce_container.setHidden(True)




            elif (getSelected.text(0) == '닭'):
                self.rice_container.setHidden(True)
                self.casaba_container.setHidden(False)
                self.casaba_result_label.setHidden(True)
                self.banana_container.setHidden(True)
                self.farm_produce_container.setHidden(True)

            else:
                self.rice_container.setHidden(True)
                self.casaba_container.setHidden(True)
                self.banana_container.setHidden(False)
                self.banana_result_label.setHidden(True)
                self.farm_produce_container.setHidden(True)

    def farm_produce_OnClick(self):
        Selected = self.farm_produce_combobox.currentText()
        if Selected:
            if Selected == '전체':
                with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
                id = self.id_json['id']
                print(id)

                out_s = ""
                for i in data_dic:
                    out_s += i + "\n"
                    for j in range(len(data_dic[i])):
                        out_s += str(data_dic[i][j][0]) + "  " + str(data_dic[i][j][1]) + "\n"
                self.farm_produce_label.setText(out_s)

                self.rice_result_name.clear()
                self.rice_result_time.clear()
                self.rice_result_kg.clear()
                self.rice_result_jil.clear()
                self.rice_result_name.setText("종류")
                self.rice_result_time.setText("시간")
                self.rice_result_kg.setText("번호")
                self.rice_result_jil.setText("질병")
                db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                     port=3306)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM "+id+"ani ")

                while (True):
                    result = cursor.fetchone()

                    if result == None:
                        break;
                    print(result["ani_name"], str(result["ani_time"]), str(result["ani_num"]),str(result["ani_jil"]))
                    self.rice_result_name.append(result["ani_name"])
                    self.rice_result_time.append(str(result["ani_time"]))
                    self.rice_result_kg.append(str(result["ani_num"]))
                    self.rice_result_jil.append(str(result["ani_jil"]))
            elif Selected == '소':
                with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
                id = self.id_json['id']
                print(id)
                # out_s1 = ""
                # for i in data_dic
                print(Selected)
                self.rice_result_name.clear()
                self.rice_result_time.clear()
                self.rice_result_kg.clear()
                self.rice_result_jil.clear()
                self.rice_result_name.setText("종류")
                self.rice_result_time.setText("시간")
                self.rice_result_kg.setText("번호")
                self.rice_result_jil.setText("질병")
                db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                     port=3306)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'cow'")

                while (True):
                    result = cursor.fetchone()

                    if result == None:
                        break;
                    print(result["ani_name"], str(result["ani_time"]), str(result["ani_num"]), str(result["ani_jil"]))
                    self.rice_result_name.append(result["ani_name"])
                    self.rice_result_time.append(str(result["ani_time"]))
                    self.rice_result_kg.append(str(result["ani_num"]))
                    self.rice_result_jil.append(str(result["ani_jil"]))
                db.commit()
                db.close()

            elif Selected == '닭':
                with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
                id = self.id_json['id']
                print(id)
                self.rice_result_name.clear()
                self.rice_result_time.clear()
                self.rice_result_kg.clear()
                self.rice_result_jil.clear()
                self.rice_result_name.setText("종류")
                self.rice_result_time.setText("시간")
                self.rice_result_kg.setText("번호")
                self.rice_result_jil.setText("질병")
                db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                     port=3306)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'chicken'")

                while (True):
                    result = cursor.fetchone()

                    if result == None:
                        break;
                    print(result["ani_name"], str(result["ani_time"]), str(result["ani_num"]), str(result["ani_jil"]))
                    self.rice_result_name.append(result["ani_name"])
                    self.rice_result_time.append(str(result["ani_time"]))
                    self.rice_result_kg.append(str(result["ani_num"]))
                    self.rice_result_jil.append(str(result["ani_jil"]))
                print(Selected)
                db.commit()
                db.close()
            else:
                with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
                id = self.id_json['id']
                print(id)
                print(Selected)
                self.rice_result_name.clear()
                self.rice_result_time.clear()
                self.rice_result_kg.clear()
                self.rice_result_jil.clear()
                self.rice_result_name.setText("종류")
                self.rice_result_time.setText("시간")
                self.rice_result_kg.setText("번호")
                self.rice_result_jil.setText("질병")
                db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                     port=3306)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'pig'")

                while (True):
                    result = cursor.fetchone()

                    if result == None:
                        break;
                    print(result["ani_name"], str(result["ani_time"]), str(result["ani_num"]), str(result["ani_jil"]))
                    self.rice_result_name.append(result["ani_name"])
                    self.rice_result_time.append(str(result["ani_time"]))
                    self.rice_result_kg.append(str(result["ani_num"]))
                    self.rice_result_jil.append(str(result["ani_jil"]))
                db.commit()
                db.close()
    # 각 컨테이너에 있는 버튼 클릭 후, 면적값 누적 함수

    def rice_push_Button(self):
        with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
        id = self.id_json['id']
        print(id)
        try:
            inputDate = self.rice_Dateedit.text()
            inputArea = int(self.rice_lineedit.text())

            name = 'cow'
            self.rice_lineedit.setText('')
            self.rice_result_label.setHidden(False)

            if self.cow_RadioButton.isChecked():
                a = "O"
            elif self.cow_RadioButton_2.isChecked():
                a = "X"

            self.rice_result_label.setText(inputDate + "\n소 번호는 " + str(inputArea) + "번 입니다.\n질병 유무는 " + a + " 입니다.")
            self.rice_result_label.setFont(QtGui.QFont("Nanum Gothic", 8))
            self.rice_result_label.setStyleSheet("Color : green")

            data_list = [name, inputDate, inputArea, a]

            db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                 port=3306)
            cursor = db.cursor(pymysql.cursors.DictCursor)

            try:
                cursor.execute("INSERT INTO "+id+"ani VALUES (%s ,%s ,%s, %s)", data_list)
            except:  # 에러발생 시 작동
                messagebox.showerror('오류', '데이터 입력 오류가 발생함')
            else:  # 에러 없을 시 작동
                messagebox.showinfo('성공', '데이터 입력 성공')
            db.commit()
            db.close()

        except ValueError:
            print("잘못된 값 입력")
            self.rice_lineedit.setText('')
            self.rice_result_label.setHidden(False)
            self.rice_result_label.setText("잘못된 값 입력")
            self.rice_result_label.setFont(QtGui.QFont("Nanum Gothic", 15))
            self.rice_result_label.setStyleSheet("Color : red")

    def casaba_push_Button(self):
        with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
        id = self.id_json['id']
        print(id)
        try:
            inputDate = self.casaba_Dateedit.text()
            inputArea = int(self.casaba_lineedit.text())

            name = 'chicken'
            self.casaba_lineedit.setText('')
            self.casaba_result_label.setHidden(False)

            if self.ck_RadioButton.isChecked():
                a = "O"
            elif self.ck_RadioButton_2.isChecked():
                a = "X"

            self.casaba_result_label.setText(inputDate + "\n닭 번호는 " + str(inputArea) + "번 입니다.\n질병 유무는 " + a + " 입니다.")
            self.casaba_result_label.setFont(QtGui.QFont("Nanum Gothic", 8))
            self.casaba_result_label.setStyleSheet("Color : green")

            data_list = [name, inputDate, inputArea, a]

            db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                 port=3306)
            cursor = db.cursor(pymysql.cursors.DictCursor)

            try:
                cursor.execute("INSERT INTO "+id+"ani VALUES (%s ,%s ,%s, %s)", data_list)
            except:  # 에러발생 시 작동
                messagebox.showerror('오류', '데이터 입력 오류가 발생함')
            else:  # 에러 없을 시 작동
                messagebox.showinfo('성공', '데이터 입력 성공')
            db.commit()
            db.close()

        except ValueError:
            print("잘못된 값 입력")
            self.casaba_lineedit.setText('')
            self.casaba_result_label.setHidden(False)
            self.casaba_result_label.setText("잘못된 값 입력")
            self.casaba_result_label.setFont(QtGui.QFont("Nanum Gothic", 15))
            self.casaba_result_label.setStyleSheet("Color : red")

    def banana_push_Button(self):
        with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
        id = self.id_json['id']
        print(id)
        try:
            inputDate = self.banana_Dateedit.text()
            inputArea = int(self.banana_lineedit.text())

            name = 'pig'
            self.banana_lineedit.setText('')
            self.banana_result_label.setHidden(False)

            if self.pig_RadioButton.isChecked():
                a = "O"
            elif self.pig_RadioButton_2.isChecked():
                a = "X"

            self.banana_result_label.setText(inputDate + "\n돼지 번호는 " + str(inputArea) + "번 입니다.\n질병 유무는 " + a + " 입니다.")
            self.banana_result_label.setFont(QtGui.QFont("Nanum Gothic", 8))
            self.banana_result_label.setStyleSheet("Color : green")

            data_list = [name, inputDate, inputArea, a]

            db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                                 port=3306)
            cursor = db.cursor(pymysql.cursors.DictCursor)

            try:
                cursor.execute("INSERT INTO "+id+"ani VALUES (%s ,%s ,%s, %s)", data_list)
            except:  # 에러발생 시 작동
                messagebox.showerror('오류', '데이터 입력 오류가 발생함')
            else:  # 에러 없을 시 작동
                messagebox.showinfo('성공', '데이터 입력 성공')
            db.commit()
            db.close()


        except ValueError:
            print("잘못된 값 입력")
            self.banana_lineedit.setText('')
            self.banana_result_label.setHidden(False)
            self.banana_result_label.setText("잘못된 값 입력")
            self.banana_result_label.setFont(QtGui.QFont("Nanum Gothic", 15))
            self.banana_result_label.setStyleSheet("Color : red")

    # 각 컨테이너에 있는 라인에딧 엔터 후, 면적값 누적 함수


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", " "))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "가축"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "소"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "닭"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "돼지"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.farm_produce_combobox.addItem("전체")
        self.farm_produce_combobox.addItem("소")
        self.farm_produce_combobox.addItem("닭")
        self.farm_produce_combobox.addItem("돼지")
        self.farm_produce_container.setTitle(_translate("MainWindow", "가축"))
        self.rice_container.setTitle(_translate("MainWindow", "소"))
        self.rice_area_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">가축 번호 입력</p></body></html>"))
        self.rice_pushbutton.setText(_translate("MainWindow", "OK"))
        self.rice_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.cow_RadioButton.setText(_translate("MainWindow", "O"))
        self.cow_RadioButton_2.setText(_translate("MainWindow", "X"))
        self.cow_label_3.setText(_translate("MainWindow", "질병 유무"))
        self.casaba_container.setTitle(_translate("MainWindow", "닭"))
        self.casaba_area_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">가축 번호 입력</p></body></html>"))
        self.casaba_pushbutton.setText(_translate("MainWindow", "OK"))
        self.casaba_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ck_RadioButton.setText(_translate("MainWindow", "O"))
        self.ck_RadioButton_2.setText(_translate("MainWindow", "X"))
        self.ck_label_3.setText(_translate("MainWindow", "질병 유무"))
        self.banana_container.setTitle(_translate("MainWindow", "돼지"))
        self.banana_area_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">가축 번호 입력</p></body></html>"))
        self.pig_RadioButton.setText(_translate("MainWindow", "O"))
        self.pig_RadioButton_2.setText(_translate("MainWindow", "X"))
        self.pig_label_3.setText(_translate("MainWindow", "질병 유무"))
        self.banana_pushbutton.setText(_translate("MainWindow", "OK"))
        self.banana_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.rice_exit.setText(_translate("MainWindow", "exit"))
        self.casaba_exit.setText(_translate("MainWindow", "exit"))
        self.banana_exit.setText(_translate("MainWindow", "exit"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
