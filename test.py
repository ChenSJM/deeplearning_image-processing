# -*- coding:UTF-8 -*-
from Tkinter import *
from tkMessageBox import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s = '手表 仪表'
s.decode()
s = s.split(' ')
print s[0].decode()