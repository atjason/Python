# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'chee_xxx@sohu.com'
password = 'PASSWORD'
to_addr = 'qui_xxx@gmail.com'
smtp_server = 'smtp.sohu.com'

msg = MIMEText(u"I'm the email content.", "plain", "utf-8")
msg['From'] = _format_addr(u'Python Lover <%s>' % from_addr)
msg['To'] = _format_addr(u'Manager <%s>' % to_addr)
msg['Subject'] = Header(u'Congratulations to you.', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

