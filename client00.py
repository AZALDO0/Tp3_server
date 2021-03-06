import webbrowser as wb
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        
        self.label1 = QLabel("Enter your hostname:", self)
        self.label1.move(10,0)
        self.text1 = QLineEdit(self)
        self.text1.move(10, 30)
        
        self.label2 = QLabel("Enter your API Key:", self)
        self.label2.move(10,70)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 100)
        
        
        self.label3 = QLabel("Enter the IP of the target:", self)
        self.label3.move(10,130)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 160)
       
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 200)
        self.button = QPushButton("Send", self)
        self.button.move(10, 250)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text1.text()
        api_key = self.text2.text()
        ip = self.text3.text()
        if hostname == "" or api_key == "" or ip == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip, api_key)
            if res:
                self.label4.setText("Answer %s" % (res))
                self.label4.adjustSize()
                self.show()
                url2 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["lat"],res["long"])
                wb.open_new_tab(url2)

    def __query(self, hostname, ip ,  api_key):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip,api_key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()

    #API Key :9eN2sBX6fI3ZPTjLvfceIAutz8C7Qyio
    #Adresse du serveur : 127.0.0.1:8000
    # Ip : 149.62.158.57
    #http://hostname=149.62.158.57api_key=vJU6VAepn5xQGVFHVs5dEsXs24m0m7nCip=127.0.0.1:8000