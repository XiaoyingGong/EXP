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
excel_operation = ExcelOperation("E:/xx学习/第三篇论文/method_2/实验/GXY_RS_EXP.xlsx")
# RS_part_1 Satellite
# RS_part_2 SUAV
# mixture_dataset AMI
category = 'AMI'
sheet = excel_operation.get_sheet("AMI")

p = []
r = []
# 2, 22
# 2, 12
for i in range(2, 12):
    p_row = sheet.row_values(i)[1:7]
    p_row.reverse()
    p.append(p_row)
    r_row = sheet.row_values(i)[10:16]
    r_row.reverse()
    r.append(r_row)
p = np.array(p).T
print(p.shape)
r = np.array(r).T
print(p)
colors = ['black', 'green', 'blue', 'm', 'gold', 'red']
markers = ['.', 'x', '+', '1', 'v', '^']
method_list = ["RANSAC", "RFM-SCAN", "GS", "ICF", "LPM", "OURS"]

plt.figure()
fig = plt.gcf()
axes = plt.axes()
axes.set_xlim([0, 1.01])
axes.set_ylim([0, 1.01])
axes.set_xticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9, 1.0])

plt.xlabel("precision")
plt.ylabel("recall")
# plt.axis("equal")
scatter_list = []
for i in range(len(p)):
    s = plt.scatter(p[i], r[i], c=colors[i], marker=markers[i], label=method_list[i])
    scatter_list.append(s)
    plt.legend(loc='lower left', fontsize=12)

fig.savefig("../results/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../results/" + category + '.svg')
plt.show()
