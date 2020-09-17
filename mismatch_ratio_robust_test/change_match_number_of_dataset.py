# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/13 15:16  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np

# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/5 20:18
# IDE：PyCharm
# des:此文件用于增加/降低RS数据集的true match率
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

# 别的不用管 只用管点的数量
def change_match_number(mat, save_path, required_number):
    ground_truth = mat["ground_truth"].flatten()
    img_x = mat["img_x"]
    img_y = mat["img_y"]
    X = mat["X"]
    Y = mat["Y"]

    cur_num = len(X)

    X_d1_MAX = np.max(X[:, 0])
    X_d1_MIN = np.min(X[:, 0])
    X_d2_MAX = np.max(X[:, 1])
    X_d2_MIN = np.min(X[:, 1])

    Y_d1_MAX = np.max(Y[:, 0])
    Y_d1_MIN = np.min(Y[:, 0])
    Y_d2_MAX = np.max(Y[:, 1])
    Y_d2_MIN = np.min(Y[:, 1])

    if cur_num < required_number:
        add_num = required_number - cur_num
        for j in range(add_num):
            match_X, match_Y = create_random_matches(X_d1_MAX, X_d1_MIN, X_d2_MAX, X_d2_MIN, \
                                                     Y_d1_MAX, Y_d1_MIN, Y_d2_MAX, Y_d2_MIN)
            X = np.vstack((X, match_X))
            Y = np.vstack((Y, match_Y))
            ground_truth = np.hstack((ground_truth, [0]))
    elif cur_num > required_number:
        reserve_idx = random.sample(range(0, cur_num), required_number)
        ground_truth = ground_truth[reserve_idx]
        X = X[reserve_idx]
        Y = Y[reserve_idx]
        # 存储
    io.savemat(save_path,
                   {'ground_truth': ground_truth.reshape([-1, 1]), 'img_x': img_x, 'img_y': img_y, 'X': X, 'Y': Y})

if __name__ == '__main__':
    mat = io.loadmat("../dataset/Satellite/1002.mat")
    print(len(mat["X"]))
    required_number_list = np.linspace(100, 3000, 30, dtype=int)
    print(required_number_list)
    save_path_ori = "../dataset/running_time_test/"
    for number in required_number_list:
        save_path = save_path_ori + "1002_" + str(number) + ".mat"
        change_match_number(mat, save_path, number)
