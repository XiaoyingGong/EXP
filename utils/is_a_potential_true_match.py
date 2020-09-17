# author: 龚潇颖(Xiaoying Gong)
# date： 2020/7/6 17:11  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
from sklearn.neighbors import KDTree
import numpy as np

def is_add(cur_Y, cur_X, tree_Y, tree_X, neighbors_num, ratio):

    dist_y, ind_y = tree_Y.query(cur_Y, k=neighbors_num)
    dist_x, ind_x = tree_X.query(cur_X, k=neighbors_num)
    dist_y, dist_x, ind_y, ind_x = dist_y.flatten(), dist_x.flatten(), ind_y.flatten(), ind_x.flatten()

    corr_num = len(list(set(ind_x) & set(ind_y)))
    cur_ratio = corr_num / neighbors_num

    return True if cur_ratio <= ratio else False
