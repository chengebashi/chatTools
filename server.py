import socket
import json
import threading
import smtp_mail
import server_mysql
import os.path
import hashlib


sock = socket.socket()   #用于响应登录注册等功能
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("127.0.0.1", 9997))
sock.listen(5)

sock_2 = socket.socket()     #创建一个套接字，用于实时显示聊天消息
sock_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_2.bind(("127.0.0.1", 9996))
sock_2.listen(5)

sock_3 = socket.socket()  # 创建一个套接字，传文件
sock_3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_3.bind(("127.0.0.1", 9995))
sock_3.listen(5)
address = []
File_list = []
PATH = r'D:\笔记\临时文件传输'
PATH_2 = r'D:\笔记\临时接收'
A = 0



def login_register(conn):
    '''登录和注册请求响应'''
    try:
        while True:
            reponse_len = conn.recv(15).decode()    #接收报文长度
            if len(reponse_len) == 0:
                break
            reponse_len = int(reponse_len.strip())

            reponse = recved_main(reponse_len, conn)   #接收报文

            reponse = json.loads(reponse)         #解析报文成字典格式
            if reponse["login"] == 0:
                break
            elif reponse["login"] == 1:         #登录请求
                r = login(reponse)
                if r["return"] != 0:            #返回值不为0，登录失败
                    reg = json.dumps(r)
                    reg = reg.encode()
                    reg_len = '{:<15}'.format(len(reg))
                    conn.send(reg_len.encode())
                    conn.send(reg)
                else:
                    reg = json.dumps(r)
                    reg = reg.encode()#登录成功
                    reg_len = '{:<15}'.format(len(reg))
                    conn.send(reg_len.encode())
                    conn.send(reg)
                    codd, addr = sock_2.accept()    #连接第二个端口，收发消息
                    print(addr, "端口2已连接")
                    user_name = r['user_name']
                    nick_name = server_mysql.select_nick_name(user_name)  # 查询数据库返回昵称
                    print(nick_name, type(nick_name))
                    threading.Thread(target=perosn, args=(codd, nick_name)).start()   #开启线程接消息

                    conn_3, addr_3 = sock_3.accept()
                    File_list.append([conn_3,nick_name])
                    print(addr_3, '端口3已连接')
                    threading.Thread(target=recv_files, args=(conn_3, nick_name)).start()


            elif reponse["login"] == 2:
                r = register(reponse)

                reg = json.dumps(r)
                reg = reg.encode()
                reg_len = '{:<15}'.format(len(reg))
                conn.send(reg_len.encode())
                conn.send(reg)

            elif reponse["login"] == 3:
                r = update_pd(reponse)

                reg = json.dumps(r)
                reg = reg.encode()
                reg_len = '{:<15}'.format(len(reg))
                conn.send(reg_len.encode())
                conn.send(reg)

            elif reponse["login"] == 4:
                r = forget_pd(reponse)

                reg = json.dumps(r)
                reg = reg.encode()
                reg_len = '{:<15}'.format(len(reg))
                conn.send(reg_len.encode())
                conn.send(reg)

    except Exception as e:
        print(e)

    finally:
        conn.close()
        print('端口1连接关闭')


def login(reponse):
    '''登录'''
    reg = dict()
    reg["login"] = 1
    user_name = reponse['args']['user_name']
    password = reponse['args']['password']
    nick_name = server_mysql.select_nick_name(user_name)
    user_exist = filter(lambda x: nick_name == x[1], address)
    for i in user_exist:
        if i:
            reg["return"] = 3
            return reg
    a = server_mysql.check_user_name(user_name)  # 验证账号
    if a == 1:
        reg["return"] = 1
    else:
        b = server_mysql.check_password(user_name, password)  # 验证密码
        if b == 1:
            reg["return"] = 2
        else:
            reg["return"] = 0
            reg['user_name'] = user_name
            print('登录成功')

    return reg


def register(reponse):
    '''注册'''
    reg = dict()
    reg["login"] = 2
    nick = reponse["args"]["nick_name"]
    a = server_mysql.check_nick_name(nick)        # 验证用户名
    if a == 0:
        reg["return"] = 1                #用户名已存在

    else:
        user_name = reponse['args']['user_name']
        b = server_mysql.check_user_name(user_name)   #验证账号
        if b == 0:
            reg["return"] = 2        #账号存在
        else:
            the_email = reponse['args']['email']
            c = server_mysql.check_email(the_email)
            if c == 0:
                reg["return"] = 3     #邮箱存在
            else:
                information = reponse['args']   #用户注册信息
                print(information, type(information))
                server_mysql.add_user(information)
                reg["return"] = 0    #注册成功

    return reg

def update_pd(reponse):
    '''修改密码'''
    reg = dict()
    reg["login"] = 3
    user_name = reponse['args']['user_name']          #查询数据库
    old_passwd = reponse['args']['old_password']
    new_passwd = reponse['args']['new_password']
    a = server_mysql.check_user_name(user_name)  #验证账号
    if a == 1:
        reg["return"] = 1
    else:
        b = server_mysql.check_password(user_name, old_passwd)   #验证密码
        if b == 1:
            reg["return"] = 2
        else:
            server_mysql.update_passwd(user_name, new_passwd)    #将新密码写入数据库
            reg['return'] = 0

    return reg


def forget_pd(reponse):
    '''重置密码'''
    reg = dict()
    reg["login"] = 4
    the_email = reponse["args"]  # 查询数据库
    # 修改密码
    a = server_mysql.check_email(the_email)     #验证邮箱
    if  a == 1:
        reg["return"] = 1
    else:
        threading.Thread(target=smtp_mail.main, args=(the_email,)).start()
        reg["return"] = 0

    return reg



def recved_main(data_len, sock):
    '''接收报文正文'''
    size = 0
    tmp = b''
    while size < data_len:
        data = sock.recv(data_len - size)
        if not data:
            break
        tmp += data
        size += len(data)
    tmp = tmp.decode()
    return tmp



def perosn(conn, nick_name):
    '''显示在线人数'''
    address.append([(conn,), nick_name])
    welcome_user(conn, nick_name)    #欢迎上线
    active_people()
    up_people(nick_name)  # 提示某人上线
    try:
        while True:
            action_len = conn.recv(15).decode()  # 消息长度
            if not action_len:
                break
            action_data_len = int(action_len.strip())
            action = recved_main(action_data_len, conn)  # 接收消息
            print(action)
            if 'login' in action:
                break

            elif 'person_talk' in action:
                action = json.loads(action)
                other_name = action['person_talk']
                news = action['oneToone_talk']
                if other_name != nick_name:
                    threading.Thread(target=person_talk, args=(other_name, nick_name, news)).start()  # 接收邀请聊天消息并转发

            # elif 'files_connect' in action:
            #     conn_3, addr_3 = sock_3.accept()
            #     threading.Thread(target=file_change.recv_files, args=(conn_3, )).start()   #开启线程传文件

            else:
                new_action = nick_name + ':' + action
                new_action = new_action.encode()
                new_action_len = '{:<15}'.format(len(new_action))
                for list in address:  # address结构[[第一个用户], [第二个用户], .....]
                    send_conn = list[0][0]  # list结构[(套接字),用户]
                    if send_conn is not conn:
                        try:
                            send_conn.send(new_action_len.encode())
                            send_conn.send(new_action)
                        except:
                            address.remove([(send_conn,), nick_name])
                            send_conn.close()
    except Exception as e:
            print(e)
    finally:
        address.remove([(conn,), nick_name])
        active_people()        #重新更新在线人数

        down = dict()                         #提示某人下线
        down['down_line'] = nick_name
        down = json.dumps(down, ensure_ascii=False)
        down = down.encode()
        down_len = '{:<15}'.format(len(down))
        for list in address:
            send_conn = list[0][0]
            if send_conn is not conn:
                try:
                    send_conn.send(down_len.encode())         # 发送下线消息
                    send_conn.send(down)
                except:
                    pass

        conn.close()
        # print(address)
        print('端口2连接关闭')


def active_people():
    '''给每个上线的客户端发送所有在线人数'''
    line_people = dict()
    line = []
    chi = 0
    for list in address:
        user_name = list[1]
        line.append(user_name)
    line_people['active_people'] = line
    line_people = json.dumps(line_people, ensure_ascii=False)
    line_people = line_people.encode()
    user_name_len = '{:<15}'.format(len(line_people))
    for list in address:
        send_conn = list[0][0]
        try:
            send_conn.send(user_name_len.encode())  # 发送下线消息
            send_conn.send(line_people)
        except:
            pass


def up_people(nick_name):
    '''客户端上线提醒'''
    up = dict()
    up['up_line'] = nick_name
    up_data = json.dumps(up, ensure_ascii=False)
    up_data = up_data.encode()
    down_len = '{:<15}'.format(len(up_data))
    for list in address:
        send_conn = list[0][0]
        try:
            send_conn.send(down_len.encode())  # 发送下线消息
            send_conn.send(up_data)
        except:
            pass



def person_talk(other_name, nick_name, news):
    '''单人聊天接收到客户端`请求，并将请求转发目标客户端2'''
    list = filter(lambda x: other_name == x[1], address)
    for i in list:
        conn = i
    conn = conn[0][0]
    req_head = dict()
    try:
        req_head['person_talk'] = nick_name
        req_head['oneToone_talk'] = news
        req_head_data = json.dumps(req_head, ensure_ascii=False)
        req_head_data = req_head_data.encode()
        req_head_len = '{:<15}'.format(len(req_head_data))
        conn.send(req_head_len.encode())
        conn.send(req_head_data)
    except Exception as f:
        print(f)



def welcome_user(conn, nick_name):
    '''欢迎信息'''
    new_people = dict()
    new_people['welcome_uppeople'] = nick_name
    # abc = re.sub("['A-Za-z0-9_\!\%\[\]\,\。:./?@;#$^&*`+=(){}]", "", nick_name)  # 匹配中文字符,中文字节+2
    line_people = json.dumps(new_people, ensure_ascii=False)
    line_people = line_people.encode()
    user_name_len = '{:<15}'.format(len(line_people))
    try:
        conn.send(user_name_len.encode())  # 发送下线消息
        conn.send(line_people)
    except:
        pass





def recv_files(conn, nick_name):
    global A
    try:
        while True:
            file_len = conn.recv(15).decode()      # 消息长度
            if not file_len:
                break
            data_len = int(file_len.strip())
            file_data = recved_main(data_len, conn)
            if 'down_file_list' in file_data:
                send_file_list(conn)         #发送文件列表

            elif 'down_files' in file_data:          #下载文件或者文件夹请求
                files_info = json.loads(file_data)
                print('有问题吗')
                if files_info['down_files'] == 'everyone':
                    if files_info['files_type'] == 'files':         #文件类型
                        down_one_file(files_info, conn)
                    else:
                        print(1)
                        dirs_path = os.path.join(PATH, files_info['files_name'])
                        print(dirs_path,'哈哈哈哈')
                        for root, dirs, files in os.walk(dirs_path):
                            if len(dirs) == 0 and len(files) == 0:
                                empty = root[len(dirs_path)+1:]
                                empty_dir = empty
                                print('空文件夹', empty_dir)
                                down_empty_dir(empty_dir, conn)
                                continue

                            for f in files:
                                file_abs_path = os.path.join(root, f)
                                print(file_abs_path, 999)
                                the_fi = file_abs_path[len(PATH) + 1:]
                                files_info['files_name'] = the_fi
                                down_one_file(files_info, conn)

                        finish = 'finish'
                        finish = finish.encode()
                        finish_len = '{:<15}'.format(len(finish))
                        conn.send(finish_len.encode())
                        conn.send(finish)
                else:
                    file_list = []
                    recv_name = files_info['down_files']
                    list = os.listdir(PATH_2)
                    print(list, '存放目录')
                    for i in list:
                        j = i.split(',')
                        file_list.append(j)
                    ld = filter(lambda x: recv_name == x[1], file_list)
                    for k in ld:
                        jk = k
                    current = jk[0] +','+ jk[1]
                    path = os.path.join(PATH_2, current)
                    print(path, 'path')
                    list_2 = filter(lambda x: recv_name == x[1], File_list)
                    for i in list_2:
                        the_sock_2 = i
                    print(path, '这个人的文件地址')
                    the_file_info = os.listdir(path)
                    for i in the_file_info:
                        j = os.path.join(path, i)
                        if os.path.isfile(j):
                            print(j, '文件的最终地址')
                            down_one_file_person(path, j, the_sock_2[0], recv_name)
                            the_complete = 'file_complete'
                            the_complete = the_complete.encode()
                            the_complete_len = '{:<15}'.format(len(the_complete))
                            the_sock_2[0].send(the_complete_len.encode())
                            the_sock_2[0].send(the_complete)
                            os.remove(j)   #删除该文件
                        else:
                            for root, dirs, files in os.walk(j):
                                if len(dirs) == 0 and len(files) == 0:
                                    empty = root[len(j) + 1:]
                                    empty_dir = empty
                                    print('空文件夹', empty_dir)
                                    down_empty_dir_person(path, empty_dir, the_sock_2[0], recv_name)
                                    continue

                                for f in files:
                                    file_abs_path = os.path.join(root, f)
                                    print(file_abs_path, 999)
                                    down_one_file_person(path, file_abs_path, the_sock_2[0], recv_name)
                            the_complete = 'file_complete'
                            the_complete = the_complete.encode()
                            the_complete_len = '{:<15}'.format(len(the_complete))
                            the_sock_2[0].send(the_complete_len.encode())
                            the_sock_2[0].send(the_complete)
                            os.removedirs(j)       #删除目录
            else:
                file_data = json.loads(file_data)
                if file_data['up_files'] == 'everyone':
                    file_info = file_data['files_information']
                    file_name = file_info['files_name']
                    file_size = file_info['files_size']
                    file_size = int(file_size)
                    if file_size == -1:  # 如果为空文件夹
                        os.makedirs(os.path.join(PATH, file_name), exist_ok=True)
                        continue
                    else:
                        file_md5 = file_info['files_md5']
                        dir_file = os.path.dirname(file_name)
                        if len(dir_file) == 0:
                            print(file_name, '单个文件名')
                            local_file_name = os.path.join(PATH, file_name)
                            recv_size = 0
                            with open(local_file_name, 'wb')as f:
                                while recv_size < file_size:
                                    file_tmp = conn.recv(file_size - recv_size)
                                    if not file_tmp:
                                        break
                                    f.write(file_tmp)
                                    recv_size += len(file_tmp)

                            the_md5 = check_md5(local_file_name)
                            if the_md5 == file_md5:
                                action = dict()
                                action['files_req'] = 0
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                            else:
                                A = 1
                                action = dict()
                                action['files_req'] = 1
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                                break

                        else:
                            print(dir_file, '文件的上级文件夹名')
                            os.makedirs(os.path.join(PATH, dir_file), exist_ok=True)
                            local_file_name = os.path.join(PATH, file_name)

                            recv_size = 0
                            with open(local_file_name, 'wb')as f:
                                while recv_size < file_size:
                                    file_tmp = conn.recv(file_size - recv_size)
                                    if not file_tmp:
                                        break
                                    f.write(file_tmp)
                                    recv_size += len(file_tmp)
                            the_md5 = check_md5(local_file_name)
                            if the_md5 == file_md5:
                                action = dict()
                                action['files_req'] = 0
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                            else:
                                A = 1
                                action = dict()
                                action['files_req'] = 1
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                                break

                else:                  #单人文件上传
                    new_dir = os.path.join(PATH_2, file_data['up_files'])
                    os.makedirs(new_dir, exist_ok=True)
                    file_info = file_data['files_information']
                    file_name = file_info['files_name']
                    file_size = file_info['files_size']
                    file_size = int(file_size)
                    if file_size == -1:  # 如果为空文件夹
                        os.makedirs(os.path.join(new_dir, file_name), exist_ok=True)
                        continue
                    else:
                        file_md5 = file_info['files_md5']
                        dir_file = os.path.dirname(file_name)
                        if len(dir_file) == 0:
                            print(file_name, '单个文件名')
                            local_file_name = os.path.join(new_dir, file_name)
                            recv_size = 0
                            with open(local_file_name, 'wb')as f:
                                while recv_size < file_size:
                                    file_tmp = conn.recv(file_size - recv_size)
                                    if not file_tmp:
                                        break
                                    f.write(file_tmp)
                                    recv_size += len(file_tmp)

                            the_md5 = check_md5(local_file_name)
                            if the_md5 == file_md5:
                                action = dict()
                                action['send_to_recv'] = file_data['up_files'].split(',')[0]
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                send_name = file_data['up_files'].split(',')[1]
                                list = filter(lambda x: send_name == x[1], File_list)
                                for i in list:
                                    the_sock = i
                                the_sock[0].send(action_len.encode())
                                the_sock[0].send(action)
                            else:
                                A = 1
                                action = dict()
                                action['files_req_person'] = 1
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                                break

                        else:
                            print(dir_file, '文件的上级文件夹名')
                            os.makedirs(os.path.join(new_dir, dir_file), exist_ok=True)
                            local_file_name = os.path.join(new_dir, file_name)

                            recv_size = 0
                            with open(local_file_name, 'wb')as f:
                                while recv_size < file_size:
                                    file_tmp = conn.recv(file_size - recv_size)
                                    if not file_tmp:
                                        break
                                    f.write(file_tmp)
                                    recv_size += len(file_tmp)
                            the_md5 = check_md5(local_file_name)
                            if the_md5 == file_md5:
                                action = dict()
                                action['files_req_person'] = 1
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                            else:
                                A = 1
                                action = dict()
                                action['files_req_person'] = 1
                                action['files_name'] = file_name
                                action = json.dumps(action, ensure_ascii=False)
                                action = action.encode()
                                action_len = '{:<15}'.format(len(action))
                                conn.send(action_len.encode())
                                conn.send(action)
                                break
        # print('端口3连接关闭！')
    except Exception as f:
        print(f)
        conn.close()

    finally:
        File_list.remove([conn, nick_name])
        conn.close()
        print('端口3连接关闭')

def check_md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb')as e:
        while True:
            data = e.read(1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest().upper()

def send_file_list(conn):
    LIST = []
    files_list = os.listdir(PATH)
    for i in files_list:
        if os.path.isfile(os.path.join(PATH, i)):
            LIST.append('File:' + i)
        else:
            LIST.append('Dirs:' + i)
    down_file_list = dict()
    down_file_list['down_file'] = LIST
    down_file_list = json.dumps(down_file_list)     #字典转字符串
    down_file_list = down_file_list.encode()       #编码
    down_file_list_len = '{:<15}'.format(len(down_file_list))
    conn.send(down_file_list_len.encode())
    conn.send(down_file_list)

def down_one_file(files_info, conn):
    abs_path = os.path.join(PATH, files_info['files_name'])
    send_file = dict()
    send_file['TO_send'] = 'everyone'
    send_file['files_name'] = files_info['files_name']
    send_file['files_size'] = os.path.getsize(abs_path)
    send_file['files_md5'] = check_md5(abs_path)
    send_file = json.dumps(send_file, ensure_ascii=False)
    send_file = send_file.encode()
    send_file_len = '{:<15}'.format(len(send_file))
    conn.send(send_file_len.encode())
    conn.send(send_file)

    print(os.path.join(PATH, files_info['files_name']))
    with open(os.path.join(PATH, files_info['files_name']), 'rb') as r:
        while True:
            data = r.read(1024)
            if not data:
                break
            conn.send(data)


def down_one_file_person(path, i, conn, recv_name):
    send_file = dict()
    send_file['TO_send'] = recv_name
    send_file['files_name'] = i[len(path)+1:]
    send_file['files_size'] = os.path.getsize(i)
    print(send_file['files_name'], '文件名')
    send_file = json.dumps(send_file, ensure_ascii=False)
    send_file = send_file.encode()
    send_file_len = '{:<15}'.format(len(send_file))
    conn.send(send_file_len.encode())
    conn.send(send_file)
    with open(i, 'rb') as r:
        while True:
            data = r.read(1024)
            if not data:
                break
            conn.send(data)


def down_empty_dir(root, conn):
    try:
        send_file = dict()
        send_file['TO_send'] = 'everyone'
        send_file['files_name'] = root
        send_file['files_size'] = -1
        send_file['files_md5'] = '暂无'
        send_file = json.dumps(send_file, ensure_ascii=False)
        send_file = send_file.encode()
        send_file_len = '{:<15}'.format(len(send_file))
        conn.send(send_file_len.encode())
        conn.send(send_file)
    except Exception as f:
        print(f)


def down_empty_dir_person(path, root, conn, recv_name):
    try:
        send_file = dict()
        send_file['TO_send'] = recv_name
        send_file['files_name'] = root[len(path)+1:]
        send_file['files_size'] = -1
        send_file = json.dumps(send_file, ensure_ascii=False)
        send_file = send_file.encode()
        send_file_len = '{:<15}'.format(len(send_file))
        conn.send(send_file_len.encode())
        conn.send(send_file)
    except Exception as f:
        print(f)



def main():
    while True:
        conn, addr= sock.accept()
        print(addr,"端口1已连接")
        threading.Thread(target=login_register, args=(conn,)).start()



if __name__ == '__main__':
    main()





