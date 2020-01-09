# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:36:37 2018

@author: higuchi takahiro
"""

import numpy as np
import matplotlib.pyplot as plt

# 描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.loadtxt("温度補正＿ｘ.lvm")
y = np.loadtxt("温度補正_ｙ.lvm")

plt.plot(x,y)
plt.show()