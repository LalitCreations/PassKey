import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QFont
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
        self.ui.home.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.home_page))
        self.ui.about.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.about_page))
        self.ui.retrieve.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.retrieve_page))
        self.ui.save.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.save_page))

        #login page code block
        if self.ui.main.currentWidget() == self.ui.login_page:
            for i in nav_buttons:
                i.setEnabled(False)
            usr,pswd = json_retrieve("user_data")
            text = "Welcome Back " + usr+"!"
            self.ui.label_10.setText(text)
            self.ui.pushButton_2.clicked.connect(lambda: self.login())

        #new user page code block
        if self.ui.main.currentWidget() == self.ui.newuser_page:
            for i in nav_buttons:
                i.setEnabled(False)
            self.ui.pushButton.clicked.connect(lambda: self.create_user_clicked())


        #home page code block
        if self.ui.main.currentWidget() != self.ui.login_page and self.ui.main.currentWidget() != self.ui.newuser_page:
            for i in nav_buttons:
                i.setEnabled(True)
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.save_page))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.main.setCurrentWidget(self.ui.retrieve_page))

        #save page code block    
        self.ui.pushButton_5.clicked.connect(lambda: self.save_data())  

        #retrieve page code block
        self.ui.retireve_button.clicked.connect(lambda: self.retrieve_data())

            

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

    def save_data(self):
        dtext = self.ui.datatitle.text()
        utext = self.ui.username.text()
        ptext = self.ui.password.text()
        username = encrpyt_msg(utext).decode("utf-8")
        password = encrpyt_msg(ptext).decode("utf-8")
        json_save(dtext,username,password)
        self.ui.savesatus.setFont(QFont("Noto Sans",18))
        self.ui.savesatus.setText("Save Successful!")
        for i in [self.ui.datatitle,self.ui.username,self.ui.password]:
            i.clear()

    def retrieve_data(self):
        
        text = self.ui.retrieve_datatitle_in.text()
        if json_retrieve(text) != "NotFound":
            username,password=json_retrieve(text)
            username = decrypt_msg(bytes(username,"utf-8"))
            password = decrypt_msg(bytes(password,"utf-8"))
            str1 = "DataTitle: " + text
            str2 = "UserName: " + username
            str3 = "Password: " + password
            self.ui.retrieve_datatitle_2.setText(str1)
            self.ui.retrieve_username.setText(str2)
            self.ui.retrieve_password.setText(str3)
            self.ui.retrieve_datatitle_in.clear()
            self.ui.retrieve_status.setFont(QFont("Noto Sans",18))
            self.ui.retrieve_status.setText("Retrieve Successful!")
        else:
            self.ui.retrieve_status.setFont(QFont("Noto Sans",18))
            self.ui.retrieve_status.setText("Retrieve Successful!")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show_ui()
    win.main()
    sys.exit(app.exec_())
