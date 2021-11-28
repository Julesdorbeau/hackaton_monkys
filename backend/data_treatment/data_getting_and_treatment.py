# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:48:13 2021

@author: Jules
"""

import pandas as pd
import random
from random import randint

def producteur_csv_generation() :
    generation_df = pd.DataFrame([], columns= ['names','phone','adress','website','region','coords_gps'])
    
    websites_randoms = ["a-la-ferme.fr", "le-verger.fr", "pisciculture.fr", "les-pecheurs-locaux.fr",
                        "aux-bios-vignobles.fr", "aux-elevages-naturels.fr"]
    names_randoms = ["FERME", "VERGER", "PISCICULTURE", "PECHEURS", "VIGNOBLES", "ELEVAGES"]
    adress_randoms = ["23 boulevard des bons coins", "14 rue du bon fermier", "17 Avenue du Général De Gaulle",
                      "1 Boulevard Victor Hugo", "60 rue de la Bretagne", "28 Avenue de la libération"]
    phone_randoms = ["01.01.01.01.01", "02.02.02.02.02", "03.03.03.03.03", "04.04.04.04.04",
                     "05.05.05.05.05", "06.06.06.06.06", "07.07.07.07.07"]
    regions_random = ["BRETAGNE", "ILE DE FRANCE", "RHONE ALPES COTES D_AZUR"]
    coords_gps_random = ["48.11682532474373 -1.681704216503892", "48.85739082646763 2.341206930273465",
                         "43.30346343968935 5.370686910742215"]

    website_names_random_len = len(names_randoms)
    adress_random_len = len(adress_randoms)
    phone_random_len = len(phone_randoms)
    coors_regions_random = len(regions_random)

    for i in range (0, 200) : 
        value_website_names = randint(0, website_names_random_len-1)
        value_adress = randint(0, adress_random_len-1)
        value_phone = randint(0, phone_random_len-1)
        value_coors_regions = randint(0, coors_regions_random-1)
        data = {'names': names_randoms[value_website_names],
                'phone': phone_randoms[value_phone],
                'adress': adress_randoms[value_adress],
                'website': websites_randoms[value_website_names],
                'region': regions_random[value_coors_regions],
                'coords_gps': coords_gps_random[value_coors_regions]
                }
        
        generation_df = generation_df.append(data, ignore_index=True)

    generation_df.drop_duplicates(keep=False)
    generation_df.to_csv('generated_dataframe.csv')
    """""""""
if __name__ == '__main__':
    producteur_csv_generation()
"""""""""