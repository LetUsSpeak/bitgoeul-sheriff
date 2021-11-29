import os
import numpy as np
import pandas as pd
import time 
import librosa
import soundfile as sf # librosa fails when reading files on Kaggle.
import joblib
'''
knn_from_pickle = joblib.load('knn_model.pkl')



print(knn_from_pickle)  



def mean_mfccs(x):
    return [np.mean(feature) for feature in librosa.feature.mfcc(x)]

def parse_audio(x):
    return x.flatten('F')[:x.shape[0]] 


def predict_audio(file_name):
    samples = []
    x, sr = sf.read(file_name, always_2d=True)
    if not len(x) == 0:
        x = parse_audio(x)
        samples.append(mean_mfccs(x))
    else:
        print(file_name)
    return np.array(samples)


x = predict_audio('./AnnotatedAudioFiles/code0_injury_B25.wav')

print(x)

knn_from_pickle.predict(x)
'''


def get_knn_predict_result(
        model_name = 'knn_model.pkl', 
        audio_file_path = "./AnnotatedAudioFiles/code0_injury_B25.wav"
        ):
        
    knn_from_pickle = joblib.load(model_name)
    
    def mean_mfccs(x):
        return [np.mean(feature) for feature in librosa.feature.mfcc(x)]

    def parse_audio(x):
        return x.flatten('F')[:x.shape[0]] 


    def predict_audio(file_name):
        samples = []
        x, sr = sf.read(file_name, always_2d=True)
        if not len(x) == 0:
            x = parse_audio(x)
            samples.append(mean_mfccs(x))
        else:
            print(file_name)
        return np.array(samples)


    x = predict_audio(audio_file_path)

    knn_from_pickle.predict(x)
    
    return x
    
    