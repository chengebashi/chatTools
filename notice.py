# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import main_image

class Ui_Form10(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.resize(500, 270)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 500, 270))
        self.frame.setMinimumSize(QtCore.QSize(500, 270))
        self.frame.setMaximumSize(QtCore.QSize(500, 270))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame {background-image: url(:/newPrefix/back9.png);border:none;}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(30, 90, 301, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border:none;\n"
                                       "border-radius:5px")
        self.textBrowser.setObjectName("textBrowser")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.textBrowser.setGraphicsEffect(op)
        self.textBrowser.setAutoFillBackground(True)


        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 30, 301, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("border:none;\n"
                                       "border-radius:5px")
        self.textBrowser_2.setObjectName("textBrowser")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.textBrowser_2.setGraphicsEffect(op)
        self.textBrowser_2.setAutoFillBackground(True)


        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(360, 90, 100, 40))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;border:none;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 170, 95, 35))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 170, 95, 35))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/button.png);border-radius:10px;border:none;")
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 0, 20, 20))
        self.pushButton_5.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 190, 84);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 0, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 95, 90);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 230, 391, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.save)
        self.pushButton_5.clicked.connect(Form.min)
        self.pushButton_4.clicked.connect(Form.exit)
        self.pushButton_2.clicked.connect(Form.recv)
        self.pushButton_3.clicked.connect(Form.refuce)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "选择位置"))
        self.pushButton_2.setText(_translate("Form", "接 收"))
        self.pushButton_3.setText(_translate("Form", "拒 绝"))
        self.pushButton_5.setText(_translate("Form", "-"))
        self.pushButton_4.setText(_translate("Form", "x"))
        self.label.setText(_translate("Form", "提示：拒绝将无法再接收文件，除非对方重新发送"))
