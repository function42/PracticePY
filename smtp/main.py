# -*- coding: utf-8 -*-

#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'xxxxx@xxxxx.com'
password = 'xxxxxxxxxxxxxxxx'
to_addr = 'yyyyyy@yyyyyy.com'
smtp_server = 'zzzz.zzzz.com'

msg = MIMEText('hello, this is a message from myself', 'plain', 'utf-8') # 邮件正文
msg['From'] = _format_addr('myself <%s>' % from_addr) # 邮件头部，发送者信息
msg['To'] = _format_addr('myself <%s>' % to_addr) # 接收者信息
msg['Subject'] = Header('备份成功', 'utf-8').encode() # 邮件主题
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) # 登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string()) # 发送邮件
server.quit()