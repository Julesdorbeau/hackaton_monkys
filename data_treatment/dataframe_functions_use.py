# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:33:11 2021

@author: Jules
"""

import pandas as pd

def region_selection(df, region_choice):
    return df.loc[df['region'] == region_choice]

df = pd.read_csv("generated_dataframe.csv")
pd.set_option('display.max_columns', None)

print("========== DATAFRAME SANS MODIFICATIONS ==========")
print(df.head())
print()


print("========== BRETAGNE REGION SELECTION ===========")
df_bretagne = region_selection(df, 'BRETAGNE')
print(df_bretagne.head())
print()
print("========== IDF REGION SELECTION ==========")
df_idf = region_selection(df, 'ILE DE FRANCE')
print(df_idf.head())
print()
print("========== RACA REGION SELECTION ==========")
df_raca = region_selection(df, 'RHONE ALPES COTES D_AZUR')
print(df_raca.head())
print()

