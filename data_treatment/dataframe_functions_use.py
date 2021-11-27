# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:33:11 2021

@author: Jules
"""

"""
SELCTION OF REGIONS FROM THE DATAFRAME GENERATED RANDOMLY

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
"""

import pandas as pd

def region_selection(df, region_choice):
    """
    Selection de tout les producteurs en fonction de la region
    """
    return df.loc[df['region'] == region_choice]

def ingredients_selection(df):
    """
    Selection d'uniquement tout les ingredients en dropant les duplicatats
    """
    return df.loc[:,"ingredient_name"].drop_duplicates()

def recipe_selection(ingredient_choice):
    """
    Return la liste des toutes les recettes contenants l'ingredient demande
    """
    df = pd.read_csv("../data/recipies_and_ingredients_data/ingredient.csv")
    tmp_df = df.loc[df['ingredient_name'] == ingredient_choice]
    tmp_df = tmp_df.loc[:,"recipe_title"]
    tmp_df = tmp_df.drop_duplicates()
    return tmp_df.values.tolist()

def get_empty_ingredient_dict():
    """
    Return un dictionnaire contenant la liste des ingredients et un coef a 0 pour chacun d'eux
    """
    df = pd.read_csv("../data/recipies_and_ingredients_data/ingredient_dict.csv")
    df = df.set_index(df.ingredient)
    res_dict = df.to_dict()
    # Taking only the coeficient dictionnary (the other one is only strings so not usable)
    return res_dict['coeficient']


df = pd.read_csv("../data/recipies_and_ingredients_data/ingredient.csv")
pd.set_option('display.max_columns', None)
#df = df.set_index(df.recipe_title)
#df = df[['ingredient_name','ingredient_category','max_qty','min_qty','unit','preparation']]

#print(get_empty_ingredient_dict())
#print(recipe_selection('sugar'))


# CONVERTION TO JSON 
# Pour save en fichier .json : js = df.to_json('json_test.json', orient = 'index')
js = df.to_json(orient = 'index')
print(js)


"""
print("========== DATAFRAME SANS MODIFICATIONS ==========")
print(df.head())
print()
"""

"""
Creating the dictionnary for the ingredients

ingredients_list = ingredients_selection(df)
ingredients_list = ingredients_list.drop_duplicates()

#print(ingredients_list.head())

ingr_list = ingredients_list.values.tolist()
coefs = [0] * len(ingr_list)

ingredients_dictionary = dict(zip(ingr_list, coefs))

#print(ingredients_dictionary)

df_dict = pd.DataFrame(ingredients_dictionary.items(), columns=['ingredient', 'coeficient'])
df_dict = df_dict.set_index(df_dict.ingredient)
df_dict = df_dict[['coeficient']]

#df_dict.to_csv('ingredient_dict.csv')

test_dict = df_dict.to_dict()
#print(test_dict)
"""