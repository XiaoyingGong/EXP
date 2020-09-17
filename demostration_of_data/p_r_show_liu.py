# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/4 9:43  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
from utils.excel_reader import ExcelOperation
import numpy as np


# 分别是 RANSAC RFM-SCAN GS ICF LPM OURS
# excel_operation = ExcelOperation("G:\\PRAI\\Third-code\\EXP\\experiment_1-3.xlsx")
excel_operation = ExcelOperation("E:/xx学习/第三篇论文/method_2/实验/GXY_RS_EXP.xlsx")
sheet = excel_operation.get_sheet("exp_3")
# inlier_ratio = [0.601734489659773,0.465976331360947,0.398230088495575,0.334104938271605,0.396527777777778,\
#  0.509600000000000,0.261067708333333,0.245283018867925,0.467091295116773,0.475627769571640,\
#  0.517647058823530,0.505347593582888,0.273098519652884,0.257274119448698,0.115119363395225,\
#  0.112755102040816,0.0908090258668134,0.149577167019027,0.147633744855967,0.122244488977956]
p = []
r = []

for i in range(2, 22):
    p_row = sheet.row_values(i)[9:15]
    p_row.reverse()
    p.append(p_row)
    r_row = sheet.row_values(i)[1:7]
    # r_row = sheet.row_values(i)[10:16]
    r_row.reverse()
    r.append(r_row)

p = np.array(p).T
r = np.array(r).T
print(p)
colors = ['black', 'green', 'blue', 'm', 'gold', 'red']
markers = ['o', 'x', '+', '1', 'v', 'D' ]
method_list = ["RFM-SCAN", "LMR","LPM", "GS", "ICF", "OURS"]

plt.figure()
# plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
# plt.axis("equal")
plt.axis("equal")
plt.xlabel("precision")
plt.ylabel("recall")
# plt.axis("equal")
scatter_list = []
for i in range(len(p)):
    s = plt.scatter(p[i], r[i], c=colors[i], marker=markers[i], label=method_list[i])
    scatter_list.append(s)
    plt.legend(loc='lower left')
# plt.savefig('G:/PRAI/Third-code/EXP/exp_3/FIG/SUIRD_SC_RP.svg', dpi = 600)
plt.show()


