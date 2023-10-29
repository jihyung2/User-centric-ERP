import json
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pymysql
class MyApp(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        canvas = FigureCanvas(Figure(figsize = (3,4)))
        vbox = QVBoxLayout(self.main_widget)
        vbox.addWidget(canvas)

        self.addToolBar(NavigationToolbar(canvas, self))

        self.ax = canvas.figure.subplots()
        self.draw_pie()

        self.setWindowTitle("matplotlib in pyqt5")
        self.setGeometry(400, 150, 360, 640)
        self.show()

    def draw_pie(self) :
        with open('id.json', 'r', encoding="utf-8") as read_file :
                    self.id_json = json.load(read_file)
        id = self.id_json['id']
        print(id)
        db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                             port=3306)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM "+id+"ani")
        valueall = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            valueall = valueall + 1

        cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'cow'")
        cow = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            cow = cow + 1

        cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'chicken'")
        chicken = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            chicken = chicken + 1

        cursor.execute("SELECT * FROM "+id+"ani WHERE ani_name = 'pig'")
        pig = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            pig = pig + 1

        perrice = (cow / valueall) * 100
        percasaba = (chicken / valueall) * 100
        perbanana = (pig / valueall) * 100


        ratio = [perrice, percasaba, perbanana]
        labels = ['cow', 'chicken', 'pig']
        explode = [0.1, 0.1, 0.1]
        self.ax.pie(ratio, labels = labels, autopct='%.1f%%', startangle = 0, counterclock = False, explode=explode)



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())


