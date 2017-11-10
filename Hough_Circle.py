# -*- coding:UTF-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2.cv as cv
from get_sift_point import get_points
import math

def get_distance(p, x):
    arr = []
    for i in x:
        arr.append(math.sqrt(math.pow(i[0] - p[0], 2) + math.pow(i[1] - p[1], 2)))
    return arr



def get_circle(original, img, temp):
    h1, w1 = img.shape[:2]
    gray = img
    plt.subplot(221), plt.imshow(gray, 'gray')
    plt.xticks([]), plt.yticks([])
    points = get_points(original, temp)
    circles1 = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 100, param2=30, minRadius=50)
    circles = circles1[0, :, :]         # 提取为二维
    circles = np.uint16(np.around(circles))         # 四舍五入，取整
    for i in circles[:]:
        p = (i[0], i[1])
        arr = get_distance(p, points)
        if i[2] > max(arr):
            cv2.circle(original, (i[0], i[1]), i[2], (255, 0, 0), 3)        # 画圆
            cv2.circle(original, (i[0], i[1]), 2, (255, 0, 255), 3)        # 画圆心
        else:
            continue
        # cv2.circle(original, (i[0], i[1]), i[2], (255, 0, 0), 3)  # 画圆
        # cv2.circle(original, (i[0], i[1]), 2, (255, 0, 255), 3)  # 画圆心

    plt.subplot(222), plt.imshow(img)
    plt.subplot(223), plt.imshow(original)
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('D://731.JPG', 0)
    temp = cv2.imread('D://temp.PNG', 0)
    # print get_points(img, temp)
    f = cv2.Canny(img, 50, 150)
    f = cv2.GaussianBlur(f, (3, 3), 0)
    get_circle(img, f, temp)


