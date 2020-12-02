<<<<<<< HEAD
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

fontsize = 16
image_size_pixel = 512
dpi = 300

pathes = []
for ii,row in df.iterrows():
    row
    fig,ax = plt.subplots(figsize = (image_size_pixel/dpi,image_size_pixel/dpi))
    ax.text(0.45,0.45,row['Word'].lower(),
            ha = 'center',
            fontsize = fontsize,)
    ax.axis('off')
    pathes.append(os.path.join(figure_dir,f'{row["English"].lower()}.jpeg'))
    fig.savefig(os.path.join(figure_dir,f'{row["English"].lower()}.jpeg'),
                dpi = 300,
                bbox_inches = 'tight')
    plt.close('all')

df['PATH_spanish'] = pathes

#pathes = []
#for ii,row in df.iterrows():
#    row
#    fig,ax = plt.subplots(figsize = (image_size_pixel/dpi,image_size_pixel/dpi))
#    ax.text(0.45,0.45,row['English'].lower(),
#            ha = 'center',
#            fontsize = fontsize,)
#    ax.axis('off')
#    pathes.append(os.path.join(figure_dir,f'{row["English"].upper()}.jpeg'))
#    fig.savefig(os.path.join(figure_dir,f'{row["English"].upper()}.jpeg'),
#                dpi = 300,
#                bbox_inches = 'tight')
#    plt.close('all')
#
#df['PATH_english'] = pathes

columns = []
for col in df.columns:
    if '\n' in col:
        col = col.replace('\n','_')
    columns.append(col)
df.columns = columns
df.to_csv('../data/sampled_words.csv',encoding = 'latin-1',index = False)

=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:11:23 2020

@author: nmei
"""

import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('dark_background')

df = pd.read_csv('../data/sampled.csv',encoding = 'latin-1')
figure_dir = '../stimuli_figure'
if not os.path.exists(figure_dir):
    os.mkdir(figure_dir)

dpi = 300
image_size = 512
fontsize = 20

pathes = []
for ii,row in df.iterrows():
    fig,ax = plt.subplots(figsize = (image_size/dpi,image_size/dpi))
    ax.text(0.45,0.45,row['Word'].lower(),
            ha = 'center',
            va = 'center',
            fontsize = fontsize,
            )
    ax.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    pathes.append(os.path.join(figure_dir,f'{row["English"].lower()}.jpeg'))
    fig.savefig(os.path.join(figure_dir,f'{row["English"].lower()}.jpeg'),
                dpi = dpi,
#                bbox_inches = 'tight'
                )
    plt.close('all')

df['PATH_spanish'] = pathes

pathes = []
for ii,row in df.iterrows():
    fig,ax = plt.subplots(figsize = (image_size/dpi,image_size/dpi))
    ax.text(0.45,0.45,row['English'].lower(),
            ha = 'center',
            va = 'center',
            fontsize = fontsize,
            )
    ax.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    pathes.append(os.path.join(figure_dir,f'{row["English"].upper()}.jpeg'))
    fig.savefig(os.path.join(figure_dir,f'{row["English"].upper()}.jpeg'),
                dpi = dpi,
#                bbox_inches = 'tight'
                )
    plt.close('all')

df['PATH_english'] = pathes

columns = []
for col in df.columns:
    if '\n' in col:
        col = col.replace('\n','_')
    columns.append(col)
df.columns = columns

# add varying blank period
df['blank_dur'] = np.random.uniform(low = 0.3,high = 0.7,size = df.shape[0])
df['category'] = df['Category'].map({'animal':'Living_Things',
                                     'object':'Nonliving_Things'})
df.to_csv('../data/sampled_words.csv',encoding = 'latin-1',index = False)
>>>>>>> 5fe83eaa2f078f018ecde81bc7fd2529be564dee
