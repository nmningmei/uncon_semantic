#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:19:44 2020

@author: nmei
"""

import os
from glob import glob
import pandas as pd
import numpy as np
from scipy.spatial import distance
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_context('talk')
from gensim.models.keyedvectors import KeyedVectors # for loading word2vec models

working_dir = '../data'
working_data = glob(os.path.join(working_dir,'*.csv'))
working_models = glob(os.path.join(working_dir,'*.gz'))

df = pd.concat([pd.read_csv(f,sep = ';',encoding='latin-1') for f in working_data])
df = df.drop_duplicates('English')
df['en'] = df['English']
df['es'] = df['Spanish']
df['eu'] = df['Basque']
df_hi = df[df['Conc'] == 'Hi']

for model in working_models:
    language = model.split('.')[3]
    words = df_hi[language].values
    if not os.path.exists('../figures/{}_high_concrete_words.jpeg'.format(language)):
        model_loaded = KeyedVectors.load_word2vec_format(model)
        word2vecs = np.array([model_loaded[word] for word in words])
        df_lan = pd.DataFrame(word2vecs.T,columns = words)
        df_lan.to_csv('../results/{}_high_concrete_words.csv'.format(language),index = False,encoding='latin-1')
        RDM = distance.squareform(distance.pdist(word2vecs - word2vecs.mean(1).reshape(-1,1),'cosine'))
        np.fill_diagonal(RDM,np.nan)
        dissimilarity = pd.DataFrame(RDM,columns=words)
        dissimilarity.index = words
        fig,ax = plt.subplots(figsize = (22,20))
        
        ax = sns.heatmap(dissimilarity,
                        xticklabels = True,
                        yticklabels = True,
                        ax = ax,
                        cmap = plt.cm.coolwarm,)
        _ = ax.set(title = '{}, Red = dissimilar, Blue = similar'.format(language))
        ax.axhline(round(dissimilarity.shape[0] / 2.),linestyle = '--', color = 'black', alpha = 1.)
        ax.axvline(round(dissimilarity.shape[0] / 2.),linestyle = '--', color = 'black', alpha = 1.)
        fig.savefig('../figures/{}_high_concrete_words.jpeg'.format(language),dpi = 350,bbox_inches = 'tight')
    words = df[language].values
    if not os.path.exists('../figures/{}_all_words.jpeg'.format(language)):
        word2vecs = np.array([model_loaded[word] for word in words])
        df_lan = pd.DataFrame(word2vecs.T,columns = words)
        df_lan.to_csv('../results/{}_all_words.csv'.format(language),index = False,encoding='latin-1')
        RDM = distance.squareform(distance.pdist(word2vecs - word2vecs.mean(1).reshape(-1,1),'cosine'))
        np.fill_diagonal(RDM,np.nan)
        dissimilarity = pd.DataFrame(RDM,columns=words)
        dissimilarity.index = words
        fig,ax = plt.subplots(figsize = (22,20))
        
        ax = sns.heatmap(dissimilarity,
                        xticklabels = True,
                        yticklabels = True,
                        ax = ax,
                        cmap = plt.cm.coolwarm,)
        _ = ax.set(title = '{}, Red = dissimilar, Blue = similar'.format(language))
        ax.axhline(round(dissimilarity.shape[0] / 2.),linestyle = '--', color = 'black', alpha = 1.)
        ax.axvline(round(dissimilarity.shape[0] / 2.),linestyle = '--', color = 'black', alpha = 1.)
        fig.savefig('../figures/{}_all_words.jpeg'.format(language),dpi = 350,bbox_inches = 'tight')
