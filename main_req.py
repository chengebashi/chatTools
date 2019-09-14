from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from login import Ui_Form
from take5_win import Ui_Form1
from add import Ui_Form2
from forget import Ui_Form3
from update import Ui_Form4
from record import Ui_Form5
from recv_win import Ui_Form6
from down_files import Ui_Form7
from up_all_file import Ui_Form8
import client, os.path
import re, time, threading
import socket, json, hashlib

sock_3 = socket.socket()

FILE_PATH = ''

class MyQtWidgets(QtWidgets.QMainWindow,Ui_Form1):
    '''定义一个聊天窗口类，显示聊天框'''
    info2 = ''
    info3 = ''
    info4 = ''
    info5 = ''
    info6 = ''
    dyname_win = []
    F = 0
    PEOPLE = 0
    people = []
    DOWN = []


    def __init__(self):
        super(MyQtWidgets, self).__init__()
        self.setupUi(self)
        sock_3.connect(("127.0.0.1", 9995))

        self.mythread = MyThread()    #开启一个线程来接收消息
        self.mythread2 = MyThread_2()
        self.mythread.signal.connect(self.callback)
        self.mythread2.signal.connect(self.callback2)
        self.mythread.start()
        self.mythread2.start()
        self.info6 = Mysendfile()
        self.info5 = Mydownfiles()
        MyQtWidgets.DOWN.append(self.info5)

        self.mythread3 = Mythread_3()
        self.mythread3.signal.connect(self.callback3)
        self.mythread3.start()


    def callback(self, tmp):  # 这里的 i 就是任务线程传回的数据
        try:
            if 'active_people' in tmp:             #返回显示在线人数
                tmp = json.loads(tmp)
                list = tmp['active_people']     #在线人数列表
                peoples = '在线人数:' + str(len(list)) + '人'
                self.textBrowser_4.setText(peoples)
                for k, p in enumerate(list):
                    if p not in MyQtWidgets.people:
                        self.listWidget.addItem(p)
                        MyQtWidgets.people.append(p)
                        p = Myrecvtalk()
                        MyQtWidgets.dyname_win.append([p, list[k], 0])

                # if self.PEOPLE == 0:
                #     for i, j in enumerate(list):      #为每个用户按钮附上用户名
                #         MyQtWidgets.people.append(j)
                #         j = Myrecvtalk()
                #         MyQtWidgets.dyname_win.append([j, list[i], 0])      #每个用户的对象名，用户名，窗口状态0/1（0表示窗口关闭，1表示开启）
                #         self.PEOPLE = 1
                # print(MyQtWidgets.dyname_win,1)
            elif 'down_line' in tmp:
                dict_name = json.loads(tmp)
                nick_name = dict_name['down_line']
                down_action = nick_name + '下线!'

                MyQtWidgets.people.remove(nick_name)
                down_user = filter(lambda x: nick_name == x[1], MyQtWidgets.dyname_win)
                for i in down_user:
                    down_p = i
                self.listWidget.takeItem(MyQtWidgets.dyname_win.index(down_p))
                MyQtWidgets.dyname_win.remove(down_p)

                self.textBrowser.append(down_action)

                self.statusBar.showMessage(down_action, 5000)


            elif 'up_line' in tmp:
                dict_name = json.loads(tmp)
                nick_name = dict_name['up_line']
                up_action = nick_name + '已上线!'

                # user_name = nick_name
                # nick_name = Myrecvtalk()
                # ld = filter(lambda x: user_name == x[1], MyQtWidgets.dyname_win)
                # for i in ld:
                #     kd = i
                # print(kd,'kd')
                # if not len(kd):
                #     MyQtWidgets.dyname_win.append([nick_name, user_name, 0])
                #     print(MyQtWidgets.dyname_win)
                #     self.listWidget.addItem(user_name)
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


    def callback3(self, tmp):
        try:
            if 'down_file' in tmp:
                tmp = json.loads(tmp)
                files_list = tmp['down_file']
                self.info5.listWidget.clear()
                self.info5.listWidget.addItems(files_list)
            # print(tmp, type(tmp))
            elif 'finish' in tmp:
                MyQtWidgets.DOWN[0].textBrowser_2.append('文件夹传输完成!')
                MyQtWidgets.DOWN[0].statusBar.showMessage('文件传输完成', 5000)

            else:
                tmp = json.loads(tmp)
                if tmp['files_req'] == 0:
                    file_name = tmp['files_name']
                    self.info6.textBrowser_2.append('-' + file_name + ' 的md5校验成功，上传完成!')
                    # self.textBrowser.clear()
                else:
                    self.info6.textBrowser_2.append(tmp['file_name'] + '上传失败！,传输终止,请重新上传!')
        except Exception as e:
            print(e)



    def closed(self):
        client.exit()
        self.close()
        up_talk = filter(lambda x: 1 == x[2], MyQtWidgets.dyname_win)
        for i in up_talk:
            i[0].close()



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
            with open('record.txt', 'r',)as f:
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
        down_file = dict()
        down_file['down_file_list'] = 'files_list'
        down_file = json.dumps(down_file, ensure_ascii=False)
        down_file = down_file.encode()
        down_file_len = '{:<15}'.format(len(down_file))  # 报头长度
        sock_3.send(down_file_len.encode())  # 发送报头长度
        sock_3.send(down_file)  # 发送正文
        # sock_3.send()
        self.info5.show()

    def send_file(self):
        self.info6.show()

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

class Mysendfile(QtWidgets.QMainWindow, Ui_Form8):
    '''
    上传文件
    '''
    # sock = socket.socket()
    Oline = 0
    def __init__(self):
        super(Mysendfile, self).__init__()
        self.setupUi(self)

        # self.sock.connect(('127.0.0.1', 9995))
        print('端口3已连接')




    def min(self):
        self.showMinimized()

    def exit(self):
        try:
            # if self.Oline == 0:
            self.hide()
            # Mysendfile.sock.close()
            # else:
            #     self.close()
            #     ex = 'the_out_of'
            #     self.closed(ex)
            #     self.Oline = 0
        except Exception as f:
            print(f)

    def select_files(self):
        '''选择文件'''
        try:
            box = QtWidgets.QMessageBox()
            if self.Oline == 1:
                box.warning(self, '警告', '文件上传中，请稍后重试!')
            else:
                self.progressBar.setValue(0)
                self.textBrowser_2.clear()
                # self.Oline = 1  #代表文件端口已连接
                dif = QFileDialog()
                dif.setFileMode(QFileDialog.AnyFile)    #设置打开任意文件
                dif.setFilter(QDir.Files)  #文件过滤
                if dif.exec_():
                    # 接受选中文件的路径，默认为列表
                    file_path = dif.selectedFiles()   #获得文件绝对路径
                    # file_name = os.path.basename(file_path[0])        #获得文件名
                self.textBrowser.setText(file_path[0])
                self.textBrowser_2.append('文件名:'+file_path[0])
                file_size = os.path.getsize(file_path[0])  # 获取文件大小
                new_file_size = round(file_size / 1024 / 1024, 2)
                new_file_size = '文件大小:' + str(new_file_size) + 'MB'
                self.textBrowser_2.append(new_file_size)
                file_md5 = self.file_md5(file_path[0])
                self.textBrowser_2.append('文件md5为:' + file_md5)

        except Exception as f:
            print(f)

    def select_dirs(self):
        '''选择文件夹'''
        try:
            box  = QtWidgets.QMessageBox()
            if self.Oline == 1:
                box.warning(self, '警告','文件上传中，请稍后重试!')
            else:
                self.progressBar.setValue(0)
                self.textBrowser_2.clear()
                dif = QFileDialog()
                dif.setFileMode(QFileDialog.Directory)    #设置打开任意文件夹
                dif.setFilter(QDir.Files)  #文件过滤
                if dif.exec_():
                    # 接受选中文件的路径，默认为列表
                    dir_path = dif.selectedFiles()   #获得文件夹绝对路径
                    # file_name = os.path.basename(file_path[0])        #获得文件名
                self.textBrowser.setText(dir_path[0])
                self.textBrowser_2.setText('文件夹名:'+dir_path[0])
        except Exception as f:
            print(f)

    def begin(self):
        try:
            box = QtWidgets.QMessageBox()
            if self.Oline == 1:
                box.warning(self, '警告', '文件上传中，请稍后重试!')
            else:
                file_path = self.textBrowser.toPlainText()    #获取文件绝对地址
                if file_path == '':
                    box.warning(self, '提示', '请选择文件或者文件夹!')
                if os.path.isdir(file_path):
                    self.textBrowser_2.append('您正在上传文件夹，请耐心等待....')
                    threading.Thread(target=self.up_dirs, args=(file_path, )).start()   #发送文件夹
                else:
                    file_size = os.path.getsize(file_path)       #获取文件大小
                    if file_size > 102400:
                        self.textBrowser_2.append('文件过大，请耐心等待!')
                    self.textBrowser_2.append('文件开始上传.....' + '\n' + '请不要关闭窗口!')
                    threading.Thread(target=self.up_file_thread, args=(file_path, )).start() #发送一个文件


            # self.sock.close()
        except Exception as f:
            print(f)

    def file_md5(self, file_path):
        m = hashlib.md5()
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                m.update(data)
        return m.hexdigest().upper()


    def up_file_thread(self, file_path):     #传输一个文件
        try:
            self.Oline = 1
            file_info = dict()  # 文件信息字典
            file_info['files_name'] = os.path.basename(file_path)
            file_info['files_size'] = os.path.getsize(file_path)
            file_info['files_md5'] = self.file_md5(file_path)
            visit = file_info['files_size'] / 100
            reg = dict()
            reg['up_files'] = 'everyone'
            reg['files_information'] = file_info
            reg = json.dumps(reg, ensure_ascii=False)
            reg = reg.encode()

            reg_len = '{:<15}'.format(len(reg))
            sock_3.send(reg_len.encode())
            sock_3.send(reg)
            sum = 0
            self.progressBar.setValue(sum)
            with open(file_path, 'rb')as s:
                while True:
                    data = s.read(1024)
                    sum += len(data)
                    if not data:
                        break
                    self.progressBar.setValue(sum / visit)
                    sock_3.send(data)
            self.Oline = 0
        except Exception as d:
            print(d)

    def up_dirs(self, dir_path):
        # box = QtWidgets.QMessageBox()
        try:
            self.Oline = 1
            self.textBrowser.append('文件夹传输不提供进度显示,传输完成会提示!')
            for root, dirs, files in os.walk(dir_path):
                if len(dirs) == 0 and len(files) == 0:
                    empty = root[len(dir_path):]
                    empty_dir = os.path.basename(dir_path) + empty
                    print(empty_dir, '空文件夹')
                    self.up_empty_dir(empty_dir)
                    continue

                for f in files:
                    file_abs_path = os.path.join(root, f)
                    print(file_abs_path, 999)
                    self.up_file_load(file_abs_path, dir_path)
            dir_name = os.path.basename(dir_path)
            self.statusBar.showMessage('文件夹<'+dir_name+'>上传完成', 5)
            self.Oline = 0
        except Exception as f:
            print(f)

    def up_empty_dir(self, root):           #空文件夹
        try:
            file_info = dict()
            file_info['files_name'] = root
            file_info['files_size'] = -1
            reg = dict()
            reg['up_files'] = 'everyone'
            reg['files_information'] = file_info
            reg = json.dumps(reg, ensure_ascii=False)
            reg = reg.encode()

            reg_len = '{:<15}'.format(len(reg))
            sock_3.send(reg_len.encode())
            sock_3.send(reg)
        except Exception as f:
            print(f)


    def up_file_load(self, file_path, dir_path):     #传输一个文件
        try:
            new_file_path = file_path[len(dir_path):]
            file_info = dict()  # 文件信息字典
            file_name = os.path.basename(dir_path) + new_file_path
            print(file_name, '文件夹中的文件名字')
            file_info['files_name'] = file_name
            file_info['files_size'] = os.path.getsize(file_path)
            file_info['files_md5'] = self.file_md5(file_path)
            # visit = file_info['files_size'] / 100
            reg = dict()
            reg['up_files'] = 'everyone'
            reg['files_information'] = file_info
            reg = json.dumps(reg, ensure_ascii=False)
            reg = reg.encode()

            reg_len = '{:<15}'.format(len(reg))
            sock_3.send(reg_len.encode())
            sock_3.send(reg)
            sum = 0
            # self.progressBar.setValue(sum)
            with open(file_path, 'rb')as s:
                while True:
                    data = s.read(1024)
                    sum += len(data)
                    if not data:
                        break
                    # self.progressBar.setValue(sum / visit)
                    sock_3.send(data)
        except Exception as d:
            print(d)



class Mydownfiles(QtWidgets.QMainWindow, Ui_Form7):
    '''下载文件'''
    word = ''
    local_name = ''
    def __init__(self):
        super(Mydownfiles, self).__init__()
        self.setupUi(self)

    def min(self):
        self.showMinimized()

    def exit(self):
        self.hide()

    def down_files(self):
        '''开始下载'''
        global FILE_PATH
        try:
            box = QtWidgets.QMessageBox
            local_path = self.textBrowser.toPlainText()
            FILE_PATH = os.path.join(local_path, self.word[5:])
            print(FILE_PATH, '你')
            if local_path == '':
                box.warning(self, '提示', '您还未选择下载位置呢？')
            else:
                # self.textBrowser_2.clear()
                # print(self.word[:4], '头')
                if self.word[:4] == 'Dirs':
                    dirs = dict()
                    dirs['down_files'] = 'everyone'
                    dirs['files_type'] = 'dirs'
                    dirs['files_name'] = self.word[5:]
                    dirs = json.dumps(dirs, ensure_ascii=False)
                    dirs = dirs.encode()
                    dirs_len = '{:<15}'.format(len(dirs))
                    sock_3.send(dirs_len.encode())
                    sock_3.send(dirs)
                else:
                    print('wenjian')
                    files = dict()
                    files['down_files'] = 'everyone'
                    files['files_type'] = 'files'
                    files['files_name'] = self.word[5:]
                    files = json.dumps(files, ensure_ascii=False)
                    files = files.encode()
                    files_len = '{:<15}'.format(len(files))
                    sock_3.send(files_len.encode())
                    sock_3.send(files)
                    print('fasong')
        except Exception as f:
            print(f)

    def change(self, item):
        '''选择下载的文件或者文件夹'''
        try:
            box = QtWidgets.QMessageBox()
            if self.local_name == '':
                box.warning(self, '提示', '请先选择保存位置!')
            else:
                self.local_name = self.textBrowser.toPlainText()
                self.word = item.text()
        except Exception as f:
            print(f)

    def choice(self):
        '''选择文件保存地址'''
        try:
            self.textBrowser.clear()
            self.progressBar.setValue(0)
            self.textBrowser_2.clear()
            dif = QFileDialog()
            dif.setFileMode(QFileDialog.Directory)    #设置打开任意文件夹
            dif.setFilter(QDir.Files)  #文件过滤
            if dif.exec_():
                # 接受选中文件的路径，默认为列表
                dir_path = dif.selectedFiles()   #获得文件夹绝对路径
                # file_name = os.path.basename(file_path[0])        #获得文件名
            self.textBrowser.setText(dir_path[0])
            self.local_name = dir_path[0]
        except Exception as f:
            print(f)



class Mythread_3(QThread):    #发送文件
    signal = pyqtSignal(str)  # 设置触发信号传递的参数数据类型,这里是字符串
    info = ''
    M = 0
    def __init__(self):
        super(Mythread_3, self).__init__()
    def run(self):
        try:
            while True:    #不停的接消息
                while True:
                    fan_len = sock_3.recv(15).decode()
                    if not len(fan_len):
                        break
                    fan_len = int(fan_len.strip())
                    size = 0
                    tmp = b''
                    while size < fan_len:
                        data = sock_3.recv(fan_len - size)
                        if not data:
                            break
                        tmp += data
                        size += len(data)
                    tmp = tmp.decode()
                    if 'TO_send' in tmp:
                        tmp = json.loads(tmp)
                        if tmp['TO_send'] == 'everyone':

                            if tmp['files_size'] == -1:  # 如果为空文件夹
                                os.makedirs(os.path.join(FILE_PATH, tmp['files_name']), exist_ok=True)
                                continue

                            dir_file = os.path.dirname(tmp['files_name'])
                            if len(dir_file) == 0:
                                MyQtWidgets.DOWN[0].progressBar.setValue(0)
                                MyQtWidgets.DOWN[0].textBrowser_2.append('文件名:'+tmp['files_name'])
                                MyQtWidgets.DOWN[0].textBrowser_2.append('文件大小:'+str(tmp['files_size']))
                                MyQtWidgets.DOWN[0].textBrowser_2.append('md5:'+str(tmp['files_md5']))
                                recv_size = 0
                                print(FILE_PATH, '哼')
                                sum = tmp['files_size'] / 100
                                with open(FILE_PATH, 'wb')as f:
                                    while recv_size < tmp['files_size']:
                                        file_tmp = sock_3.recv(tmp['files_size'] - recv_size)
                                        if not file_tmp:
                                            break
                                        f.write(file_tmp)
                                        recv_size += len(file_tmp)
                                        MyQtWidgets.DOWN[0].progressBar.setValue(recv_size / sum)
                                print(5)
                                if self.file_md5(FILE_PATH) == tmp['files_md5']:
                                    MyQtWidgets.DOWN[0].textBrowser_2.append('md5检验通过！下载成功！')
                                else:
                                    MyQtWidgets.DOWN[0].textBrowser_2.append('md5检验不通过！下载失败！')
                            else:
                                os.makedirs(os.path.join(MyQtWidgets.DOWN[0].textBrowser.toPlainText(), dir_file), exist_ok=True)
                                if self.M == 0:
                                    MyQtWidgets.DOWN[0].textBrowser_2.append('文件夹名:' + Mydownfiles.word[5:])
                                    MyQtWidgets.DOWN[0].textBrowser_2.append('文件夹传输不提供进度显示,传输完成会有提示!')
                                    self.M = 1
                                recv_size = 0
                                print(FILE_PATH, '哼')
                                with open(os.path.join(MyQtWidgets.DOWN[0].textBrowser.toPlainText(), tmp['files_name']), 'wb')as f:
                                    while recv_size < tmp['files_size']:
                                        file_tmp = sock_3.recv(tmp['files_size'] - recv_size)
                                        if not file_tmp:
                                            break
                                        f.write(file_tmp)
                                        recv_size += len(file_tmp)
                    else:
                        self.signal.emit(str(tmp))    #把接到的消息返回
        except Exception as d:
            print(d)

    def file_md5(self, file_path):
        m = hashlib.md5()
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                m.update(data)
        return m.hexdigest().upper()
