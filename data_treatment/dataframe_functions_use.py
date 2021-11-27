# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:33:11 2021

@author: Jules
"""

import pandas as pd

df = pd.read_csv("generated_dataframe.csv")
pd.set_option('display.max_columns', None)

df = df.loc[df['region'] == 'BRETAGNE']

print(df.head())
