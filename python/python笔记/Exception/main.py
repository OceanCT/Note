import sys
import datetime
import socket
import threading
# sys.stdin = open('in','r')
# sys.stdout = open('out','w')
###################################################################################################################

import poplib
import getpass
user = '@qq.com'
pwd = 'adsfs'
s = poplib.POP3(host)
s.user(user)
s.pass_(pwd)
mboxstat = M.stat()
print(mboxstat[0])
lis = s.list()
mailx = s.retr(3)[1]
for line in mailx:
	print(line)