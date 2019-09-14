# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recv_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import main_image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QColor


class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.resize(400, 400)
        # Form.move(977, 516)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 401, 400))
        self.frame.setStyleSheet("#frame {border:none;border-radius:12px;background-image: url(:/newPrefix/back5.png)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(22, 30, 360, 231))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border:1px solid gray;\n"
"border-bottom:3px solid gray;\n"
"border-top-radius:10px;")
        self.textBrowser.setObjectName("textBrowser")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.textBrowser.setGraphicsEffect(op)
        self.textBrowser.setAutoFillBackground(True)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 260, 361, 91))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border:1px solid gray;\n"
"border-top:1px solid black;\n"
"border-bottom-radius:10px;")
        self.textEdit.setObjectName("textEdit")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.textEdit.setGraphicsEffect(op)
        self.textEdit.setAutoFillBackground(True)


        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 360, 110, 25))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 110, 25))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_2")


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 0, 91, 35))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 0, 20, 20))
        self.pushButton_5.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 190, 84);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 0, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 95, 90);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.closed)
        self.pushButton_5.clicked.connect(Form.min)
        self.pushButton_2.clicked.connect(Form.send_action)
        self.pushButton_3.clicked.connect(Form.send_file)
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
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "发送消息"))
        self.pushButton_3.setText(_translate("Form", "发送文件"))
        self.pushButton_5.setText(_translate("Form", "-"))
        self.pushButton.setText(_translate("Form", "x"))
