import json
import os.path
import hashlib, threading



PATH = r'D:\笔记\临时文件传输'
A = 0


def recv_files(conn):
    global A
    try:
        while True:
            file_len = conn.recv(15).decode()      # 消息长度
            print(1)
            if not file_len:
                break
            data_len = int(file_len.strip())
            print(2)
            file_data = recved_main(data_len, conn)
            print(3)
            file_data = json.loads(file_data)
            print(4)
            if file_data['up_files'] == 'everyone':
                print(5)
                file_info = file_data['files_information']
                file_name = file_info['files_name']
                file_size = file_info['files_size']
                file_size = int(file_size)
                print(6)
                if file_size == -1:  # 如果为空文件夹
                    os.makedirs(os.path.join(PATH, file_name), exist_ok=True)
                    continue
                else:
                    print(7)
                    file_md5 = file_info['files_md5']
                    print(8)
                    dir_file = os.path.dirname(file_name)
                    if len(dir_file) == 0:
                        print(9)
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
                        print(10)
                        print(dir_file, '文件的上级文件夹名')
                        print(11)
                        os.makedirs(os.path.join(PATH, dir_file), exist_ok=True)
                        print(12)
                        local_file_name = os.path.join(PATH, file_name)
                        print(13)

                        recv_size = 0
                        print(14)
                        with open(local_file_name, 'wb')as f:
                            while recv_size < file_size:
                                file_tmp = conn.recv(file_size - recv_size)
                                if not file_tmp:
                                    break
                                f.write(file_tmp)
                                recv_size += len(file_tmp)
                        print(15)
                        the_md5 = check_md5(local_file_name)
                        print(16)
                        if the_md5 == file_md5:
                            action = dict()
                            action['files_req'] = 0
                            action['files_name'] = file_name
                            action = json.dumps(action, ensure_ascii=False)
                            action = action.encode()
                            action_len = '{:<15}'.format(len(action))
                            conn.send(action_len.encode())
                            conn.send(action)
                            print(17)
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
        # print('端口3连接关闭！')
    except Exception as f:
        print(f)
        conn.close()


def check_md5(file_name):
    m = hashlib.md5()
    with open(file_name, 'rb')as e:
        while True:
            data = e.read(1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest().upper()


def recved_main(data_len, conn):
    '''接收报文正文'''
    size = 0
    tmp = b''
    while size < data_len:
        data = conn.recv(data_len - size)
        if not data:
            break
        tmp += data
        size += len(data)
    tmp = tmp.decode()
    return tmp