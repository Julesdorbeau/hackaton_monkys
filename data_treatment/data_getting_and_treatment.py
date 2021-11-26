# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:48:13 2021

@author: Jules
"""

import pandas as pd 

df = pd.read_csv("../data/cotes_d_amor_producteurs.csv")

df.columns = ['names','phone','adress','website']

pd.set_option('display.max_columns', None)


print(df.head())