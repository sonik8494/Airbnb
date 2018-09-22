# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 18:23:38 2018

@author: 15p001tx
"""
import os
import pandas as pd
import numpy as np
os.chdir('C:\\Users\\15p001tx\\Desktop\\New folder')
df = pd.read_csv('dc_airbnb.csv')
df1 = df.copy()
our_accom = 3
df1['distance'] = abs(df1['accommodates'] - 3) #abs(df1['accommodates'] - 3)
#cleaning the data
df1['price'] = df1['price'].str.replace(',','')
df1['price'] = df1['price'].str.replace('$','')
df1['price'] = df1['price'].astype(float)
#selecting the data
dist = df1[df1['distance'] == 0]
dist['price'].mean()



def people(n,k,feature):
    np.random.seed(53)
    df_new = pd.read_csv('dc_airbnb.csv')
    df_new = df_new.loc[np.random.permutation(len(df_new))]
    df_new['price'] = df_new['price'].str.replace(',','')
    df_new['price'] = df_new['price'].str.replace('$','')
    df_new['price'] = df_new['price'].astype(float)
    df_new['dist'] = df_new[feature] - n
    df_new = df_new[df_new['dist'] == 0]
    return df_new['price'].head(k).mean()