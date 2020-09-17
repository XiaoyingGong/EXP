# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/8 15:58  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from demostration_of_data import plot_feature_matching as pfm

f = open('../dataset/FIRE/Ground Truth/control_points_A01_1_2.txt')

X = []
Y = []
data = f.readlines()
for i in range(len(data)):
    cur_data = data[i][:-1]
    cur_coor = cur_data.split(" ")
    X.append([float(ele) for ele in cur_coor[:2]])
    Y.append([float(ele) for ele in cur_coor[2:4]])

img_1 = cv2.imread('../dataset/FIRE/Images/A01_1.jpg')[:, :, [2, 1, 0]]
img_2 = cv2.imread('../dataset/FIRE/Images/A01_2.jpg')[:, :, [2, 1, 0]]

X = np.array(X)
Y = np.array(Y)

pfm.plot_image_pair_and_matching(img_1, img_2, X, Y, np.ones(len(X)))

plt.show()
