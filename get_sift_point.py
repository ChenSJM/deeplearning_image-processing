# -*- coding:utf-8 -*-
__author__ = 'chenxu'
import cv2
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

def filter_matches(kp1, kp2, matches, ratio=0.5):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs


def dist(x1, x2, y1, y2,):
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def explore_match(img, temp, kp_pairs, status=None, H=None):
    h1, w1 = temp.shape[:2]
    h2, w2 = img.shape[:2]  # h2 = 4032, w2 = 3024
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = temp
    vis[:h2, w1:w1+w2] = img
    vis = img
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

    if H is not None:
        corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        corners = np.int32( cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0) )
        cv2.polylines(vis, [corners], True, (255, 255, 255))

    if status is None:
        status = np.ones(len(kp_pairs), np.bool)
    p1 = np.int32([kpp[0].pt for kpp in kp_pairs])
    p2 = np.int32([kpp[1].pt for kpp in kp_pairs])
    x = []
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            x.append((x2, y2))
            col = (0, 255, 0)
            cv2.circle(vis, (x2, y2), 2, col, -1)
    # print x
    # plt.subplot(111), plt.imshow(vis, 'gray')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    return x

def get_points(img_gray, temp_gray):
    # img_gray = cv2.imread(img_gray, 0)
    # temp_gray = cv2.imread(temp_gray, 0)
    sift = cv2.SIFT()
    kp1, des1 = sift.detectAndCompute(temp_gray, None)
    kp2, des2 = sift.detectAndCompute(img_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_L2)
    matches = bf.knnMatch(des1, des2, k=2)
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
    if len(kp_pairs) > 4:  # 判断特征点匹配的个数，太少证明不匹配，可以使用模版匹配和sift匹配交叉验证
        x = explore_match(img_gray, temp_gray, kp_pairs)
        return x
    else:
        print 'match points too less'



if __name__ == '__main__':
    img = cv2.imread('D://731.JPG', 0)
    temp = cv2.imread('D://temp.PNG', 0)
    print get_points(img, temp)

