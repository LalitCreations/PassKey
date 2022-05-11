
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 776)
        MainWindow.setMinimumSize(QtCore.QSize(856, 776))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(856, 776))
        self.centralwidget.setStyleSheet("background-color:rgb(32,32,32);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_panel = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_panel.sizePolicy().hasHeightForWidth())
        self.side_panel.setSizePolicy(sizePolicy)
        self.side_panel.setStyleSheet("#side_panel{\n"
"background-image:url(resources/pexels-photo-3308588.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"border-width:0px;\n"
"}")
        self.side_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_panel.setObjectName("side_panel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_panel)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.side_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(131, 131))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setBaseSize(QtCore.QSize(131, 131))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/passkey logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.side_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 24pt \"Impact\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 80, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.home = QtWidgets.QPushButton(self.side_panel)
        self.home.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.home.setFont(font)
        self.home.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"font: 18pt \"Impact\";\n"
"border-width:0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"")
        self.home.setFlat(True)
        self.home.setObjectName("home")
        self.verticalLayout.addWidget(self.home)
        self.save = QtWidgets.QPushButton(self.side_panel)
        self.save.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"font: 18pt \"Impact\";\n"
"border-width:0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"")
        self.save.setFlat(True)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)
        self.retrieve = QtWidgets.QPushButton(self.side_panel)
        self.retrieve.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.retrieve.setFont(font)
        self.retrieve.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"font: 18pt \"Impact\";\n"
"border-width:0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"")
        self.retrieve.setFlat(True)
        self.retrieve.setObjectName("retrieve")
        self.verticalLayout.addWidget(self.retrieve)
        self.about = QtWidgets.QPushButton(self.side_panel)
        self.about.setMinimumSize(QtCore.QSize(0, 85))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.about.setFont(font)
        self.about.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"font: 18pt \"Impact\";\n"
"border-width:0px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"   background-color:rgba(0,0,0,80);\n"
"}\n"
"\n"
"")
        self.about.setFlat(True)
        self.about.setObjectName("about")
        self.verticalLayout.addWidget(self.about)
        self.horizontalLayout.addWidget(self.side_panel)
        self.main = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.main.setFont(font)
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.newuser_page = QtWidgets.QWidget()
        self.newuser_page.setObjectName("newuser_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.newuser_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.newuser_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.newuser_page)
        self.line.setStyleSheet("background-color:rgb(152,152,152);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.newuser_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.user_frame = QtWidgets.QFrame(self.newuser_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.user_frame.sizePolicy().hasHeightForWidth())
        self.user_frame.setSizePolicy(sizePolicy)
        self.user_frame.setStyleSheet("#user_frame\n"
"{\n"
"border:0px;\n"
"}")
        self.user_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_frame.setObjectName("user_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.user_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.user_frame)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.create_username = QtWidgets.QLineEdit(self.user_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_username.setFont(font)
        self.create_username.setObjectName("create_username")
        self.horizontalLayout_2.addWidget(self.create_username)
        self.verticalLayout_2.addWidget(self.user_frame)
        self.password_frame = QtWidgets.QFrame(self.newuser_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.password_frame.sizePolicy().hasHeightForWidth())
        self.password_frame.setSizePolicy(sizePolicy)
        self.password_frame.setStyleSheet("#password_frame\n"
"{\n"
"border:0px;\n"
"}")
        self.password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.password_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.create_password = QtWidgets.QLineEdit(self.password_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_password.setFont(font)
        self.create_password.setObjectName("create_password")
        self.horizontalLayout_3.addWidget(self.create_password)
        self.verticalLayout_2.addWidget(self.password_frame)
        spacerItem3 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.newuser_page)
        self.pushButton.setMinimumSize(QtCore.QSize(135, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/check-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.main.addWidget(self.newuser_page)
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(self.home_page)
        self.line_3.setStyleSheet("background-color:rgb(152,152,152);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem5)
        self.label_13 = QtWidgets.QLabel(self.home_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(200, 200))
        self.label_13.setMaximumSize(QtCore.QSize(200, 200))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("resources/passkey logo.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.label_14 = QtWidgets.QLabel(self.home_page)
        self.label_14.setStyleSheet("font: 40pt \"Impact\";")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem7)
        self.pushButton_4 = QtWidgets.QPushButton(self.home_page)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_3 = QtWidgets.QPushButton(self.home_page)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(40, 200, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem8)
        self.main.addWidget(self.home_page)
        self.retrieve_page = QtWidgets.QWidget()
        self.retrieve_page.setObjectName("retrieve_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.retrieve_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.retrieve_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter)
        self.line_5 = QtWidgets.QFrame(self.retrieve_page)
        self.line_5.setStyleSheet("background-color:rgb(152,152,152);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_6.addWidget(self.line_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem9)
        self.frame_2 = QtWidgets.QFrame(self.retrieve_page)
        self.frame_2.setStyleSheet("#frame_2\n"
"{\n"
"border:0px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.retrieve_datatitle_in = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.retrieve_datatitle_in.setFont(font)
        self.retrieve_datatitle_in.setObjectName("retrieve_datatitle_in")
        self.horizontalLayout_8.addWidget(self.retrieve_datatitle_in)
        self.verticalLayout_6.addWidget(self.frame_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem10)
        self.retrieve_status = QtWidgets.QLabel(self.retrieve_page)
        self.retrieve_status.setText("")
        self.retrieve_status.setObjectName("retrieve_status")
        self.verticalLayout_6.addWidget(self.retrieve_status)
        self.frame_3 = QtWidgets.QFrame(self.retrieve_page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.retrieve_datatitle_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.retrieve_datatitle_2.setFont(font)
        self.retrieve_datatitle_2.setObjectName("retrieve_datatitle_2")
        self.verticalLayout_7.addWidget(self.retrieve_datatitle_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem11)
        self.retrieve_username = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.retrieve_username.setFont(font)
        self.retrieve_username.setObjectName("retrieve_username")
        self.verticalLayout_7.addWidget(self.retrieve_username)
        spacerItem12 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem12)
        self.retrieve_password = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.retrieve_password.setFont(font)
        self.retrieve_password.setObjectName("retrieve_password")
        self.verticalLayout_7.addWidget(self.retrieve_password)
        self.verticalLayout_6.addWidget(self.frame_3)
        spacerItem13 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem13)
        self.retireve_button = QtWidgets.QPushButton(self.retrieve_page)
        self.retireve_button.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.retireve_button.setFont(font)
        self.retireve_button.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"")
        self.retireve_button.setObjectName("retireve_button")
        self.verticalLayout_6.addWidget(self.retireve_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem14 = QtWidgets.QSpacerItem(577, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem14)
        self.main.addWidget(self.retrieve_page)
        self.about_page = QtWidgets.QWidget()
        self.about_page.setObjectName("about_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.about_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.about_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20, 0, QtCore.Qt.AlignHCenter)
        self.line_6 = QtWidgets.QFrame(self.about_page)
        self.line_6.setStyleSheet("background-color:rgb(152,152,152);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_8.addWidget(self.line_6)
        spacerItem15 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem15)
        self.frame_4 = QtWidgets.QFrame(self.about_page)
        self.frame_4.setMinimumSize(QtCore.QSize(350, 350))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setMinimumSize(QtCore.QSize(250, 250))
        self.label_21.setMaximumSize(QtCore.QSize(250, 250))
        self.label_21.setBaseSize(QtCore.QSize(250, 250))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("resources/passkey logo.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_9.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_9.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.about_page)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_6.setStyleSheet("#frame_6\n"
"{\n"
"border:0px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_9.addWidget(self.label_23)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.label_26 = QtWidgets.QLabel(self.about_page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_8.addWidget(self.label_26)
        self.label_25 = QtWidgets.QLabel(self.about_page)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_8.addWidget(self.label_25, 0, QtCore.Qt.AlignHCenter)
        spacerItem16 = QtWidgets.QSpacerItem(40, 80, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem16)
        self.main.addWidget(self.about_page)
        self.save_page = QtWidgets.QWidget()
        self.save_page.setObjectName("save_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.save_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.save_page)
        self.label_3.setMinimumSize(QtCore.QSize(0, 37))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line_4 = QtWidgets.QFrame(self.save_page)
        self.line_4.setStyleSheet("background-color:rgb(152,152,152);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        spacerItem17 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem17)
        self.datatitle_save = QtWidgets.QFrame(self.save_page)
        self.datatitle_save.setStyleSheet("#datatitle_save\n"
"{\n"
"border:0px;\n"
"}")
        self.datatitle_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.datatitle_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.datatitle_save.setObjectName("datatitle_save")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.datatitle_save)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.datatitle_save)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.datatitle = QtWidgets.QLineEdit(self.datatitle_save)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.datatitle.setFont(font)
        self.datatitle.setObjectName("datatitle")
        self.horizontalLayout_7.addWidget(self.datatitle)
        self.verticalLayout_5.addWidget(self.datatitle_save)
        self.username_save = QtWidgets.QFrame(self.save_page)
        self.username_save.setStyleSheet("#username_save\n"
"{\n"
"border:0px;\n"
"}")
        self.username_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_save.setObjectName("username_save")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.username_save)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.username_save)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.username = QtWidgets.QLineEdit(self.username_save)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout_6.addWidget(self.username)
        self.verticalLayout_5.addWidget(self.username_save)
        self.password_save = QtWidgets.QFrame(self.save_page)
        self.password_save.setStyleSheet("#password_save\n"
"{\n"
"border:0px;\n"
"}")
        self.password_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_save.setObjectName("password_save")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.password_save)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.password_save)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.password = QtWidgets.QLineEdit(self.password_save)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.horizontalLayout_5.addWidget(self.password)
        self.verticalLayout_5.addWidget(self.password_save)
        spacerItem18 = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem18)
        self.savesatus = QtWidgets.QLabel(self.save_page)
        self.savesatus.setText("")
        self.savesatus.setObjectName("savesatus")
        self.verticalLayout_5.addWidget(self.savesatus)
        self.pushButton_5 = QtWidgets.QPushButton(self.save_page)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem19 = QtWidgets.QSpacerItem(580, 400, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem19)
        self.main.addWidget(self.save_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.login_page)
        self.line_2.setStyleSheet("background-color:rgb(152,152,152);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_10 = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.login_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        spacerItem20 = QtWidgets.QSpacerItem(40, 150, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem20)
        self.frame = QtWidgets.QFrame(self.login_page)
        self.frame.setStyleSheet("#frame\n"
"{\n"
"border:0px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem21 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem21)
        self.pushButton_2 = QtWidgets.QPushButton(self.login_page)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:rgb(152,152,152);\n"
"border-radius:10px;\n"
"color:black;\n"
"border-color:rgb(152,152,152);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(32,32,32);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem22 = QtWidgets.QSpacerItem(40, 300, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem22)
        self.main.addWidget(self.login_page)
        self.horizontalLayout.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passkey"))
        self.label_2.setText(_translate("MainWindow", "PassKey"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.retrieve.setText(_translate("MainWindow", "Retrieve"))
        self.about.setText(_translate("MainWindow", "About"))
        self.label_4.setText(_translate("MainWindow", "Welcome to PassKey!"))
        self.label_5.setText(_translate("MainWindow", "Create user"))
        self.label_7.setText(_translate("MainWindow", "UserName:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", " Confirm"))
        self.label_12.setText(_translate("MainWindow", "Home"))
        self.label_14.setText(_translate("MainWindow", "PassKey"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Retrieve"))
        self.label_18.setText(_translate("MainWindow", "Retrieve"))
        self.label_19.setText(_translate("MainWindow", "DataTitle :"))
        self.retrieve_datatitle_2.setText(_translate("MainWindow", "DataTitle:"))
        self.retrieve_username.setText(_translate("MainWindow", "Username:"))
        self.retrieve_password.setText(_translate("MainWindow", "Password:"))
        self.retireve_button.setText(_translate("MainWindow", "Retrieve"))
        self.label_20.setText(_translate("MainWindow", "About"))
        self.label_22.setText(_translate("MainWindow", "PassKey"))
        self.label_24.setText(_translate("MainWindow", "Version : 2.0.0"))
        self.label_23.setText(_translate("MainWindow", "Author : G . Lalit Kartikeyan"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p>Source : <a href=\"www.github.com\"><span style=\" text-decoration: underline; color:#2980b9;\">GitHub</span></a></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Save"))
        self.label_17.setText(_translate("MainWindow", "DataTitle:"))
        self.label_16.setText(_translate("MainWindow", "Username:"))
        self.label_15.setText(_translate("MainWindow", "Password:"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "Login"))
        self.label_10.setText(_translate("MainWindow", "Welcome back!"))
        self.label_11.setText(_translate("MainWindow", "Password:"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
