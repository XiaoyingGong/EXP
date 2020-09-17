# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/5 10:45  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
#绘制三角螺旋线

import matplotlib.pyplot as plt
import numpy as np
from utils.excel_reader import ExcelOperation
# 分别是 RANSAC RFM-SCAN GS ICF LPM OURS
excel_operation = ExcelOperation("E:\\xx学习\\第三篇论文\\method_2\\实验\\GXY_RS_EXP.xlsx")
sheet = excel_operation.get_sheet("RS_part_2")

inlier_ratio_1 = [0.601734489659773,0.465976331360947,0.398230088495575,0.334104938271605,0.396527777777778,\
 0.509600000000000,0.261067708333333,0.245283018867925,0.467091295116773,0.475627769571640,\
 0.517647058823530,0.505347593582888,0.273098519652884,0.257274119448698,0.115119363395225,\
 0.112755102040816,0.0908090258668134,0.149577167019027,0.147633744855967,0.122244488977956]

inlier_ratio_2 = [0.337899543378995,0.279951100244499,0.397897897897898,0.382559774964838,\
                  0.401774397972117,0.279181708784597,0.196019900497512,0.306165099268548,\
                  0.245033112582781,0.245098039215686,0.217717717717718,0.420871559633028,\
                  0.305627705627706,0.356564019448947,0.335279399499583,0.414876033057851,\
                  0.176045016077170,0.107679465776294,0.324324324324324,0.193869096934548]

inlier_ratio = inlier_ratio_1
p = []
r = []

for i in range(2, 22):
    p_row = sheet.row_values(i)[1:7]
    p_row.reverse()
    p.append(p_row)
    r_row = sheet.row_values(i)[10:16]
    r_row.reverse()
    r.append(r_row)

p = np.array(p).T
r = np.array(r).T

colors = ['black', 'green', 'blue', 'm', 'gold', 'red']
markers = ['.', 'x', '+', '1', 'v', '^']
method_list = ["RANSAC", "RFM-SCAN", "GS", "ICF", "LPM", "OURS"]

ax = plt.axes(projection='3d')

for i in range(len(p)):
    for j in range(len(p[i])):
        ax.scatter3D(p[i, j], r[i, j], inlier_ratio[j], c=colors[i], marker=markers[i])

plt.show()