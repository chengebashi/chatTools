import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
import server_mysql
import hashlib

def random_pd():
    b = ''
    for i in range(4):
        a = chr(random.randint(97, 123))
        b = b + a
    for j in range(4):
        a = str(random.randint(1, 9))
        b = b + a

    return b




def mail(b, recv):
    # 第三方 SMTP 服务b
    mail_host = "smtp.exmail.qq.com"  # 设置服务器
    mail_user = "chenge@chenge.online"  # 用户名
    mail_pass = "QrwdCHPzdZPga835"  # 口令

    sender = 'chenge@chenge.online'
    receivers = [recv, ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(b, 'plain', 'utf-8')
    message['From'] = Header("chenge", 'utf-8')
    message['To'] = Header("myself", 'utf-8')

    subject = '新密码'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        print(1)
        smtpObj = smtplib.SMTP_SSL(mail_host)
        print(2)
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        print(3)
        smtpObj.login(mail_user, mail_pass)
        print(4)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return 0
    except smtplib.SMTPException:
        return 1


def passwd_md5(b):
    m = hashlib.md5()
    m.update(b.encode())
    return m.hexdigest().upper()


def main(recv):
    b = random_pd()
    mail(b, recv)
    pd_md5 = passwd_md5(b)
    server_mysql.modify_pd(recv, pd_md5)
