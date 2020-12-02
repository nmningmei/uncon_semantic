#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:27:15 2020

@author: nmei
"""

import os
from glob import glob
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeavePOut, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

df = pd.read_csv('../data/SEMGEN_Final_Stimuli.csv',sep = ';',encoding='latin-1')
df = df.drop_duplicates('English')
df['en'] = df['English']
df['es'] = df['Spanish']
df['eu'] = df['Basque']
df_hi = df[df['Conc'] == 'Hi']

working_dir = '../results'
working_data = glob(os.path.join(working_dir,'*all_words.csv'))

label_map = {'Living':0,'Nonliving':1}

for lan in ['en','es','eu']:
    f = [item for item in working_data if (f'{lan}_all_words' in item)][0]
    df_words = pd.read_csv(f,encoding='latin-1')
    word_vecs = np.array([df_words[word].values for word in df_hi[lan]])
    clf = make_pipeline(StandardScaler(),
                    LogisticRegression(C=1, solver='liblinear',
                                       multi_class='auto'))
    labels = np.array([label_map[item] for item in df_hi['Living']])
    cv = LeavePOut(p = 2)
    results = dict(
                    fold = [],
                    score = [],
                    test_word1 = [],
                    test_word2 = [],
                    )
    groups = df_hi[lan].values
    for fold, (idx_train,idx_test) in enumerate(cv.split(word_vecs,labels,groups = groups)): 
        X_train,y_train = word_vecs[idx_train],labels[idx_train]
        X_test,y_test = word_vecs[idx_test],labels[idx_test]
        X_train,y_train = shuffle(X_train,y_train)
        test_pairs = groups[idx_test]
        clf = make_pipeline(StandardScaler(),LogisticRegression(solver='liblinear',random_state=12345))
        clf.fit(X_train,y_train)
        preds = clf.predict_proba(X_test)[:,-1]
        score = np.abs(preds[0] - preds[1])
        results['fold'].append(fold + 1)
        results['score'].append(score)
        results['test_word1'].append(test_pairs[0])
        results['test_word2'].append(test_pairs[1])
    results_to_save = pd.DataFrame(results)
    
    idx_map = {word:idx for idx,word in enumerate(groups)}
    
    decode_distance = np.zeros((len(groups),len(groups)))
    for ii,row in results_to_save.iterrows():
        decode_distance[idx_map[row['test_word1']],
                        idx_map[row['test_word2']]] = row['score']
        decode_distance[idx_map[row['test_word2']],
                        idx_map[row['test_word1']]] = row['score']
    np.fill_diagonal(decode_distance,np.nan)
    
    decode_distance = pd.DataFrame(decode_distance,index = groups,columns=groups)
    
    fig,ax = plt.subplots(figsize = (14,14))
    ax = sns.heatmap(decode_distance,
                     xticklabels = True,
                     yticklabels = True,
                     ax = ax,
                     cmap = plt.cm.coolwarm,)
    _ = ax.set(title = 'Red = dissimilar, Blue = similar')
    ax.axhline(round(len(groups) / 2),linestyle = '--', color = 'black', alpha = 1.)
    ax.axvline(round(len(groups) / 2),linestyle = '--', color = 'black', alpha = 1.)
    fig.savefig('../figures/{}_high_concrete_words_decode_RMD.jpeg'.format(lan),dpi = 350,bbox_inches = 'tight')





















