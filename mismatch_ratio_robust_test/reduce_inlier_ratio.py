# author: 龚潇颖(Xiaoying Gong)
# date： 2020/8/25 14:36  
# IDE：PyCharm 
# des:用于降低SUIRD数据集的inlier率
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
import os
import numpy as np
import scipy.io as io
import random


def main_process():
    category_list = ['HorizontalRotation', 'VerticalRotation',
                     'Scaling', 'Mixture', 'Extreme']
    sum = 0
    # category_list = ['HorizontalRotation']

    for category in category_list:
        src_mat = "./SUIRD/" + category + "/"
        save_mat = "./SUIRD_reduced/" + category + "/"
        dic_list = os.listdir(src_mat)

        img_num_list = [dic_list[i].split('.')[0] for i in range(len(dic_list))]

        for img_num in img_num_list:
            cur_mats = io.loadmat(src_mat + img_num + ".mat")

            X = cur_mats["X"]
            Y = cur_mats["Y"]
            img_x = cur_mats["img_x"]
            img_y = cur_mats["img_y"]
            reOrderIdx = cur_mats["reOrderIdx"].flatten()
            seed_idx = cur_mats["seed_idx"].flatten()
            ground_truth = cur_mats["ground_truth"].flatten()

            print("-----------------------------------------------------------------")
            print(img_num, "修改前的inlier率：",  np.sum(ground_truth) / len(ground_truth))

            # ------------------------ 修改后的inlier率(将原本60%的inlier去掉) ------------------------
            true_gt = np.argwhere(ground_truth == 1).flatten()
            true_gt_len = len(true_gt)
            p_true_gt_len = int(np.floor(true_gt_len*0.85))
            # 随机生成 0 到 len(ground_truth) - 1的， p_true_gt_len个要删掉的

            remove_idx = random.sample(true_gt.tolist(),  p_true_gt_len)
            # print("remove_idx:", remove_idx)
            reserve_idx = np.linspace(0, len(ground_truth)-1, len(ground_truth), dtype=int)
            reserve_idx = np.setdiff1d(reserve_idx, remove_idx)
            print("check_result", len(remove_idx) + len(reserve_idx) - len(ground_truth))
            # 去掉相应的X
            X = X[reserve_idx]
            # 去掉相应的Y
            Y = Y[reserve_idx]
            # 去掉相应的ground_truth
            ground_truth = ground_truth[reserve_idx]
            print(img_num, "修改后的inlier率：", np.sum(ground_truth) / len(ground_truth))
            ground_truth = ground_truth.reshape([-1, 1])
            print(ground_truth.shape)
            io.savemat(save_mat + img_num + ".mat", {"X":X, "Y":Y,
            "img_x":img_x, "img_y":img_y, "ground_truth":ground_truth})

main_process()



