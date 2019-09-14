# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'down_files.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QColor

import main_image


class Ui_Form7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.resize(620, 520)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 620, 520))
        self.frame.setMinimumSize(QtCore.QSize(620, 520))
        self.frame.setMaximumSize(QtCore.QSize(620, 520))
        self.frame.setStyleSheet("#frame {background-image: url(:/newPrefix/back7.png);\n"
"border:none;}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 60, 130, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"background-image: url(:/newPrefix/back3.png);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 100, 130, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:10px;\n"
                                      "background-image: url(:/newPrefix/back3.png);")
        self.pushButton_2.setObjectName("pushButton")

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 311, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border:none;\n"
"border-radius:5px")
        self.textBrowser.setObjectName("textBrowser")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.textBrowser.setGraphicsEffect(op)
        self.textBrowser.setAutoFillBackground(True)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(370, 390, 231, 23))
        # self.progressBar.setProperty("value", 0)
        self.progressBar.setRange(0, 100)
        self.progressBar.setStyleSheet("border:2px solid grey;border-radius:5px;text-align:center;\n")
        self.progressBar.setObjectName("progressBar")
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.progressBar.setGraphicsEffect(op)
        self.progressBar.setAutoFillBackground(True)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 220, 231, 151))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("border:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.textBrowser_2.setGraphicsEffect(op)
        self.textBrowser_2.setAutoFillBackground(True)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(19, 131, 311, 341))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border:none;")
        self.listWidget.setObjectName("listWidget")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.listWidget.setGraphicsEffect(op)
        self.listWidget.setAutoFillBackground(True)

        self.statusBar = QtWidgets.QStatusBar()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("border:none;\n"
                                     "background-color:transparent;\n"
                                     "")
        self.setStatusBar(self.statusBar)

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         # if self.m_Position == (20-450, 470-500):
    #         #     self.m_flag = False
    #         event.accept()
    #         self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     self.setCursor(QCursor(Qt.ArrowCursor))


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.down_files)
        self.pushButton_2.clicked.connect(Form.choice)
        self.pushButton_4.clicked.connect(Form.min)
        self.pushButton_3.clicked.connect(Form.exit)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(Form.change)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "下载文件"))
        self.pushButton_2.setText(_translate("Form", "选择保存地址"))
        self.label.setText(_translate("Form", "       下载群文件"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.pushButton_4.setText(_translate("Form", "—"))

