import json
import os.path
import hashlib, threading



PATH = r'D:\笔记\临时文件传输'
A = 0


def recv_files(conn, nickname):
    global A
    global File_list
    print(File_list)
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
        # print('端口3连接关闭！')
    except Exception as f:
        print(f)
        conn.close()

    finally:
        File_list.remove()


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
    print('到这儿了吗')
    print(os.path.join(PATH, files_info['files_name']))
    with open(os.path.join(PATH, files_info['files_name']), 'rb') as r:
        while True:
            data = r.read(1024)
            if not data:
                break
            conn.send(data)
    print('不知道啊')



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