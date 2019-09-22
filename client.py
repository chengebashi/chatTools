import socket
import json,hashlib
import re

server = json.load(open('./client_conf.json'))
sock = socket.socket()
sock.connect(("47.100.253.248", server['server_port_1']))


def login(arg):
    '''客户端登录请求'''
    sum = dict()
    sum["login"] = 1
    sum["args"] = arg
    sum = json.dumps(sum)
    sum = sum.encode()
    sum_len = '{:<15}'.format(len(sum))   #报头长度
    sock.send(sum_len.encode())            #发送报头长度
    sock.send(sum)     #发送报文
    ret_len = sock.recv(15).decode()   #接收响应长度
    ret_len = int(ret_len.strip())

    ret = recved_main(ret_len)   #接收报文长度
    ret = json.loads(ret)
    back = ret["return"]

    return back


def register(reg):
    sum = dict()
    sum["login"] = 2
    sum["args"] = reg
    # abc = re.sub("[{A-Za-z0-9\!\%\[\]\,\。}]", "", sum["args"]['nick_name'])  # 匹配中文字符,中文字节+2
    sum = json.dumps(sum, ensure_ascii=False)
    sum = sum.encode()
    sum_len = '{:<15}'.format(len(sum))  # 报头长度
    sock.send(sum_len.encode())  # 发送报头长度
    sock.send(sum)  # 发送报文
    ret_len = sock.recv(15).decode()  # 接收响应长度
    ret_len = int(ret_len.strip())

    ret = recved_main(ret_len)  # 接收报文长度
    ret = json.loads(ret)

    back = ret["return"]

    return back

def update(args):
    sum = dict()
    sum["login"] = 3
    sum["args"] = args
    sum = json.dumps(sum)
    sum = sum.encode()
    sum_len = '{:<15}'.format(len(sum))  # 报头长度
    sock.send(sum_len.encode())  # 发送报头长度
    sock.send(sum)  # 发送报文
    ret_len = sock.recv(15).decode()  # 接收响应长度
    ret_len = int(ret_len.strip())

    ret = recved_main(ret_len)  # 接收报文长度

    ret = json.loads(ret)
    back = ret["return"]

    return back

def forget_pd(args):
    sum = dict()
    sum["login"] = 4
    sum["args"] = args
    sum = json.dumps(sum)
    sum = sum.encode()
    sum_len = '{:<15}'.format(len(sum))  # 报头长度
    sock.send(sum_len.encode())  # 发送报头长度
    sock.send(sum)  # 发送报文
    ret_len = sock.recv(15).decode()  # 接收响应长度
    ret_len = int(ret_len.strip())

    ret = recved_main(ret_len)  # 接收报文长度

    ret = json.loads(ret)
    back = ret["return"]

    return back



def exit():
    global sock
    sum = dict()
    sum["login"] = 0
    sum = json.dumps(sum)
    sum = sum.encode()
    sum_len = '{:<15}'.format(len(sum))  # 报头长度
    sock.send(sum_len.encode())  # 发送报头长度
    sock.send(sum)  # 发送报文
    sock.close()


def recved_main(data_len):
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


def passwd_md5(b):
    m = hashlib.md5()
    m.update(b.encode())
    return m.hexdigest().upper()