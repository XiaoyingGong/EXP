# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/8 20:09  
# IDE：PyCharm 
# des: 本文件用于处理FIRE dataset
# input(s)：
# output(s)：
import numpy as np
import scipy.io as io
import cv2
import os
def read_FIRE_dataset(path, file_name):
    gt_path = path + "/Ground Truth/" + "control_points_" + file_name + "_1_2.txt"
    img_1_path = path + "/images/" + file_name + "_1.jpg"
    img_2_path = path + "/images/" + file_name + "_2.jpg"

    f = open(gt_path)
    X = []
    Y = []
    data = f.readlines()
    for i in range(len(data)):
        cur_data = data[i][:-1]
        cur_coor = cur_data.split(" ")
        X.append([float(ele) for ele in cur_coor[:2]])
        Y.append([float(ele) for ele in cur_coor[2:4]])
    f.close()
    X = np.array(X)
    Y = np.array(Y)
    img_1 = cv2.imread(img_1_path)[:, :, [2, 1, 0]]
    img_2 = cv2.imread(img_2_path)[:, :, [2, 1, 0]]
    ground_truth = np.ones(len(X))
    return X, Y, img_1, img_2, ground_truth


def main():
    path = "../dataset/FIRE/"
    file_name_list = ['A01', 'A02', 'A03', 'A04', 'A05','A06','A07','A08','A09','A10']
    save_name_list = [5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019, 5020]
    save_path = "../dataset/FIRE/processed_data_for_EXP/"

    for i in range(len(file_name_list)):
        file_name = file_name_list[i]
        save_mat_path = save_path + str(save_name_list[i]) + ".mat"
        X, Y, img_x, img_y, ground_truth = read_FIRE_dataset(path, file_name)
        io.savemat(save_mat_path, {'X':X, 'Y':Y, 'img_x':img_x, 'img_y':img_y, 'ground_truth':ground_truth.reshape([-1, 1])})

if __name__ == '__main__':
    main()