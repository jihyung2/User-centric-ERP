import sys
import numpy as np
from erplogin import *
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

        canvas = FigureCanvas(Figure(figsize = (4, 3)))
        vbox = QVBoxLayout(self.main_widget)
        vbox.addWidget(canvas)

        self.addToolBar(NavigationToolbar(canvas, self)) 

        self.ax = canvas.figure.subplots()
        self.draw_pie()

        self.setWindowTitle("matplotlib in pyqt5")
        self.setGeometry(400, 150, 360, 640)
        

    def draw_pie(self) :
        with open('id.json', 'r', encoding="utf-8") as read_file :
            self.id_json = json.load(read_file)
        id = self.id_json['id']
        print(id)

        db = pymysql.connect(host='127.0.0.1', user='root', password='040416', db='qtdata', charset='utf8',
                             port=3306)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM "+id+"plant")
        valueall = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            valueall = valueall + result["su_kg"]
        print(valueall)


        cursor.execute("SELECT * FROM "+id+"plant WHERE su_name = 'rice'")
        rice = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            rice = rice + result["su_kg"]

        print(rice)

        cursor.execute("SELECT * FROM "+id+"plant WHERE su_name = 'casaba'")
        casaba = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;

            casaba = casaba + result["su_kg"]

        print(casaba)

        cursor.execute("SELECT * FROM "+id+"plant WHERE su_name = 'banana'")
        banana = 0
        while (True):
            result = cursor.fetchone()
            if result == None:
                break;
            banana = banana + result["su_kg"]

        print(banana)
        db.commit()
        db.close()

        perrice = (rice / valueall)*100
        percasaba = (casaba / valueall) * 100
        perbanana = (banana / valueall) * 100
        print(perrice,percasaba,perbanana)
        

        ratio = [perrice, perbanana, percasaba]
        labels = ['rice', 'banana', 'cassava']
        explode = [0.1, 0.1, 0.1]
        self.ax.pie(ratio, labels = labels, autopct='%.1f%%', startangle = 0, counterclock = False, explode=explode)



if __name__ == '__main__' :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    app = QApplication(sys.argv)
    ex = MyApp(ui.get_LId())
    sys.exit(app.exec())

    

