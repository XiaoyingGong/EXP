# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/12 9:45  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
import numpy as np
from utils.excel_reader import ExcelOperation

excel_operation = ExcelOperation("E:/xx学习/第三篇论文/method_2/实验/GXY_RS_EXP.xlsx")
# RS_part_1 Satellite
# RS_part_2 SUAV
# mixture_dataset AMI
category = 'RS_part_1'
sheet = excel_operation.get_sheet("RS_part_1")

true_match_ratio_list = []
# 2, 22
# 2, 12
for i in range(2, 22):
    true_match_ratio = sheet.row_values(i)[25]
    true_match_ratio_list.append(true_match_ratio)

true_match_ratio_list = np.array(true_match_ratio_list)
true_match_ratio_list = np.sort(true_match_ratio_list)
print(true_match_ratio_list)


idx = np.linspace(1, len(true_match_ratio_list), len(true_match_ratio_list), dtype=int)
idx = idx / len(true_match_ratio_list)


plt.figure()
fig = plt.gcf()
axes = plt.axes()
axes.set_xlim([0, 1.01])
axes.set_ylim([0, 1.01])
axes.set_xticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9, 1.0])

plt.xlabel("cumulative distribution")
plt.ylabel("true match ratio")
# plt.axis("equal")
scatter_list = []

average_true_match_ratio = np.average(true_match_ratio_list)

average_true_match_ratio = float(("%.4f"%average_true_match_ratio)) * 100
plt.scatter(idx, true_match_ratio_list, c='white', edgecolors='red',
            label="average true match ratio %.2f %%"%average_true_match_ratio)
plt.legend(loc='upper left', fontsize=12)

for i in range(len(idx) - 1):
    plt.plot([idx[i], idx[i+1]], [true_match_ratio_list[i], true_match_ratio_list[i+1]], c='red')
fig.savefig("../results/cumulative/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../results/cumulative/" + category + '.svg')
# plt.show()
plt.show()
print(idx)

