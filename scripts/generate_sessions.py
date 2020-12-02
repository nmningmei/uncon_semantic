#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:02:54 2020

@author: nmei
"""

import os
import pandas as pd

df = pd.read_csv('../data/sampled_words.csv',encoding = 'latin-1')

csv_dir = '../experiment_csvs'
if not os.path.exists(csv_dir):
    os.mkdir(csv_dir)

n_days = 6
n_sessions_per_day = 8
n_half = int(df.shape[0] / 4)

count = 1
for day in range(n_days):
    for session in range(n_sessions_per_day):
        df_temp = df.copy().sample(frac = 1., replace = False,)
        
        animal = df_temp[df_temp['Category'] == 'animal']
        tool = df_temp[df_temp['Category'] == 'object']
        
        df_first = pd.concat([animal.iloc[:n_half,:],tool.iloc[:n_half,:]]).sample(frac = 1., replace = False)
        df_second = pd.concat([animal.iloc[n_half:,:],tool.iloc[n_half:,:]]).sample(frac = 1., replace = False)
        
        df_first.to_csv(os.path.join(csv_dir,f'session_{count}.csv'),index = False)
        count += 1
        df_second.to_csv(os.path.join(csv_dir,f'session_{count}.csv'),index = False)
        count += 1