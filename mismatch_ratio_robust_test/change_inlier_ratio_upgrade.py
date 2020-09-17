# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/13 19:08  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np
import scipy.io as io
import random
from utils import is_a_potential_true_match
from sklearn.neighbors import KDTree

def create_random_matches(X_d1_max, X_d1_min, X_d2_max, X_d2_min, Y_d1_max, Y_d1_min, Y_d2_max, Y_d2_min):
    created_X = np.array([[np.random.randint(X_d1_min, X_d1_max), np.random.randint(X_d2_min, X_d2_max)]])
    created_Y = np.array([[np.random.randint(Y_d1_min, Y_d1_max), np.random.randint(Y_d2_min, Y_d2_max)]])
    return created_X, created_Y


def change_inlier_ratio(mat, save_path, required_ratio):
    ground_truth = mat["ground_truth"].flatten()
    img_x = mat["img_x"]
    img_y = mat["img_y"]
    X = mat["X"]
    Y = mat["Y"]


    false_match = np.argwhere(ground_truth == 0).flatten()
    false_match_num = len(false_match)
    true_match = np.argwhere(ground_truth == 1).flatten()
    true_match_num = len(true_match)
    total_num = len(ground_truth)
    cur_inlier_ratio = true_match_num / total_num

    X_d1_MAX = np.max(X[:, 0])
    X_d1_MIN = np.min(X[:, 0])
    X_d2_MAX = np.max(X[:, 1])
    X_d2_MIN = np.min(X[:, 1])

    Y_d1_MAX = np.max(Y[:, 0])
    Y_d1_MIN = np.min(Y[:, 0])
    Y_d2_MAX = np.max(Y[:, 1])
    Y_d2_MIN = np.min(Y[:, 1])

    # 高于inlier_ratio的要求 随机增加false matches
    if cur_inlier_ratio > required_ratio:
        # 增加的false match数量
        add_false_match_num = int(np.floor((true_match_num / required_ratio) - total_num))
        add_false_match = []
        # 开始随机增加false matches
        for i in range(add_false_match_num):
            match_X, match_Y = create_random_matches(X_d1_MAX, X_d1_MIN, X_d2_MAX, X_d2_MIN,\
                                  Y_d1_MAX, Y_d1_MIN, Y_d2_MAX, Y_d2_MIN)
            X = np.vstack((X, match_X))
            Y = np.vstack((Y, match_Y))
            ground_truth = np.hstack((ground_truth, [0]))
    else:
    # 低于inlier_ratio的要求 随机去掉false matches
        # 去掉的数量
        remove_false_match_num = int(np.floor(total_num - (true_match_num / required_ratio)))
        # 保存的数量
        reserve_false_match_num = false_match_num - remove_false_match_num
        # 产生保存的ground_truth的index
        reserve_list = np.array(random.sample(range(0, reserve_false_match_num), reserve_false_match_num))
        false_match_reserved = false_match[reserve_list]
        reserved_match = np.hstack((true_match, false_match_reserved))
        #
        ground_truth = ground_truth[reserved_match]
        X = X[reserved_match]
        Y = Y[reserved_match]
    # 存储
    io.savemat(save_path, {'ground_truth': ground_truth.reshape([-1, 1]), 'img_x': img_x, 'img_y': img_y, 'X': X, 'Y': Y})


if __name__ == '__main__':
    mat_name_list = ["3008"]
    save_path_ori = "../dataset/robust_change_ratio"
    iter_idx = 1
    iter_required = 1
    ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    # ratio_list = [0.9]
    for mat_name in mat_name_list:
        for ratio in ratio_list:
            while True:
                mat = io.loadmat("../dataset/check_inlier_ratio/SUAV1/" + mat_name + ".mat")
                save_path = save_path_ori + "/" + "iter_" + str(iter_idx) + "/" + "ratio_" + str(ratio) + "/" + mat_name + ".mat"
                change_inlier_ratio(mat, save_path, ratio)
                if iter_idx >= iter_required:
                    break
                else:
                    iter_idx += 1

