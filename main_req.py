from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtCore import QThread, pyqtSignal
from login import Ui_Form
from take5_win import Ui_Form1
from add import Ui_Form2
from forget import Ui_Form3
from update import Ui_Form4
from record import Ui_Form5
from recv_win import Ui_Form6
import client
import re, time
import socket, json



class MyQtWidgets(QtWidgets.QMainWindow,Ui_Form1):
    '''定义一个聊天窗口类，显示聊天框'''
    info2 = ''
    info3 = ''
    dyname_win = []

    def __init__(self):
        super(MyQtWidgets, self).__init__()
        self.setupUi(self)

        self.mythread = MyThread()    #开启一个线程来接收消息
        self.mythread2 = MyThread_2()
        self.mythread.signal.connect(self.callback)
        self.mythread2.signal.connect(self.callback2)
        self.mythread.start()
        self.mythread2.start()



    def callback(self, tmp):  # 这里的 i 就是任务线程传回的数据
        try:
            if 'active_people' in tmp:             #返回显示在线人数
                tmp = json.loads(tmp)
                list = tmp['active_people']     #在线人数列表
                self.listWidget.clear()
                self.listWidget.addItems(list)
                peoples = '在线人数:' + str(len(list)) + '人'
                self.textBrowser_4.setText(peoples)
                for i, j in enumerate(list):      #为每个用户按钮附上用户名
                    j = Myrecvtalk()
                    MyQtWidgets.dyname_win.append([j, list[i], 0])      #每个用户的对象名，用户名，窗口状态0/1（0表示窗口关闭，1表示开启）

            elif 'down_line' in tmp:
                dict_name = json.loads(tmp)
                nick_name = dict_name['down_line']
                down_action = nick_name + '下线!'
                self.textBrowser.append(down_action)


            elif 'up_line' in tmp:
                dict_name = json.loads(tmp)
                nick_name = dict_name['up_line']
                up_action = nick_name + '已上线!'
                self.textBrowser.append(up_action)
                self.statusBar.showMessage(up_action, 5000)

            elif 'person_talk' in tmp:
                request_name = json.loads(tmp)
                other_name = request_name['person_talk']
                news = request_name['oneToone_talk']
                news = other_name + ':' + news
                ld = filter(lambda x: other_name == x[1], MyQtWidgets.dyname_win)    #判断来自对方的消息的窗口是否打开，如果打开则在上面添加消息，否则重新打开窗口添加消息
                for l in ld:
                    obj = l
                if obj[2] == 1:    #当窗口存在直接添加消息
                    obj[0].textBrowser.append(news)

                elif obj[2] == 0:   #当窗口不存在
                    obj[2] = 1    #打开窗口
                    obj[0].show()
                    obj[0].label.setText(other_name)
                    obj[0].textBrowser.append(news)



            elif 'welcome_uppeople' in tmp:
                at_user = json.loads(tmp)
                at_usr_name = at_user['welcome_uppeople']
                self.info3 = at_usr_name
                welcome = '                    '+'欢迎'+at_usr_name+'上线'
                self.textBrowser.append(welcome)

            else:
                self.textBrowser.append(tmp)
                with open('record.txt', 'a')as f:
                    f.write(tmp + '\n')

        except Exception as f:
            print(f)

    def callback2(self, now_time):  # 这里的 i 就是任务线程传回的数据
        self.textBrowser_5.setText(now_time)


    def closed(self):
        client.exit()
        self.close()


    def min(self):
        self.showMinimized()


    def setfont(self):
        try:
            ft = self.fontComboBox.currentText()
            font = QtGui.QFont()
            size = self.comboBox.currentText()
            size = int(size)
            font.setFamily(ft)
            font.setPointSize(size)
            self.textBrowser.setFont(font)
            self.textEdit.setFont(font)
        except Exception as e:
            print(e)


    def setsize(self):
        try:
            size = self.comboBox.currentText()
            ft = self.fontComboBox.currentText()
            size = int(size)
            font = QtGui.QFont()
            font.setFamily(ft)
            font.setPointSize(size)
            self.textBrowser.setFont(font)
            self.textEdit.setFont(font)
        except Exception as e:
            print(e)

    def allaction(self):
        try:
            self.info2 = Myrecord()
            self.info2.show()
            with open('record.txt', 'r')as f:
                all = f.read()
            self.info2.textBrowser.append(all)
        except Exception as d:
            print(d)

    def send_action(self):
        try:
            req = self.textEdit.toPlainText()
            if req:
                reqs = '我' + ':' + req
                self.textBrowser.append(reqs)
                self.textEdit.clear()
                # abc = re.sub("['A-Za-z0-9_\!\%\[\]\,\。:./?@;#$^&*`+=(){}]", "", req)  # 匹配中文字符
                # abc = abc.replace(' ', '')
                # num = len(abc)*2
                self.mythread.action(req)
                with open('record.txt', 'a')as h:
                    h.write(req + '\n')
        except Exception as e:
            print(e)



    def recv_file(self):
        pass

    def send_file(self):
        pass

    def change(self,item):    #按钮事件1（用户）
        try:
            box = QtWidgets.QMessageBox()
            word = item.text()
            if word != self.info3:    #不能点自己
                list = filter(lambda x: word == x[1], MyQtWidgets.dyname_win)
                for li in list:
                    obj = li
                if obj[2] == 1:
                    box.information(self, "温馨提示", " 别点了，您正在和他聊天呢!")
                else:
                    obj[0].show()
                    obj[0].textBrowser.clear()
                    obj[0].label.setText(word)
                    obj[2] = 1

        except Exception as f:
            print(f)



class MyThread(QThread):
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是字符串
    sock = socket.socket()

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        self.sock.connect(('127.0.0.1', 9996))
        while True:    #不停的接消息
            while True:
                fan_len = self.sock.recv(15).decode()
                if not len(fan_len):
                    break
                fan_len = int(fan_len.strip())
                size = 0
                tmp = b''
                while size < fan_len:
                    data = self.sock.recv(fan_len - size)
                    if not data:
                        break
                    tmp += data
                    size += len(data)
                    tmp = tmp.decode()
                    self.signal.emit(str(tmp))    #把接到的消息返回

    def action(self,act):
        # abc = re.sub("[{A-Za-z0-9\!\%\[\]\,\。}]", "", act)     #匹配中文字符
        # abc = abc.replace(' ', '')
        act = act.encode()
        act_len = '{:<15}'.format(len(act))  # 报头长度
        self.sock.send(act_len.encode())  # 发送报头长度
        self.sock.send(act)     #发送正文




class MyThread_2(QThread):
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(MyThread_2, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        week = ['一', '二', '三', '四', '五', '六', '日']
        while True:
            local_time = time.localtime()
            now_time = '%s/%s/%s %s:%s:%s 星期%s' % (local_time[:6] + (week[local_time[6]],))
            time.sleep(1)
            self.signal.emit(str(now_time))    #把接到的消息返回

class Mylogin(QtWidgets.QMainWindow, Ui_Form):
    '''登录窗口，实现等功能模块'''
    ui1 = ''
    ui2 = ''
    ui3 = ''
    ui4 = ''
    ui5 = ''
    def __init__(self):
        super(Mylogin, self).__init__()
        self.setupUi(self)

    def exit(self):
        self.close()
        client.exit()

    def login(self):
        box = QtWidgets.QMessageBox()
        user_name = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        if not re.match("^[a-zA-Z0-9_]{0,8}$", user_name):
            box.warning(self, "提示", "用户名输入格式有误!")

        elif not re.match("^[a-zA-Z0-9_]{0,15}$", passwd):
            box.warning(self, "提示", "密码输入格式有误!")

        else:
            try:
                args = dict()
                passwd = client.passwd_md5(passwd)
                args["user_name"] = user_name
                args["password"] = passwd
                a = client.login(args)
                if a == 0:
                    self.ui1 = MyQtWidgets()
                    self.ui1.show()
                    self.close()

                elif a == 1:
                    box.warning(self, "提示", "用户名不存在!")

                elif a == 3:
                    box.warning(self, "提示", "您已登录，无需重复登录！")

                else:
                    box.warning(self, "提示", "密码错误!")

            except Exception as e:
                print(e)

    def add(self):
        self.ui2 = Myregister()
        self.ui2.show()

    def select_pd(self):
        self.ui3 = Myforget()
        self.ui3.show()

    def modify(self):
        self.ui4 = Myupdate()
        self.ui4.show()




class Myregister(QtWidgets.QMainWindow, Ui_Form2):
    '''注册账号模块'''
    def __init__(self):
        super(Myregister, self).__init__()
        self.setupUi(self)

    def register(self):
        try:
            box = QtWidgets.QMessageBox()
            nick_name = self.lineEdit.text()
            user_name = self.lineEdit_2.text()
            password = self.lineEdit_3.text()
            phone = self.lineEdit_4.text()
            email = self.lineEdit_5.text()
            if len(nick_name) > 7:
                box.warning(self,'提示','昵称太长')
            elif len(nick_name) == 0:
                box.warning(self, '提示', '昵称为空')
            elif len(user_name) > 8:
                box.warning(self, '提示', '账号太长')
            elif len(user_name) == 0:
                box.warning(self, '提示', '请输入账号')
            elif not re.match("^[a-zA-Z0-9_]{0,8}$", user_name):
                box.warning(self, "提示", "账号输入格式有误!")
            elif len(password) > 12:
                box.warning(self, '提示', '密码太长')
            elif len(password) == 0:
                box.warning(self, '提示', '请输入密码')
            elif not re.match("^[a-zA-Z0-9_]{0,12}$", password):
                box.warning(self, "提示", "密码输入格式有误!")
            elif len(phone) > 11 or len(phone) < 11:
                box.warning(self, '警告', '手机号格式错误!')
            elif not re.match("^[0-9]{0,11}$", phone):
                box.warning(self, '警告', '手机号输入有误!')
            elif not re.search('@', email):
                box.warning(self, '提示', '邮箱格式有误！')
            else:
                reg = dict()
                password = client.passwd_md5(password)
                reg["nick_name"] = nick_name
                reg["user_name"] = user_name
                reg["password"] = password
                reg["phone"] = phone
                reg["email"] = email
                print(reg)
                b = client.register(reg)
                if b == 0:
                    box.information(self, "恭喜", "注册成功!")
                    self.close()
                elif b == 1:
                    box.warning(self, '警告', '该用户名已存在!')

                elif b ==2:
                    box.warning(self, '警告', '该账号已存在!')

                else:
                    box.warning(self, '警告', '该邮箱已存在!')
        except Exception as f:
            print(f)



    def send_num(self):
        pass

    def exit(self):
        self.close()


class Myforget(QtWidgets.QMainWindow, Ui_Form3):
    '''忘记密码，实现邮箱重置密码'''
    def __init__(self):
        super(Myforget, self).__init__()
        self.setupUi(self)

    def yanzheng(self):
        box = QtWidgets.QMessageBox()
        email = self.lineEdit.text()
        if not re.search('@', email):
            box.warning(self, '提示', '邮箱格式有误！')
        else:
            arg = email
            e = client.forget_pd(arg)
            if e == 0:
                box.information(self, "恭喜", "密码重置成功,新密码30秒内将发送到你的邮箱！")
            elif e == 1:
                box.warning(self, "警告", "邮箱不存在!")


    def exit(self):
        self.close()


class Myupdate(QtWidgets.QMainWindow, Ui_Form4):
    '''修改密码'''
    def __init__(self):
        super(Myupdate, self).__init__()
        self.setupUi(self)

    def update_set(self):
        box = QtWidgets.QMessageBox()
        user_name = self.lineEdit.text()
        old_password = self.lineEdit_2.text()
        new_password = self.lineEdit_3.text()
        if len(user_name) > 8:
            box.warning(self, '提示', '账号太长')
        elif len(user_name) == 0:
            box.warning(self, '提示', '请输入账号')
        elif not re.match("^[a-zA-Z0-9_]{0,8}$", user_name):
            box.warning(self, "提示", "账号输入格式有误!")
        elif len(old_password) > 12:
            box.warning(self, '提示', '密码太长')
        elif len(old_password) == 0:
            box.warning(self, '提示', '请输入旧密码')
        elif not re.match("^[a-zA-Z0-9_]{0,12}$", old_password):
            box.warning(self, "提示", "密码输入格式有误!")
        elif len(new_password) > 12:
            box.warning(self, '提示', '密码太长')
        elif len(new_password) == 0:
            box.warning(self, '提示', '请输入新密码')
        elif not re.match("^[a-zA-Z0-9_]{0,12}$", new_password):
            box.warning(self, "提示", "密码输入格式有误!")
        else:
            args = dict()
            old_password = client.passwd_md5(old_password)
            new_password = client.passwd_md5(new_password)
            args["user_name"] = user_name    #账号
            args["old_password"] = old_password
            args["new_password"] = new_password
            c = client.update(args)
            if c == 0:
                box.information(self, "恭喜", "修改密码成功!")
                self.close()
            elif c == 1:
                box.warning(self, "警告", "账号不存在!")
            elif c == 2:
                box.warning(self, "警告", "旧密码错误!")


    def exit(self):
        self.close()



class Myrecvtalk(QtWidgets.QMainWindow, Ui_Form6):
    '''私人聊天'''
    def __init__(self):
        super(Myrecvtalk, self).__init__()
        self.setupUi(self)

    def recv_action(self, recv_news):
        self.textBrowser.append(recv_news)

    def closed(self):
        try:
            word = self.label.text()
            self.close()
            list = filter(lambda x: word == x[1], MyQtWidgets.dyname_win)
            for li in list:
                obj = li
            obj[2] = 0
        except Exception as e:
            print(e)

    def min(self):
        self.showMinimized()

    def send_action(self):
        try:
            send_new = self.textEdit.toPlainText()
            if send_new is not '':
                self.textEdit.clear()
                send_news = '我：'+send_new
                self.textBrowser.append(send_news)
                new_dict = dict()
                user = self.label.text()
                new_dict['person_talk'] = user
                new_dict['oneToone_talk'] = send_new
                news = json.dumps(new_dict, ensure_ascii=False)
                MyThread().action(news)
        except Exception as e:
            print(e)


class Myrecord(QtWidgets.QMainWindow, Ui_Form5):
    '''聊天记录'''
    def __init__(self):
        super(Myrecord, self).__init__()
        self.setupUi(self)


    def closed(self):
        self.close()

    def min(self):
        self.showMinimized()