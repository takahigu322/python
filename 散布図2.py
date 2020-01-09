# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:29:43 2019

@author: higuchi takahiro
"""

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
import seaborn as sns

#data = np.loadtxt('Book2.csv')
data = pd.read_csv('Book2.csv')
data.describe()

sns.pairplot(data)
#plt.rcParams["font.size"] = 16

plt.show()