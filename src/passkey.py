
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow
from encryption import decrypt_msg,encrpyt_msg,generate_key
from json_handler import json_save,json_retrieve,check_occupancy,create_new_acc


class main_window():
    

    def __init__(self):
        self.mainwin = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        if check_occupancy:
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

        if self.ui.main.currentWidget() == self.ui.login_page:
            for i in nav_buttons:
                i.setEnabled(False)
        else:
            for i in nav_buttons:
                i.setEnabled(True)

        if self.ui.main.currentWidget() == self.ui.newuser_page:
            username = self.ui.create_username.text()
            password = self.ui.create_password.text()
            
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show_ui()
    win.main()
    sys.exit(app.exec_())
