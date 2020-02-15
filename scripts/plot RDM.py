#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:19:44 2020

@author: nmei
"""

import os
from glob import glob
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors
from scipy.spatial import distance
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_context('poster')

working_dir = '../data'
working_data = glob(os.path.join(working_dir,'*.csv'))
working_models = glob(os.path.join(working_dir,'*.gz'))

df = pd.concat([pd.read_csv(f,sep = ';',encoding='latin-1') for f in working_data])
df['es'] = df['Spanish']
df['eu'] = df['Basque']
df['en'] = df['English']
for model in working_models[:-2]:
    language = model.split('.')[2]
    model_loaded = KeyedVectors.load_word2vec_format(model,
                                                     encoding = 'latin-1',
                                                     binary = True,)
    words = df[language].values
