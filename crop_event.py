#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import os
import soundfile as sf
import librosa
import numpy as np
import glob
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv('event_data_preprocesssing_jjin_real_final.csv')


# In[8]:


df


# In[9]:


j = len(df)


# In[12]:


train_path = "./AnnotatedAudioFiles/"
train_file_list = os.listdir(train_path)
train_file_names = [file for file in train_file_list if file.endswith(".wav")]
train_file_names.sort(key=lambda x: (x.partition('.')[0]))


# # event 음원 추출

# In[ ]:


for i in range(j):
    if df.iloc[i]['file_name'] not in train_file_names:
        print(df.iloc[i]['file_name'])
    file_path = './AnnotatedAudioFiles/' + df.iloc[i]['file_name']
    x, sr = sf.read(file_path, always_2d=True)
    start = int(df.iloc[i]['from'] * sr)
    end = int(df.iloc[i]['to'] * sr)
    y = x[start : end]
    if start==end:
        print(df.iloc[i]['file_name'])
        df.iloc[i] = None
        continue
    event = df.iloc[i]['event']
    sf.write(f'./sound_extract/{i}_{event}.wav', y, sr)

