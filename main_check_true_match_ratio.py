# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/7 10:53  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np
import os
from utils import check_inlier_ratio
# mats_path = "./dataset/RS_inlier_ratio_change/"
# dic_list = ['RS_01', 'RS_02', 'RS_03', 'RS_04', 'RS_05', 'RS_06', 'RS_07', 'RS_08', 'RS_09']
#
# for dic in dic_list:
#     print(dic)
#     cur_mats_path = mats_path + dic + "/"
#     print(cur_mats_path)
#     mats_list = os.listdir(cur_mats_path)
#     check_inlier_ratio.check_inlier_ratio(cur_mats_path, mats_list)


cur_mats_path = "./dataset/chen_mixture_dataset/"
mats_list = os.listdir(cur_mats_path)

inlier_ratio = check_inlier_ratio.check_inlier_ratio(cur_mats_path, mats_list)
print("平均inlier率为:", np.mean(inlier_ratio))


