import json
import os.path
import hashlib, threading



PATH = r'D:\笔记\临时文件传输'

def recv_files(conn):
        recv_one_file(conn)

def recv_one_file(conn):
    try:
        while True:
            file_len = conn.recv(15).decode()      # 消息长度
            if not file_len:
                break
            data_len = int(file_len.strip())
            file_data = recved_main(data_len, conn)
            # if 'the_out_of' in file_data:
            #     print('客户端断开')
            #     return 0
            file_data = json.loads(file_data)

            if file_data['up_files'] == 'everyone':
                file_info = file_data['files_information']
                file_name = file_info['files_name']
                file_size = file_info['files_size']
                file_md5 = file_info['files_md5']

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
                    action = dict()
                    action['files_req'] = 1
                    action = json.dumps(action)
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