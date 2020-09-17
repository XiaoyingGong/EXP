# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/7 15:05  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as io
import os


mats_path = "../dataset/RS_inlier_ratio_change/"
mats_path = "../dataset/RS_inlier_ratio_change/"
# dic_list = ['RS_01', 'RS_02', 'RS_03', 'RS_04', 'RS_05', 'RS_06', 'RS_07', 'RS_08', 'RS_09']
# dic_list = ['RS_09']
dic_list = ["SUAV1"]
# mats_path = "../dataset/"
# dic_list = ['chen_mixture_dataset']
for dic in dic_list:
    cur_mats_path = mats_path + dic + "/"
    mats_list = os.listdir(cur_mats_path)
    mats_list = ["3010.mat"]
    for j in range(len(mats_list)):
        cur_mat_path = cur_mats_path + mats_list[j]
        cur_mat = io.loadmat(cur_mat_path)

        ground_truth = cur_mat["ground_truth"].flatten()
        img_x = cur_mat["img_x"]
        img_y = cur_mat["img_y"]
        X = cur_mat["X"]
        Y = cur_mat["Y"]

        color_map = ['black', 'blue']
        print("当前的mats为：", mats_list[j])
        print("总计的点数为:", len(X))
        print("inlier率为%.2f", np.sum(ground_truth)/len(ground_truth))
        plt.axis("off")
        plt.imshow(np.hstack((img_x, img_y)))
        plt.scatter(X[:, 0], X[:, 1], c='r')
        plt.scatter(Y[:, 0]+img_x.shape[1], Y[:, 1], c='r')

        for i in range(len(X)):
            if ground_truth[i] == 0:
                plt.plot([X[i, 0], Y[i, 0]+img_x.shape[1]], [X[i, 1], Y[i, 1]], c=color_map[ground_truth[i]])
        for i in range(len(X)):
            if ground_truth[i] == 1:
                plt.plot([X[i, 0], Y[i, 0]+img_x.shape[1]], [X[i, 1], Y[i, 1]], c=color_map[ground_truth[i]])
        plt.show()
