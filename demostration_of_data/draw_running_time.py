# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/13 15:51  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

running_time_list = [0.01994943618774414, 0.049834251403808594, 0.08980679512023926, 0.15657448768615723, 0.23778939247131348, 0.33144354820251465,\
                     0.42589855194091797, 0.5365569591522217, 0.6493370532989502, 0.7814886569976807, 0.9324936866760254, 1.0977721214294434, \
                     1.2791862487792969, 1.4665658473968506, 1.6747345924377441, 1.9041321277618408, 2.1398794651031494, 2.405921220779419, \
                     2.6955530643463135, 3.013035297393799, 3.3237109184265137, 3.7171852588653564, 4.001194477081299, 4.32368540763855, \
                     4.726067304611206, 5.059404611587524, 5.514103651046753, 5.877182722091675, 6.2847418785095215, 6.721677303314209]

x = np.linspace(100, 3000, 30, dtype=int)
x_new = np.hstack((x, np.linspace(100, 3000, 300, dtype=int)))
plt.figure()
fig = plt.gcf()
axes = plt.axes()
axes.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000])

f2 = interp1d(x, running_time_list, kind='cubic')
# xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max
# power_smooth = spline(T,power,xnew)
plt.plot(x, running_time_list)
# plt.plot(x_new, f2(x_new))
# print(x_new)
plt.xlabel("number of pre-matches")
plt.ylabel("time cost (s)")
plt.scatter(x, running_time_list)

fig.savefig("../dataset/" + 'runtime', bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
fig.savefig("../dataset/" + 'runtime' + '.svg', bbox_inches='tight', dpi=fig.dpi, pad_inches=0.0)
plt.show()