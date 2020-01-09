# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:05:13 2018

@author: higuchi takahiro
"""

import numpy as np
import matplotlib.pyplot as plt

data7 = np.loadtxt("Run 42.lvm",skiprows=22,encoding='SHIFT-JIS',dtype = None)

dy_data7 = np.gradient(data7)
dy_data7 = abs(dy_data7)

v = np.ones(3)/3.0 # 移動平均をとるための配列vを設定。今回は前後3つの値を用いて平均をとる。
huge7 = np.convolve(dy_data7,v, 'same') #移動平均

def min_max(x, axis=None): #正規化
     min = x.min(axis=axis, keepdims=True)
     max = x.max(axis=axis, keepdims=True)
     result = (x-min)/(max-min)
     return result

huge7 = min_max(huge7)
huge7_diff = (np.max(huge7) - np.min(huge7))*10/100

huge7_index = np.where(huge7 > huge7_diff)[0] #data6の移動平均(huge),indexの[0]番目のタプルを指定すれば返してくれる。
print(huge7_index)

diff7 = np.diff(huge7_index, n= 1) # huge_indexの差分、n=1から。
print (diff7)

diff7_index = np.argwhere(diff7 != 1) # 1以外の差分のインデックス
print (diff7_index) #14

huge7_index_min = np.min(huge7_index) #38
huge7_index_max = np.max(huge7_index) #164

diff_max = np.max(diff7_index) #14
diff_min = np.min(diff7_index)

hoge74 = huge7_index[diff_min] #傾きが終わるindex 56
hoge75 = huge7_index[diff_min+1]

hoge71 = huge7_index[diff_max] #傾きが終わるindex 56
hoge77 = huge7_index[diff_max+1]

data91 = data7[0:huge7_index_min-1].mean() #176.015454054054
data93 = data7[hoge74+1:hoge75-1].mean() #171.15863665806447
data96 = data7[huge7_index_max+1:].mean() #176.0167888888889

dataoff = (data91 + data96)/2

data = data93 - dataoff

plt.plot(huge7)