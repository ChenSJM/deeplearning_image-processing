# -*- coding:utf-8 -*-
from sklearn import model_selection
import cv2
import os
import numpy as np


def get_data(path1, path2):
    X = []
    files1 = os.listdir(path1)
    files2 = os.listdir(path2)
    min_len = min(len(files1), len(files2))
    y = [1.0, 0.0] * min_len
    for i in range(0, min_len):
        # 压入正确数据
        pic1 = path1 + '/' + files1[i]
        single = cv2.imread(pic1, 0)
        single = cv2.resize(single, (300, 400), interpolation=cv2.INTER_CUBIC)
        X.append(single/255.0)
        # 压入噪音
        pic2 = path2 + '/' + files2[i]
        single = cv2.imread(pic2, 0)
        single = cv2.resize(single, (300, 400), interpolation=cv2.INTER_CUBIC)
        X.append(single / 255.0)
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test

    # for image in range(1, 3001):
    #     path = DataSet + str(image) + ".jpg"
    #     single = cv2.imread(path)
    #     pic = cv2.cvtColor(single, cv2.COLOR_BGR2HSV)
    #     single = cv2.resize(pic, (64, 64), interpolation=cv2.INTER_CUBIC)
    #     # ---------------------------------------
    #     single = single / 255.0  # 归一化
    #     X.append(single)
    # X = np.array(X)
    # y = np.array(y)
    # X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    # # X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
    # # cross_validation在scikit-learn 0.18中已经被丢弃了
    # return X_train, X_test, y_train, y_test