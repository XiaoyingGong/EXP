# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/13 20:22  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
from utils.excel_reader import ExcelOperation
import numpy as np

# 分别是 RANSAC RFM-SCAN GS ICF LPM OURS
excel_operation = ExcelOperation("../dataset/ROBUST_913_FINAL.xlsx")
X = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
sheet_name_list = ["RS_01", "RS_02", "RS_03", "RS_04", "RS_05", "RS_06", "RS_07", "RS_08", "RS_09"]

p = []
r = []
f1 = []

colors = ['black', 'green', 'blue','m', 'gold', 'red']
markers = ['.', 'x', '+', '1', 'v', '^']
method_list = ["RANSAC", "RFM-SCAN", "GS", "ICF", "LPM", "OURS"]

for sheet_name in sheet_name_list:
    sheet = excel_operation.get_sheet(sheet_name)

    # 2, 22
    # 2, 12 19:24
    i = 2
    p_row = sheet.row_values(i)[1:7]
    p_row.reverse()
    p.append(p_row)
    r_row = sheet.row_values(i)[10:16]
    r_row.reverse()
    r.append(r_row)
    f1_row = sheet.row_values(i)[19:25]
    f1_row.reverse()
    f1.append(f1_row)

p = np.array(p)
r = np.array(r)
f1 = np.array(f1)
print(f1)

# precision曲线
plt.figure("precision")
fig = plt.gcf()
plt.xlabel("true match ratio")
plt.ylabel("precision")
# 确定哪个方法
for j in range(len(method_list)):
    plt.scatter(X, p[:, j], c=colors[j],  marker=markers[j], label=method_list[j])
    plt.plot(X, p[:, j], c=colors[j])

plt.legend(loc='lower right', fontsize=12)
category = 'p'
fig.savefig("../dataset/robust_result/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../dataset/robust_result/" + category + '.svg', bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)


# recall曲线
plt.figure("recall")
fig = plt.gcf()
plt.xlabel("true match ratio")
plt.ylabel("recall")
# 确定哪个方法
for j in range(len(method_list)):
    plt.scatter(X, r[:, j], c=colors[j],  marker=markers[j], label=method_list[j])
    plt.plot(X, r[:, j], c=colors[j])

plt.legend(loc='lower right', fontsize=12)
category = 'r'
fig.savefig("../dataset/robust_result/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../dataset/robust_result/" + category + '.svg', bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)

# f1曲线
plt.figure("f1")
fig = plt.gcf()
plt.xlabel("true match ratio")
plt.ylabel("f1-score")
# 确定哪个方法
for j in range(len(method_list)):
    plt.scatter(X, f1[:, j], c=colors[j],  marker=markers[j], label=method_list[j])
    plt.plot(X, f1[:, j], c=colors[j])

plt.legend(loc='lower right', fontsize=12)

category = 'f1'
fig.savefig("../dataset/robust_result/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../dataset/robust_result/" + category + '.svg', bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)

plt.show()


# plt.figure()
# fig = plt.gcf()
# axes = plt.axes()
# axes.set_xlim([0, 1.01])
# axes.set_ylim([0, 1.01])
# axes.set_xticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9,1.0])
# axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9, 1.0])
#
# plt.xlabel("precision")
# plt.ylabel("recall")
# # plt.axis("equal")
# scatter_list = []
# for i in range(len(p)):
#     s = plt.scatter(p[i], r[i], c=colors[i], marker=markers[i], label=method_list[i])
#     scatter_list.append(s)
#     plt.legend(loc='lower left', fontsize=12)
#
# fig.savefig("../results/" + category, bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
# fig.savefig("../results/" + category + '.svg')
# plt.show()