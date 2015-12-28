#!/usr/bin/python
#-*- coding:utf-8 -*-
#Filename:back.py
#Author:kaka
#data:2015/12/28

import Tkinter
import os
import time

def backup():
    global entry_source
    global entry_target
    source = entry_source.get()
    target_dir = entry_target.get()

    today_dir = target_dir + time.strftime('%Y%m%d')
    time_dir = time.strftime('%H%M%S')

    touch = today_dir + os.sep + time_dir + '.zip'
    command_touch = "zip -qr" + touch + ' ' + source

    print command_touch
    print source
    print target_dir
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)
    if not os.system(command_touch):
        print "Success backup"
    else:
        print "Failed backup"

root = Tkinter.Tk()
root.title("BackUp")
root.geometry("200x200")
#第一行的两个控件
lbl_source = Tkinter.Label(root, text='Source')
lbl_source.grid(row=0, column=0)
entry_source = Tkinter.Entry(root)
entry_source.grid(row=0,column=1)
#第二行的两个控件
lbl_target = Tkinter.Label(root, text='Target')
lbl_target.grid(row=1, column=0)
entry_target = Tkinter.Entry(root)
entry_target.grid(row=1,column=1)
#第三行的一个按钮控件
but_back = Tkinter.Button(root,text='BackUp')
but_back.grid(row=3, column=0)
but_back["command"] = backup
#界面的开始
root.mainloop()
