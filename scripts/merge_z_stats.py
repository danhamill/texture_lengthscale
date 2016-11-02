# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:23:42 2016

@author: dan
"""

import pandas as pd
from glob import glob
import os
import numpy as np

files = glob(r"C:\workspace\texture_lengthscale\output\*zonalstats*.csv")

file_04 = files[0]
file_09 = files[1]
file_09_2 = files[2]


df1 = pd.read_csv(file_04, sep=',')
df2 = pd.read_csv(file_09, sep=',')
df3 = pd.read_csv(file_09_2, sep=',')
merge = pd.concat([df1,df2,df3])   
merge['Variance'] = merge['std']**2
del df1,df2, df3

pvt_tbl = pd.pivot_table(merge, index=['substrate'], values=['Variance','mean'],aggfunc=np.average) 
pvt_tbl['CV'] = np.sqrt(pvt_tbl['Variance'])/pvt_tbl['mean']

oName = r"C:\workspace\texture_lengthscale\output" + os.sep + "texture_lentghtscale_zonal_stats_merged.csv"

merge.to_csv(oName, sep=',', index=False)
