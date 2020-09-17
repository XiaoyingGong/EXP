# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/7 10:36  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import scipy.io as io
import numpy as np
import os
def check_inlier_ratio(mats_path, mats_list):
    true_match_ratio_list = np.zeros(len(mats_list))
    for i in range(len(mats_list)):
        cur_mat_path = mats_path + mats_list[i]
        cur_mat = io.loadmat(cur_mat_path)
        cur_gt = cur_mat["ground_truth"].flatten()
        true_match_ratio = np.sum(cur_gt) / len(cur_gt)
        print("总点数：", len(cur_gt))
        print("true_match_数量：", np.sum(cur_gt))
        print("第%s个mat，true match率为%f"%(mats_list[i], true_match_ratio))
        true_match_ratio_list[i] = true_match_ratio
    return true_match_ratio_list

if __name__ == '__main__':
    # mats_path = "../dataset/check_inlier_ratio/AMI/"
    # mats_path = "../dataset/check_inlier_ratio/Satellite/"
    # mats_path = "../dataset/check_inlier_ratio/SUAV1/"
    # mats_path = "../dataset/RS_inlier_ratio_change/RS_0535/"
    mats_path = "../dataset/robust_change_ratio/iter_1/ratio_0.9/"
    mats_list = os.listdir(mats_path)
    true_match_ratio_list = check_inlier_ratio(mats_path, ["3008.mat"])
    print(true_match_ratio_list.reshape(-1, 1))
