# -*- coding:UTF-8 -*-
import os
import shutil
from cnn_pck import get_nn_pck
from get_pic_data import get_data
from expand_pics import rotate_expand
from random import choice


def mainprograme(sample, noise, k):
    DataSet = sample.split('/')[-1]
    noise_data = noise.split('/')[-1]
    new_dataset = os.getcwd() + '/' + 'expand_' + DataSet
    new_noise = os.getcwd() + '/' + 'expand_' + noise_data
    if os.path.exists(new_dataset):
        shutil.rmtree(new_dataset)
        # print 'sample already expanded!'
    os.mkdir(new_dataset)
    rotate_expand(DataSet, new_dataset)
    if os.path.exists(new_noise):
        shutil.rmtree(new_noise)
        # print 'noise already expanded!'
    os.mkdir(new_noise)
    rotate_expand(noise_data, new_noise)
    # if os.path.exists(noise):    # 用于删除百度提取出来的图片集
    #     shutil.rmtree(noise)
    X_train, X_test, y_train, y_test = get_data(new_dataset, new_noise)
    y = []
    result = 0
    while result < k:
        x = []
        c1 = choice([10, 12, 14, 16, 18, 20, 22, 24])
        k1 = choice([5, 7, 9, 11, 13, 15, 17, 19])
        p1 = choice([1, 2, 3, 4, 5, 6])
        c2 = choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
        k2 = choice([3, 5, 7, 9, 11, 13, 15, 17, 19])
        p2 = choice([1, 2, 3, 4, 5, 6])
        c3 = choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
        k3 = choice([3, 5, 7, 9, 11, 13, 15, 17, 19])
        p3 = choice([1, 2, 3, 4, 5, 6])
        x.append(c1)
        x.append(k1)
        x.append(p1)
        x.append(c2)
        x.append(k2)
        x.append(p2)
        x.append(c3)
        x.append(k3)
        x.append(p3)
        if x in y:
            continue
        else:
            y.append(x)
            result = get_nn_pck(X_train, X_test, y_train, y_test, c1, k1, p1, c2, k2, p2, c3, k3, p3)
    return True


if __name__ == '__main__':
    pic = "C:/Users/xu_chen/PycharmProjects/deeplearning_sift/test_pic"
    pic_noise = "C:/Users/xu_chen/PycharmProjects/deeplearning_sift/test_noise"
    mainprograme(pic, pic_noise, 0.5)

