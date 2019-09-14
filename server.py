import socket
import json
import threading
import smtp_mail
import server_mysql
import file_change


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
                    print(addr_3, '端口3已连接')
                    threading.Thread(target=file_change.recv_files, args=(conn_3,)).start()


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



def main():
    while True:
        conn, addr= sock.accept()
        print(addr,"端口1已连接")
        threading.Thread(target=login_register, args=(conn,)).start()



if __name__ == '__main__':
    main()





