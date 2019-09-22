# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QColor


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.resize(850, 700)
        # Form.move(300,400)
        Form.setMinimumSize(QtCore.QSize(850, 700))
        Form.setMaximumSize(QtCore.QSize(850, 700))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 851, 701))
        self.frame.setStyleSheet("#frame {border-radius:18px;\n"
"background-image: url(:/newPrefix/back3.png)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 541, 401))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("\n"
"border:none;\n"
"border-bottom:2px solid black;\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.textBrowser.setGraphicsEffect(op)
        self.textBrowser.setAutoFillBackground(True)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 70, 281, 30))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:none;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)       #设置无法获得焦点即无法编辑

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.lineEdit_2.setGraphicsEffect(op)
        self.lineEdit_2.setAutoFillBackground(True)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 30, 151, 30))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border:none;\n"
                                         "background-color:transparent;\n"
                                         "")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)


        self.fontComboBox = QtWidgets.QFontComboBox(self.frame)
        self.fontComboBox.setGeometry(QtCore.QRect(20, 470, 241, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(9)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setStyleSheet("border:none;\n")
        self.fontComboBox.setObjectName("fontComboBox")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(260, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border:none;\n")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["14", "9", "10", "11", "12", "13", "15", "17", "19"])

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border:none;\n"
"border-top:1px solid black;\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(530, 470, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-top:1px solid black;")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 25))
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 500, 541, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-bottom-left-radius:10px;\n"
"\n"
"\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.textEdit.setGraphicsEffect(op)
        self.textEdit.setAutoFillBackground(True)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 821, 61))
        self.frame_2.setStyleSheet("background-color: rgb(180, 180, 180);\n"
"border-top-right-radius:10px;\n"
"border-top-left-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.frame_2.setGraphicsEffect(op)
        self.frame_2.setAutoFillBackground(True)


        self.statusBar = QtWidgets.QStatusBar()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("border:none;\n"
                                         "background-color:transparent;\n"
                                         "")
        self.setStatusBar(self.statusBar)



        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 0, 25, 25))
        self.pushButton_5.setStyleSheet("border-radius:12px;\n"
"background-color: rgb(255, 190, 84);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(790, 0, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:12px;\n"
"background-color: rgb(255, 95, 90);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)

        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 640, 821, 51))
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 10, 111, 32))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 10, 111, 32))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 10, 121, 32))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QTextBrowser(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 15, 281, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border:none;\n"
"background:transparent;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)



        # self.frame_4 = QtWidgets.QFrame(self.frame)
        # self.frame_4.setGeometry(QtCore.QRect(559, 99, 281, 541))
        # self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        #                            "border:none;\n")
        # self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_4.setObjectName("frame_4")
        #
        # op = QtWidgets.QGraphicsOpacityEffect()
        # op.setOpacity(0.7)
        # self.frame_4.setGraphicsEffect(op)
        # self.frame_4.setAutoFillBackground(True)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(549, 99, 282, 542))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border:none;\n")
        self.listWidget.setObjectName("listWidget")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.listWidget.setGraphicsEffect(op)
        self.listWidget.setAutoFillBackground(True)






        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.closed)
        self.pushButton_5.clicked.connect(Form.min)
        self.pushButton_6.clicked.connect(Form.allaction)
        self.toolButton.clicked.connect(self.textBrowser.clear)
        self.pushButton_2.clicked.connect(Form.send_action)
        self.pushButton_3.clicked.connect(Form.recv_file)
        self.pushButton_4.clicked.connect(Form.send_file)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(Form.change)
        self.fontComboBox.currentTextChanged['QString'].connect(Form.setfont)
        self.comboBox.currentIndexChanged['int'].connect(Form.setsize)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            # if self.m_Position == (20-450, 470-500):
            #     self.m_flag = False
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    #1123
    # def mousePressEvent(self, event):
    #     self.pressX = event.x()    #记录鼠标按下的时候的坐标
    #     self.pressY = event.y()
    #
    # def mouseMoveEvent(self, event):
    #     x = event.x()
    #     y = event.y()   #获取移动后的坐标
    #     moveX = x-self.pressX
    #     moveY = y-self.pressY  #计算移动了多少
    #     positionX = self.frameGeometry().x() + moveX
    #     positionY = self.frameGeometry().y() + moveY    #计算移动后主窗口在桌面的位置
    #     self.move(positionX, positionY)    #移动主窗口
    #23424


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "班级群聊室"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.lineEdit_2.setText(_translate("Form", "用 户 名"))

        self.fontComboBox.setCurrentText(_translate("Form", "幼圆"))
        self.pushButton_6.setText(_translate("Form", "聊天记录"))
        self.pushButton_5.setText(_translate("Form", "-"))
        # self.pushButton_7.setText(_translate("Form", "123313"))
        self.pushButton.setText(_translate("Form", "x"))
        self.lineEdit_3.setText(_translate("Form", "班级聊天室"))
        self.pushButton_4.setText(_translate("Form", "发送文件"))
        self.pushButton_3.setText(_translate("Form", "下载文件"))
        self.pushButton_2.setText(_translate("Form", "发送消息"))
