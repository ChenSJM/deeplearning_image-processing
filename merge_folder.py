# -*- coding:utf-8 -*-
import os
import cv2
from expand_pics import rotate_expand
import shutil


def save_pic(pic, save_path, k):
    cv2.imwrite(save_path + '/%d.jpg' % k, pic)

def get_name():
    x = []
    str = raw_input('输入要合并的文件夹名，以回车键分开，输入为空结束：')
    while str:
        x.append(str)
        str = raw_input('输入要合并的文件夹名，以回车键分开，输入为空结束：')
    return x

def merge_folder(arr, save_path):
    num = 1
    for i in arr:
        files = os.listdir(i)
        for pic in files:
            try:
                pic = cv2.imread(i + '/' + pic)
                pic = cv2.resize(pic, (300, 400), interpolation=cv2.INTER_CUBIC)
                save_pic(pic, save_path, num)
                num += 1
            except Exception:
                continue



if __name__ == '__main__':
    new_folder = 'test_merge'
    while os.path.exists(new_folder):
        new_folder = raw_input('已重复，请重新输入名字：')
    os.mkdir(new_folder)
    # os.mkdir(new_folder+str(123))
    x = []
    for i in range(0, 3):
        x.append('noise_' + str(i))
    merge_folder(x, new_folder)
    # rotate_expand(new_folder+str(123), new_folder)