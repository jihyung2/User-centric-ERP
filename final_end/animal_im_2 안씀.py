# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Erp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from tkinter.tix import Select
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt

cow_stack = 0
chicken_stack = 0
pig_stack = 0
sim_list = [0]  # cow, chicken, pig
name_list = ['cow', 'chicken', 'pig']
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
        self.cow_container = QtWidgets.QGroupBox(self.centralwidget)
        self.cow_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.cow_container.setObjectName("cow_container")
        self.cow_exit = QtWidgets.QPushButton(self.cow_container)
        self.cow_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.cow_exit.setObjectName("cow_exit")

        #날짜
        self.cow_Dateedit = QtWidgets.QDateEdit(self.cow_container)
        self.cow_Dateedit.setGeometry(QtCore.QRect(80, 90, 126, 25))
        self.cow_Dateedit.setObjectName("cow_Dateedit")
        self.cow_Dateedit.setDate(QDate.currentDate())

        self.cow_area_label = QtWidgets.QLabel(self.cow_container)
        self.cow_area_label.setGeometry(QtCore.QRect(80, 60, 77, 18))
        self.cow_area_label.setObjectName("cow_area_label")


        ##
        self.cow_lineedit = QtWidgets.QLineEdit(self.cow_container)
        self.cow_lineedit.setGeometry(QtCore.QRect(80, 130, 113, 21))
        self.cow_lineedit.setObjectName("cow_lineedit")

        self.cow_label = QtWidgets.QLabel(self.centralwidget)
        self.cow_label.setGeometry(QtCore.QRect(180, 93, 58, 16))
        self.cow_label.setObjectName("cow_label")
        self.cow_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.cow_label_2.setGeometry(QtCore.QRect(158, 130, 58, 16))
        self.cow_label_2.setObjectName("cow_label_2")
        self.cow_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.cow_label_3.setGeometry(QtCore.QRect(158, 160, 58, 16))
        self.cow_label_3.setObjectName("cow_label_3")

        self.cow_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.cow_checkBox.setGeometry(QtCore.QRect(210, 160, 85, 20))
        self.cow_checkBox.setObjectName("checkBox")
        self.cow_checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cow_checkBox_2.setGeometry(QtCore.QRect(210, 180, 85, 20))
        self.cow_checkBox_2.setObjectName("checkBox_2")

        self.cow_pushbutton = QtWidgets.QPushButton(self.cow_container)
        self.cow_pushbutton.setGeometry(QtCore.QRect(130, 560, 41, 31))
        self.cow_pushbutton.setObjectName("cow_pushbutton")

        self.cow_result_label = QtWidgets.QLabel(self.cow_container)
        self.cow_result_label.setGeometry(QtCore.QRect(10, 170, 201, 381))
        self.cow_result_label.setObjectName("cow_result_label")

        ##닭
        self.chicken_container = QtWidgets.QGroupBox(self.centralwidget)
        self.chicken_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.chicken_container.setObjectName("chicken_container")

        self.chicken_exit = QtWidgets.QPushButton(self.chicken_container)
        self.chicken_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.chicken_exit.setObjectName("chicken_exit")

        self.chicken_Dateedit = QtWidgets.QDateEdit(self.chicken_container)
        self.chicken_Dateedit.setGeometry(QtCore.QRect(80, 90, 126, 25))
        self.chicken_Dateedit.setObjectName("chicken_Dateedit")
        self.chicken_Dateedit.setDate(QDate.currentDate())
        self.chicken_area_label = QtWidgets.QLabel(self.chicken_container)
        self.chicken_area_label.setGeometry(QtCore.QRect(80, 60, 77, 18))
        self.chicken_area_label.setObjectName("chicken_area_label")
        self.chicken_lineedit = QtWidgets.QLineEdit(self.chicken_container)
        self.chicken_lineedit.setGeometry(QtCore.QRect(80, 130, 113, 21))
        self.chicken_lineedit.setObjectName("chicken_lineedit")

        self.chicken_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.chicken_checkBox.setGeometry(QtCore.QRect(210, 160, 85, 20))
        self.chicken_checkBox.setObjectName("checkBox")
        self.chicken_checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chicken_checkBox_2.setGeometry(QtCore.QRect(210, 180, 85, 20))
        self.chicken_checkBox_2.setObjectName("checkBox_2")


        self.chicken_pushbutton = QtWidgets.QPushButton(self.chicken_container)
        self.chicken_pushbutton.setGeometry(QtCore.QRect(130, 560, 41, 31))
        self.chicken_pushbutton.setObjectName("chicken_pushbutton")
        self.chicken_result_label = QtWidgets.QLabel(self.chicken_container)
        self.chicken_result_label.setGeometry(QtCore.QRect(10, 170, 201, 381))
        self.chicken_result_label.setObjectName("chicken_result_label")
        self.pig_container = QtWidgets.QGroupBox(self.centralwidget)
        self.pig_container.setGeometry(QtCore.QRect(130, 0, 221, 591))
        self.pig_container.setObjectName("pig_container")
        self.pig_exit = QtWidgets.QPushButton(self.pig_container)
        self.pig_exit.setGeometry(QtCore.QRect(170, 560, 51, 31))
        self.pig_exit.setObjectName("pig_exit")
        self.pig_Dateedit = QtWidgets.QDateEdit(self.pig_container)
        self.pig_Dateedit.setGeometry(QtCore.QRect(80, 90, 126, 25))
        self.pig_Dateedit.setObjectName("pig_Dateedit")
        self.pig_Dateedit.setDate(QDate.currentDate())
        self.pig_area_label = QtWidgets.QLabel(self.pig_container)
        self.pig_area_label.setGeometry(QtCore.QRect(80, 60, 77, 18))
        self.pig_area_label.setObjectName("pig_area_label")
        self.pig_lineedit = QtWidgets.QLineEdit(self.pig_container)
        self.pig_lineedit.setGeometry(QtCore.QRect(80, 130, 113, 21))
        self.pig_lineedit.setObjectName("pig_lineedit")

        self.pig_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.pig_checkBox.setGeometry(QtCore.QRect(210, 160, 85, 20))
        self.pig_checkBox.setObjectName("checkBox")
        self.pig_checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.pig_checkBox_2.setGeometry(QtCore.QRect(210, 180, 85, 20))
        self.pig_checkBox_2.setObjectName("checkBox_2")


        self.pig_pushbutton = QtWidgets.QPushButton(self.pig_container)
        self.pig_pushbutton.setGeometry(QtCore.QRect(130, 560, 41, 31))
        self.pig_pushbutton.setObjectName("pig_pushbutton")
        self.pig_result_label = QtWidgets.QLabel(self.pig_container)
        self.pig_result_label.setGeometry(QtCore.QRect(10, 170, 201, 381))
        self.pig_result_label.setObjectName("pig_result_label")
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
        self.cow_container.setHidden(True)
        self.chicken_container.setHidden(True)
        self.pig_container.setHidden(True)
        self.treeWidget.clicked.connect(self.tree_onClick)

        self.farm_produce_combobox.currentIndexChanged.connect(self.farm_produce_OnClick)
        self.cow_exit.clicked.connect(MainWindow.close)
        self.chicken_exit.clicked.connect(MainWindow.close)
        self.pig_exit.clicked.connect(MainWindow.close)

    # 트리위젯 소분류 클릭 시, 해당 컨테이너 호출 함수(재클릭 시, 결과 라벨 숨김)

    def tree_onClick(self):
        getSelected = self.treeWidget.currentItem()
        if getSelected:
            print(getSelected.text(0))
            if (getSelected.text(0) == '가축'):
                self.farm_produce_container.setHidden(False)
                self.cow_container.setHidden(True)
                self.chicken_container.setHidden(True)
                self.pig_container.setHidden(True)

            elif (getSelected.text(0) == '소'):
                self.cow_container.setHidden(False)
                self.cow_result_label.setHidden(True)
                self.chicken_container.setHidden(True)
                self.pig_container.setHidden(True)
                self.farm_produce_container.setHidden(True)

            elif (getSelected.text(0) == '닭'):
                self.cow_container.setHidden(True)
                self.chicken_container.setHidden(False)
                self.chicken_result_label.setHidden(True)
                self.pig_container.setHidden(True)
                self.farm_produce_container.setHidden(True)

            else:
                self.cow_container.setHidden(True)
                self.chicken_container.setHidden(True)
                self.pig_container.setHidden(False)
                self.pig_result_label.setHidden(True)
                self.farm_produce_container.setHidden(True)

    def farm_produce_OnClick(self):
        Selected = self.farm_produce_combobox.currentText()
        if Selected:
            if Selected == '전체':
                out_s = ""
                for i in data_dic:
                    out_s += i + "\n"
                    for j in range(len(data_dic[i])):
                        out_s += str(data_dic[i][j][0]) + "  " + str(data_dic[i][j][1]) + "\n"
                self.farm_produce_label.setText(out_s)
            elif Selected == '소':
                # out_s1 = ""
                # for i in data_dic
                print(Selected)
            elif Selected == '닭':
                print(Selected)
            else:
                print(Selected)


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
        self.cow_container.setTitle(_translate("MainWindow", "소"))
        #
        self.cow_label.setText(_translate("MainWindow", "날짜"))
        self.cow_label_2.setText(_translate("MainWindow", "가축 번호"))
        self.cow_label_3.setText(_translate("MainWindow", "질병 유무"))
        self.cow_checkBox.setText(_translate("MainWindow", "O"))
        self.cow_checkBox_2.setText(_translate("MainWindow", "X"))
        #
        self.cow_pushbutton.setText(_translate("MainWindow", "OK"))
        self.cow_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.chicken_container.setTitle(_translate("MainWindow", "닭"))
        self.chicken_pushbutton.setText(_translate("MainWindow", "OK"))
        self.chicken_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pig_container.setTitle(_translate("MainWindow", "돼지"))
        self.pig_area_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.pig_pushbutton.setText(_translate("MainWindow", "OK"))
        self.pig_result_label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.cow_exit.setText(_translate("MainWindow", "exit"))
        self.chicken_exit.setText(_translate("MainWindow", "exit"))
        self.pig_exit.setText(_translate("MainWindow", "exit"))

        self.cow_label.setText(_translate("MainWindow", "날짜"))
        self.cow_label_2.setText(_translate("MainWindow", "가축 번호"))
        self.cow_label_3.setText(_translate("MainWindow", "질병 유무"))
        self.cow_checkBox.setText(_translate("MainWindow", "O"))
        self.cow_checkBox_2.setText(_translate("MainWindow", "X"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
