# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:03:27 2020

@author: ning
"""
import os
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('dark_background')

df = pd.read_csv('../data/sampled.csv',encoding = 'latin-1')
figure_dir = '../stimuli_figure'
if not os.path.exists(figure_dir):
    os.mkdir(figure_dir)

pathes = []
for ii,row in df.iterrows():
    row
    fig,ax = plt.subplots(figsize = (4,4))
    ax.text(0.5,0.5,row['Word'],
            ha = 'center',
            fontsize = 16,)
    pathes.append(os.path.join(figure_dir,f'{row["English"]}.jpeg'))
    fig.savefig(os.path.join(figure_dir,f'{row["English"]}.jpeg'),
                dpi = 300,
                bbox_inches = 'tight')
    plt.close('all')

df['PATH'] = pathes
columns = []
for col in df.columns:
    if '\n' in col:
        col = col.replace('\n','_')
    columns.append(col)
df.columns = columns
df.to_csv('../data/sampled_words.csv',encoding = 'latin-1',index = False)