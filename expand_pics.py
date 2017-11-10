# -*- coding:UTF-8 -*-
# 旋转扩增图片
import cv2
import os


def rotate_expand(filepath, save_path, len=0):
    # save_path = 'expand_' + filepath.split('/')[-1]
    # os.mkdir(save_path)
    files = os.listdir(filepath)
    for pic in files:
        img = cv2.imread(filepath + '/' + pic)
        rows, cols = img.shape[:2]
        # 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
        k = 60
        for i in range(len*360, (len+1)*360, k):
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), i, 1)
            # 第三个参数：变换后的图像大小
            res = cv2.warpAffine(img, M, (rows, cols))
            cv2.imwrite(save_path + '/%d.jpg' % (i / k), res)
        len += 1
    return True


if __name__ == '__main__':
    pic_path = 'C:/Users/xu_chen/PycharmProjects/deeplearning_sift/all_pic'
    # new_picpath = os.getcwd() + '/' + 'expand_pic'
    # os.mkdir(new_picpath)
    rotate_expand(pic_path)