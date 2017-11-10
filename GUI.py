# -*- coding:UTF-8 -*-
from Tkinter import *
import tkFileDialog
import time
from main_py import mainprograme
from tkMessageBox import *
import os
from baidu_pic import start_pic
import sys
from merge_folder import merge_folder
import shutil
from expand_pics import rotate_expand

reload(sys)
sys.setdefaultencoding('utf-8')

root = Tk()
path = StringVar()
path_noise = StringVar()
v = IntVar()
rate = StringVar()
key_word = StringVar()


def train_action(sample, noise, k):
    mainprograme(sample, noise, k)


def train():
    root.quit()
    sample = path.get()
    noise = path_noise.get()
    k = float(rate.get())
    showerror("即将开始训练", "点击确认按钮开始训练，结果之后会有窗口提示")
    time.sleep(10)
    train_action(sample, noise, k)


def get_baidu_pic():
    root.quit()
    showerror("即将开始训练", "点击确认按钮开始训练，结果之后会有窗口提示")
    if key_word.get() and path.get() and v.get() and rate.get():
        s = key_word.get()
        s = s.split(' ')
        sample_file = path.get()
        num = len(os.listdir(sample_file))
        avg_num = num/len(s) + 20
        # avg_num = 10
        for i in range(0, len(s)):
            folder_name = 'noise_' + str(i)
            start_pic(str(s[i].decode()), avg_num, folder_name)
        x = []
        for i in range(0, len(s)):
            x.append('noise_' + str(i))
        noise_folder = 'test_merge_noise'
        os.mkdir(noise_folder)
        try:
            merge_folder(x, noise_folder)
        except Exception:
            print
        for i in range(0, len(s)):
            shutil.rmtree('noise_' + str(i))
        k = float(rate.get())
        sample = path.get()
        # print sample, noise_folder, k
        train_action(sample, noise_folder, k)


def start():
    if path.get() and v.get() and rate.get():
        if float(rate.get())>0 and float(rate.get())<1:
            # print path.get(), v.get(), float(rate.get())
            if v.get() == 1:
                Label(root, text="噪音图片路径:").grid(row=5, column=0)
                Entry(root, textvariable=path_noise).grid(row=5, column=1)
                Button(root, text="路径选择", command=selectPath_noise).grid(row=5, column=2)
                Button(root, text="开始训练", command=train).grid(row=6, column=0, columnspan=3)
            else:
                Label(root, text="输入噪音关键词：").grid(row=5, column=0)
                Entry(root, textvariable=key_word).grid(row=5, column=1)
                Label(root, text="关键词之间以空格分开").grid(row=5, column=2)
                Button(root, text="开始训练", command=get_baidu_pic).grid(row=6, column=0, columnspan=3)
            # print path.get(), v.get(), float(rate.get())
        else:
            print '准确率存在问题'
    else:
        print '请完整填写信息'


        # if rotate_expand(path.get()):
        #     Label(root, text='expand successful').grid(row=2, column=1)
        # else:
        #     Label(root, text='failure').grid(row=2, column=1)
        # root.update_idletasks()

def selectPath():
    # path_ = tkFileDialog.askopenfilename(filetypes=[("jpg category".decode('gbk'), "jpg"), ("png category".decode('gbk'), "png")])
    path_ = tkFileDialog.askdirectory()
    path.set(path_)

def selectPath_noise():
    # path_ = tkFileDialog.askopenfilename(filetypes=[("jpg category".decode('gbk'), "jpg"), ("png category".decode('gbk'), "png")])
    path_ = tkFileDialog.askdirectory()
    path_noise.set(path_)


# def sel():
#     # selection = "You selected the option " + str(v.get())
#     if str(v.get()) == '1':
#         Label(root, text="噪音图片路径:").grid(row=3, column=0)
#         Entry(root, textvariable=path).grid(row=3, column=1)
#         Button(root, text="路径选择", command=selectPath).grid(row=3, column=2)
#     else:
#         Label(root, text="输入噪音关键词:").grid(row=3, column=0,fill=BOTH)
#         Label(root, text=str(v.get())).grid(row=3, column=0, columnspan=3)


def prepare():
    Label(root, text="样本图片路径:").grid(row=0, column=0)
    Entry(root, textvariable=path).grid(row=0, column=1)
    Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
    Label(root, text="选择噪音来源").grid(row=1, column=0)
    group = LabelFrame(root, padx=5, pady=5)
    group.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    LANGS = [
        ('local file', 1),
        ('key words', 2)]
    for lang, num in LANGS:
        Radiobutton(group, text=lang, variable=v, value=num).grid(row=2, column=num)
    Label(root, text="输入预期识别率：").grid(row=3, column=0)
    Entry(root, textvariable=rate).grid(row=3, column=1)
    Label(root, text="输入0-1之间的数").grid(row=3, column=2)
    Button(root, text="确认以上信息", command=start).grid(row=4, column=0, columnspan=3)
    # Label(root, text="图片扩容结果").grid(row=5)
    root.mainloop()

if __name__ == '__main__':
    prepare()

