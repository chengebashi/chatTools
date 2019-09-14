import pymysql

conf = dict()
conf = {"db_server_ip": "127.0.0.1",
        "db_server_port": 3306,
        "db_user": "chenge",
        "db_password": "chenge",
        "db_name": "mydb"
        }

#注册验证

def check_nick_name(nick_name):
    '''
    校验用户名是否存在
    :param user_name:
    :return:0 表示存在， 1表示不存在
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'], passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("select nick_name from users where nick_name = '{}'".format(nick_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0     #用户名存在
    else:
        return 1     #用户名不存在



def check_user_name(user_name):
    '''
    校验账号是否存在
    :param password:
    :return: 0表示存在， 1表示不存在
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("select user_name from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0  # 账号存在
    else:
        return 1  # 账号不存在



def check_email(email):
    '''
    检验邮箱是否存在
    :param email:
    :return: 0表示存在， 1表示不存在
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("select email from users where email = '{}'".format(email))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows:
        return 0  # 邮箱存在
    else:
        return 1  # 邮箱不存在



#登录验证


def check_password(user_name, password):
    '''
    校验密码是否正确
    :param user_name, password:
    :return:
    '''

    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("select passwd from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()

    finally:
        conn.close()

    if rows[0] == password:
        return 0  # 密码正确
    else:
        return 1  # 密码错误


#忘记密码


def modify_pd(email, password):
    '''
    根据邮箱改密码
    :param email,password:
    :return:
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")
    try:
        with conn.cursor() as cur:
            cur.execute("update users set passwd = '{}' where email = '{}'".format(password, email))
            conn.commit()
    finally:
        conn.close()



def update_passwd(user_name, news_passwd):
    '''
    修改密码
    :return:
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("update users set passwd = '{}' where user_name = '{}'".format(news_passwd, user_name))
            conn.commit()
    finally:
        conn.close()



def add_user(information):
    '''
    添加用户
    :return:
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("insert into users values ('{}', '{}', '{}', '{}', '{}')".format(information['nick_name'], information['user_name'], information['password'], information['phone'], information['email']))
            conn.commit()
    finally:
        conn.close()




def select_nick_name(user_name):
    '''
    根据用户名找昵称
    :param user_name:
    :return:
    '''
    conn = pymysql.connect(host=conf['db_server_ip'], port=conf['db_server_port'], user=conf['db_user'],
                           passwd=conf['db_password'], db=conf["db_name"], charset="utf8")

    try:
        with conn.cursor() as cur:
            cur.execute("select nick_name from users where user_name = '{}'".format(user_name))
            rows = cur.fetchone()
    finally:
        conn.close()

    return rows[0]




