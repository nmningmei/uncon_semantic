#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 17:25:11 2020

@author: nmei
"""

import os
from tqdm import tqdm
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeavePOut,cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn.base import clone

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_style('white')
#sns.set_context('talk')

label_map = {'animal':0,'object':1}

working_dir = '../results'
working_data = os.path.join(working_dir,'sampled_words.csv')
source_data = os.path.join('../data','Affective norms for 380 Spanish words belonging to three different semantic categories.xls')
language_model = os.path.join('../results/','es_all_words_from_affective_norms.csv')

print('loading model, and it is going to take some time...')
model_word2vec = pd.read_csv(language_model,encoding = 'latin-1')

df = pd.read_excel(source_data,encoding = 'latin-1')
df = df.drop_duplicates(['English'])
df = df[df['Frequency'] != 0]
df = df[np.logical_or(df['Category'] == 'animal',df['Category'] == 'object')]
df.loc[:,'log_frequency'] = np.log(df['Frequency'].values)
df_animal = df[df['Category'] == 'animal']
df_object = df[df['Category'] == 'object']
df_animal['picked'] = np.logical_and(df_animal['Mean\nFamiliarity'].apply(lambda x: 3<=x<=5),
                                     df_animal['Mean\nConcreteness'].apply(lambda x: 6<=x<=8))
df_object['picked'] = np.logical_and(df_object['Mean\nFamiliarity'].apply(lambda x: 3<=x<=5),
                                     df_object['Mean\nConcreteness'].apply(lambda x: 6<=x<=8))
lower_bound = np.min([np.sum(df_animal['picked']),np.sum(df_object['picked'])])
print('sample {lower_bound} words'.format(lower_bound=lower_bound))
if lower_bound > 100:
    lower_bound = lower_bound - (lower_bound % 100)

df_animal = df_animal[df_animal['picked']]
df_object = df_object[df_object['picked']]
df_animal = df_animal.nlargest(lower_bound,'Mean\nFamiliarity')
df_object = df_object.nlargest(lower_bound,'Mean\nFamiliarity')
df_final = pd.concat([df_animal,df_object])
df_final = df_final.sort_values(['Category','Word'])

ewrq
base_clf = make_pipeline(StandardScaler(),
                    LogisticRegression(C=1, solver='liblinear',
                                       multi_class='auto'))
word_vecs = np.array([model_word2vec[word] for word in df_final['Word']])
labels = np.array([label_map[item] for item in df_final['Category']])
cv = LeavePOut(p = 2)
groups = df_final['Word'].values

results = dict(
                fold = [],
                score = [],
                test_word1 = [],
                test_word2 = [],
                )

for fold, (idx_train,idx_test) in tqdm(enumerate(cv.split(word_vecs,labels,groups = groups))): 
    X_train,y_train = word_vecs[idx_train],labels[idx_train]
    X_test,y_test = word_vecs[idx_test],labels[idx_test]
    X_train,y_train = shuffle(X_train,y_train)
    test_pairs = groups[idx_test]
    clf = clone(base_clf)
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


axis_labels = df_final['English'].values
decode_distance = pd.DataFrame(decode_distance,index = axis_labels,columns=axis_labels)

fig,ax = plt.subplots(figsize = (20,20))
ax = sns.heatmap(decode_distance,
                 xticklabels = True,
                 yticklabels = True,
                 square = True,
                 ax = ax,
                 cmap = plt.cm.coolwarm,
                 )
_ = ax.set(title = 'Red = dissimilar, Blue = similar')
ax.axhline(round(len(groups) / 2),linestyle = '--', color = 'black', alpha = 1.)
ax.axvline(round(len(groups) / 2),linestyle = '--', color = 'black', alpha = 1.)
fig.savefig('../figures/decode sampled words (decode in spanish, translated).jpeg',
            dpi = 500,
            bbox_inches = 'tight')















