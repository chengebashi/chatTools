# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talk_person.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import main_image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QColor

class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        Form.resize(720, 700)
        Form.setMinimumSize(QtCore.QSize(720, 700))
        Form.setMaximumSize(QtCore.QSize(720, 700))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -1, 720, 700))
        self.frame.setStyleSheet("#frame {border-radius:18px;\n"
"background-image: url(:/newPrefix/back4.png)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 701, 60))
        self.frame_2.setStyleSheet("#frame_2 {background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom:1px solid gray;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.frame_2.setGraphicsEffect(op)
        self.frame_2.setAutoFillBackground(True)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 0, 25, 25))
        self.pushButton_5.setStyleSheet("border-radius:12px;\n"
"background-color: rgb(255, 190, 84);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(670, 0, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:12px;\n"
"background-color: rgb(255, 95, 90);")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(280, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("border:none;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 701, 370))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: white;\n"
"border-bottom:2px solid black;\n"
"border:none;\n"
"\n"
"")
        self.textBrowser.setObjectName("textBrowser")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.textBrowser.setGraphicsEffect(op)
        self.textBrowser.setAutoFillBackground(True)

        self.fontComboBox = QtWidgets.QFontComboBox(self.frame)
        self.fontComboBox.setGeometry(QtCore.QRect(510, 440, 201, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(9)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setStyleSheet("border:none;\n"
"")
        self.fontComboBox.setObjectName("fontComboBox")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 440, 121, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border:none;\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(350, 440, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 25))
        self.toolButton.setObjectName("toolButton")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.toolButton.setGraphicsEffect(op)
        self.toolButton.setAutoFillBackground(True)

        self.lineEdit = QtWidgets.QTextBrowser(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 440, 261, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("boeder:none;\n"
"background-color:transparent;"
"")
        self.lineEdit.setObjectName("textBrowser_5")


        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 470, 700, 151))
        self.textEdit.setStyleSheet("border:none;")
        self.textEdit.setObjectName("textEdit")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.textEdit.setGraphicsEffect(op)
        self.textEdit.setAutoFillBackground(True)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 640, 121, 32))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.closed)
        self.pushButton_5.clicked.connect(Form.min)
        self.pushButton_2.clicked.connect(Form.send_action)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "-"))
        self.pushButton.setText(_translate("Form", "x"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.fontComboBox.setCurrentText(_translate("Form", "幼圆"))
        self.pushButton_6.setText(_translate("Form", "聊天记录"))
        self.lineEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "发送消息"))
