# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:15:09 2018

@author: higuchi takahiro
"""

import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("AVIO_IR_20180604_1904_1.csv",header=7)
dfy, dfx = np.gradient(data,.2,.2) #y方向,x方向の勾配

# 3Dグラフの初期化
fig = plt.figure()
ax = fig.gca(projection='3d')


#data = np.delete(data,0,0)
#data = np.delete(data,0,1)
# データの準備
Xgrid = data.columns.values.astype(np.float32)
Ygrid = data.index.values.astype(np.float32)
X, Y = np.meshgrid(Xgrid, Ygrid)
Z = data.as_matrix()

# プロット
surf = ax.plot_surface(X, Y, Z)

# 必要な場合はここでその他の設定をします。
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T')

# 表示
plt.show()

#参考文献　matplotlibでcsvから3dサーフェスグラフを作りたい