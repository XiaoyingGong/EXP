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

def change_inlier_ratio(src_path, read_path, number_list, required_inlier_ratio_list, mat_list, category_words):
    for i in range(len(number_list)):
        save_path = src_path + category_words + str(number_list[i]) + "/"
        for j in range(len(mat_list)):
            print("在%s的inlier率下，处理%d号mat"%(required_inlier_ratio_list[i], mat_list[j]))
            # print(mat_list[j])
            save_mat_path = save_path + str(mat_list[j]) + ".mat"
            read_mat_path = read_path + str(mat_list[j]) + ".mat"
            print(read_mat_path)
            read_mat = io.loadmat(read_mat_path)

            ground_truth = read_mat["ground_truth"].flatten()
            img_x = read_mat["img_x"]
            img_y = read_mat["img_y"]
            # reOrderIdx = read_mat["reOrderIdx"]
            # seed_idx = read_mat["seed_idx"]
            X = read_mat["X"]
            Y = read_mat["Y"]

            false_match = np.argwhere(ground_truth == 0).flatten()
            false_match_num = len(false_match)
            true_match = np.argwhere(ground_truth == 1).flatten()
            true_match_num = len(true_match)
            total_num = len(ground_truth)
            inlier_ratio = true_match_num / total_num
            required_inlier_ratio = required_inlier_ratio_list[i]

            X_d1_MAX = np.max(X[:, 0])
            X_d1_MIN = np.min(X[:, 0])
            X_d2_MAX = np.max(X[:, 1])
            X_d2_MIN = np.min(X[:, 1])

            Y_d1_MAX = np.max(Y[:, 0])
            Y_d1_MIN = np.min(Y[:, 0])
            Y_d2_MAX = np.max(Y[:, 1])
            Y_d2_MIN = np.min(Y[:, 1])
            # 高于inlier_ratio的要求 随机增加false matches
            if inlier_ratio > required_inlier_ratio:
                print("add_False:", mat_list[j])
                # 增加的false match数量
                add_false_match_num = int(np.floor((true_match_num / required_inlier_ratio) - total_num))
                add_false_match = []
                # 开始随机增加false matches
                k = 0
                tree_Y = KDTree(Y)
                tree_X = KDTree(X)
                while True:
                    match_X, match_Y = create_random_matches(X_d1_MAX, X_d1_MIN, X_d2_MAX, X_d2_MIN,\
                                          Y_d1_MAX, Y_d1_MIN, Y_d2_MAX, Y_d2_MIN)
                    if is_a_potential_true_match.is_add(match_Y, match_X, tree_Y, tree_X, 5, 0.4):
                        X = np.vstack((X, match_X))
                        Y = np.vstack((Y, match_Y))
                        ground_truth = np.hstack((ground_truth, [0]))
                        k += 1
                    else:
                        continue
                    if k >= add_false_match_num:
                        break
            else:
                print("remove_False:", mat_list[j])
            # 低于inlier_ratio的要求 随机去掉false matches
                # 去掉的数量
                remove_false_match_num = int(np.floor(total_num - (true_match_num / required_inlier_ratio)))
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
            io.savemat(save_mat_path, {'ground_truth': ground_truth.reshape([-1, 1]), 'img_x': img_x, 'img_y': img_y, 'X': X, 'Y': Y})


# 使用均匀分布产生outleir
def change_inlier_ratio_2(src_path, read_path, number_list, required_inlier_ratio_list, mat_list, category_words):
    for i in range(len(number_list)):
        save_path = src_path + category_words + str(number_list[i]) + "/"
        for j in range(len(mat_list)):
            print("在%s的inlier率下，处理%d号mat"%(required_inlier_ratio_list[i], mat_list[j]))
            # print(mat_list[j])
            save_mat_path = save_path + str(mat_list[j]) + ".mat"
            read_mat_path = read_path + str(mat_list[j]) + ".mat"
            read_mat = io.loadmat(read_mat_path)

            ground_truth = read_mat["ground_truth"].flatten()
            img_x = read_mat["img_x"]
            img_y = read_mat["img_y"]
            reOrderIdx = read_mat["reOrderIdx"]
            seed_idx = read_mat["seed_idx"]
            X = read_mat["X"]
            Y = read_mat["Y"]

            false_match = np.argwhere(ground_truth == 0).flatten()
            false_match_num = len(false_match)
            true_match = np.argwhere(ground_truth == 1).flatten()
            true_match_num = len(true_match)
            total_num = len(ground_truth)
            inlier_ratio = true_match_num / total_num
            required_inlier_ratio = required_inlier_ratio_list[i]

            X_d1_MAX = np.max(X[:, 0])
            X_d1_MIN = np.min(X[:, 0])
            X_d2_MAX = np.max(X[:, 1])
            X_d2_MIN = np.min(X[:, 1])

            Y_d1_MAX = np.max(Y[:, 0])
            Y_d1_MIN = np.min(Y[:, 0])
            Y_d2_MAX = np.max(Y[:, 1])
            Y_d2_MIN = np.min(Y[:, 1])
            # 高于inlier_ratio的要求 随机增加false matches
            if inlier_ratio > required_inlier_ratio:
                print("add_False:", mat_list[j])
                # 增加的false match数量
                print(required_inlier_ratio)
                add_false_match_num = int(np.floor((true_match_num / required_inlier_ratio) - total_num))
                add_false_match = []
                # 开始随机增加false matches
                k = 0
                tree_Y = KDTree(Y)
                tree_X = KDTree(X)
                while True:
                    match_X, match_Y = create_random_matches(X_d1_MAX, X_d1_MIN, X_d2_MAX, X_d2_MIN,\
                                          Y_d1_MAX, Y_d1_MIN, Y_d2_MAX, Y_d2_MIN)
                    if is_a_potential_true_match.is_add(match_Y, match_X, tree_Y, tree_X, 10, 0.4):
                        X = np.vstack((X, match_X))
                        Y = np.vstack((Y, match_Y))
                        ground_truth = np.hstack((ground_truth, [0]))
                        k += 1
                    else:
                        continue
                    if k >= add_false_match_num:
                        break
            else:
                print("remove_False:", mat_list[j])
            # 低于inlier_ratio的要求 随机去掉false matches
                # 去掉的数量
                remove_false_match_num = int(np.floor(total_num - (true_match_num / required_inlier_ratio)))
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
            io.savemat(save_mat_path, {'ground_truth': ground_truth.reshape([-1, 1]), 'img_x': img_x, 'img_y': img_y, 'X': X, 'Y': Y})


def main_1():
    src_path = "../dataset/RS_inlier_ratio_change/"
    read_path = "../dataset/chen_mixture_dataset/"
    # number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # required_inlier_ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    # mat_list = np.linspace(3001, 3020, 20, dtype=int)

    #number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # required_inlier_ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    number_list = ['0535']
    required_inlier_ratio_list = [0.535]
    mat_list = [5006]#np.linspace(3001, 3020, 20, dtype=int)

    category_words = 'RS_'
    change_inlier_ratio(src_path, read_path, number_list, required_inlier_ratio_list, mat_list,
                                            category_words)

def main_2():
    src_path = "../dataset/FIRE/"
    read_path = "../dataset/RS_inlier_ratio_change/SUAV1/"
    # number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    number_list = ['05']
    required_inlier_ratio_list = [0.5]
    # required_inlier_ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    mat_list = np.linspace(5011, 5020, 10, dtype=int)
    mat_list = [5010]
    category_words = 'add_outlier_'
    change_inlier_ratio(src_path, read_path, number_list, required_inlier_ratio_list, mat_list,
                        category_words)


def main_3():
    src_path = "../dataset/RS_inlier_ratio_change_3/"
    read_path = "../dataset/RS_inlier_ratio_change_3/RS_08/"
    # number_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    # required_inlier_ratio_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    number_list = ['09']
    required_inlier_ratio_list = [0.9]
    mat_list = [3004]
    category_words = 'RS_'
    change_inlier_ratio(src_path, read_path, number_list, required_inlier_ratio_list, mat_list,
                                            category_words)
    return


if __name__ == '__main__':
    main_1()



