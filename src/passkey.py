
import sys
from venv import create
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui import Ui_MainWindow
from encryption import decrypt_msg,encrpyt_msg,generate_key
from json_handler import json_save,json_retrieve,check_occupancy,create_new_acc


class main_window():
    

    def __init__(self):
        self.mainwin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        if check_occupancy():
           self.ui.main.setCurrentWidget(self.ui.newuser_page)
           nav_buttons = [self.ui.home,self.ui.about,self.ui.retrieve,self.ui.save]
           for i in nav_buttons:
                i.setEnabled(False)
        else:
           self.ui.main.setCurrentWidget(self.ui.login_page)

        
    def show_ui(self):
        self.mainwin.show()
        
    def main(self):
        nav_buttons = [self.ui.home,self.ui.about,self.ui.retrieve,self.ui.save]

        #login code block
        if self.ui.main.currentWidget() == self.ui.login_page:
            for i in nav_buttons:
                i.setEnabled(False)
            usr,pswd = json_retrieve("user_data")
            text = "Welcome Back " + usr+"!"
            self.ui.label_10.setText(text)
            self.ui.pushButton_2.clicked.connect(lambda: self.login())
        else:
            for i in nav_buttons:
                i.setEnabled(True)

        #new user code block
        if self.ui.main.currentWidget() == self.ui.newuser_page:
            for i in nav_buttons:
                i.setEnabled(False)
            self.ui.pushButton.clicked.connect(lambda: self.create_user_clicked())
        else:
            for i in nav_buttons:
                i.setEnabled(True)

            

    def create_user_clicked(self):
        username = self.ui.create_username.text()
        password = self.ui.create_password.text()
        if username == "" or password == "":
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText("Empty username or password")
            x = msg.exec_()
        else:
            generate_key()
            password = encrpyt_msg(password)
            password = password.decode("utf-8")
            create_new_acc(username,password)
            self.ui.main.setCurrentWidget(self.ui.home_page)

    def login(self):
       nav_buttons = [self.ui.home,self.ui.about,self.ui.retrieve,self.ui.save]
       usr,pswd = json_retrieve("user_data")
       password = self.ui.lineEdit.text()
       pswd = bytes(pswd,"utf-8")
       pswd = decrypt_msg(pswd)
       if password == pswd:
           self.ui.main.setCurrentWidget(self.ui.home_page)
           for i in nav_buttons:
               i.setEnabled(True)
       else:
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText("Empty username or password")
            x = msg.exec_()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show_ui()
    win.main()
    sys.exit(app.exec_())
