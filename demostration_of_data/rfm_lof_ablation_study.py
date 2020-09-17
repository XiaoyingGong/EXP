# author: 龚潇颖(Xiaoying Gong)
# date： 2020/8/21 21:01  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#sns.set_style('darkgrid',{'font.sans-seif':['SimHei','Arial']})

import warnings
warnings.filterwarnings('ignore')

sns.set()
a=np.arange(30).reshape(10, 3)
df=pd.DataFrame(a,columns=['s_1','category', 'strategy'])
df['s_1'] = [0.30123, 0.999785, 0.45552, 0.343265, 0.9556, 0.49461, 0.911125, 0.95535, 0.93205, 1.2]
df['strategy'] = ['strategy1', 'strategy1', 'strategy1', 'strategy2', 'strategy2', 'strategy2', 'strategy3', 'strategy3', 'strategy3', 'strategy3']
df['category'] = ['precision', 'recall', 'f1', 'precision', 'recall', 'f1', 'precision', 'recall', 'f1', 'x']
print(df)
# df['a']=[0,4,4,8,8,8,4,12,12,12]
# df['d']=list('aabbabbbab')
sns.barplot(x='category',y='s_1',data=df, hue="strategy", palette=sns.color_palette('colorblind',8))
plt.show()