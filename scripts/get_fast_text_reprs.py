#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:17:16 2020

@author: nmei
"""

import os
from glob import glob

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.spatial import distance
#from gensim.models.keyedvectors import KeyedVectors
from matplotlib import pyplot as plt

working_dir = '../data'
working_data = os.path.join(working_dir,'Affective norms for 380 Spanish words belonging to three different semantic categories.xls')
#language_model = os.path.join(working_dir,'cc.es.300.vec.gz')
language_model = os.path.join('../results/','es_all_words_from_affective_norms.csv')

print('loading model, and it is going to take some time...')
model_word2vec = pd.read_csv(language_model,encoding = 'latin-1')

df = pd.read_excel(working_data,encoding = 'latin-1')
all_words = np.array([model_word2vec[word] for word in df['Word']])
df_all_words = pd.DataFrame(all_words.T,columns = df['Word'])
#df_all_words.to_csv('../results/es_all_words_from_affective_norms.csv',index = False,encoding = 'latin-1')
df = df.drop_duplicates(['English'])
df = df[df['Frequency'] != 0]
df = df[np.logical_or(df['Category'] == 'animal',df['Category'] == 'object')]

df.loc[:,'log_frequency'] = np.log(df['Frequency'].values)

g = sns.pairplot(df,
                 hue = 'Category',
                 vars = ['Mean\nValence','Mean\nArousal','Mean\nFamiliarity','Mean\nConcreteness','Length','log_frequency'],
                 diag_kind = 'kde')

g.savefig('../figures/before subsampled.jpeg',bbox_inches = 'tight')

df_animal = df[df['Category'] == 'animal']
df_object = df[df['Category'] == 'object']
df_animal['picked'] = np.logical_and(df_animal['Mean\nFamiliarity'].apply(lambda x: 3<=x<=5),
                                     df_animal['Mean\nConcreteness'].apply(lambda x: 6<=x<=8))
df_object['picked'] = np.logical_and(df_object['Mean\nFamiliarity'].apply(lambda x: 3<=x<=5),
                                     df_object['Mean\nConcreteness'].apply(lambda x: 6<=x<=8))
#df_animal['picked'] = np.logical_and(np.logical_and(df_animal['Mean\nFamiliarity'].apply(lambda x: 2.5<=x<=5),
#                                     df_animal['Mean\nConcreteness'].apply(lambda x: 6<=x<=9)),
#                                            df_animal["Mean\nValence"].apply(lambda x: 4.5<=x<=6))
#df_object['picked'] = np.logical_and(np.logical_and(df_object['Mean\nFamiliarity'].apply(lambda x: 2.5<=x<=5),
#                                     df_object['Mean\nConcreteness'].apply(lambda x: 6<=x<=9)),
#                                            df_object["Mean\nValence"].apply(lambda x: 4.5<=x<=6))
lower_bound = np.min([np.sum(df_animal['picked']),np.sum(df_object['picked'])])
print('sample {lower_bound} words'.format(lower_bound=lower_bound))
if lower_bound > 100:
    lower_bound = lower_bound - (lower_bound % 100)

df_animal = df_animal[df_animal['picked']]
df_object = df_object[df_object['picked']]
df_animal = df_animal.nlargest(lower_bound,'Mean\nFamiliarity')
df_object = df_object.nlargest(lower_bound,'Mean\nFamiliarity')
df_final = pd.concat([df_animal,df_object])

df_violin = pd.melt(df_final,id_vars = ["Category"],
                    value_vars = ['Mean\nValence','Mean\nArousal','Mean\nFamiliarity','Mean\nConcreteness','Length','log_frequency'])

sns.catplot(x = "Category",
            y = "value",
            row="variable",
            data = df_violin,
            kind = "violin",
            **{"cut":0,
               "inner":"quartile"})

g = sns.pairplot(df_final,
                 hue = 'Category',
                 vars = ['Mean\nValence','Mean\nArousal','Mean\nFamiliarity','Mean\nConcreteness','Length','log_frequency'],
                 diag_kind = 'kde')
g.savefig('../figures/after subsampled.jpeg',bbox_inches = 'tight')

df_final = df_final.sort_values(['Category','Word'])
words = df_final['Word'].values
categories = df_final['Category'].values
english = df_final['English'].values
word_vecs = np.array([model_word2vec[word] for word in words])

RDM = distance.squareform(distance.pdist(word_vecs - word_vecs.mean(1).reshape(-1,1),'cosine'))
RDM_copy = RDM.copy()
np.fill_diagonal(RDM,np.nan)
labels = words.copy()
df_plot = pd.DataFrame(RDM,index = labels,columns = labels)
np.fill_diagonal(RDM_copy,0)
df_cluster = pd.DataFrame(RDM_copy,index = labels,columns = labels)

fig,ax = plt.subplots(figsize = (20,20))
ax = sns.heatmap(df_plot,
                 xticklabels = True,
                 yticklabels = True,
                 square = True,
                 ax = ax,
                 cmap = plt.cm.coolwarm,
                 )
ax.axvline(df_plot.shape[0] / 2, linestyle = '--',color = 'black',alpha = 1.)
ax.axhline(df_plot.shape[0] / 2, linestyle = '--',color = 'black',alpha = 1.)
fig.savefig('../figures/RDM.jpeg',dpi = 500,bbox_inches = 'tight')

g = sns.clustermap(df_cluster,figsize = (20,20),xticklabels = True,yticklabels = True,
                   cmap = plt.cm.coolwarm,)
g.savefig('../figures/cluster RDM.jpeg',dpi = 500,bbox_inches = 'tight')

df_final.to_csv(os.path.join(working_dir,'sampled.csv'),index = False,encoding='latin-1')

sampled_words = np.array([model_word2vec[word] for word in words])
df_sampled_words = pd.DataFrame(sampled_words.T,columns = words)
df_sampled_words.to_csv('../results/sampled_words.csv',index = False,encoding = 'latin-1')
plt.close('all')















