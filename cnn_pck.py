# -*- coding:utf-8 -*-
import xlsxwriter
from sklearn import model_selection
from sknn.mlp import Classifier, Layer, Convolution
import cv2
import numpy as np
import pickle
import time
import os

currentPath = os.getcwd() + "/"


def get_nn_pck(X_train, X_test, y_train, y_test, c1=16, k1=9, p1=2, c2=14, k2=7, p2=2, c3=10, k3=3, p3=2):
    currentTime = str(time.strftime('%Y%m%d %H%M%S', time.localtime(time.time())))
    dirPath = currentPath + currentTime + 'canshu' + '%d-%d-%d-%d-%d-%d-%d-%d-%d' % (c1, k1, p1, c2, k2, p2, c3, k3, p3) + "/"
    excelPath = dirPath + "resLog.xlsx"
    os.mkdir(dirPath)
    # 创建一个excel文件，当前时间命名
    workbook = xlsxwriter.Workbook(excelPath)
    # 创建一个工作表对象
    worksheet = workbook.add_worksheet()
    worksheet.write("A1", "epochs")
    worksheet.write("B1", "Train-Score")
    worksheet.write("C1", "Test-Score")
    result = []
    for i in range(1, 10):
        nn = Classifier(
            layers=[
                Convolution('Rectifier', channels=c1, kernel_shape=(k1, k1), border_mode='full', pool_shape=(p1, p1)),
                # border_mode = 'full',没有stride
                Convolution('Rectifier', channels=c2, kernel_shape=(k2, k2), border_mode='full', pool_shape=(p2, p2)),
                # border_mode = 'full',没有stride
                Convolution('Rectifier', channels=c3, kernel_shape=(k3, k3), border_mode='full', pool_shape=(p3, p3)),
                Layer('Rectifier', units=32, ),
                Layer('Rectifier', units=32, ),
                Layer('Softmax', units=2)],
            learning_rule="sgd",
            learning_rate=0.015,
            learning_momentum=0.9,
            weight_decay=0.001,
            n_iter=i,
            n_stable=10,
            f_stable=0.001,
            valid_size=0.1,
            verbose=True)
        nn.fit(X_train, y_train)

        pickle.dump(nn, open(dirPath + "nn" + str(i) + ".pkl", 'wb'))

        worksheet.write("A" + str(i + 1), i)
        worksheet.write("B" + str(i + 1), nn.score(X_train, y_train))
        worksheet.write("C" + str(i + 1), nn.score(X_test, y_test))
        result.append(nn.score(X_test, y_test))
    workbook.close()
    return max(result)