import numpy as np
import librosa
import os


def mean_mfccs(x):
    return [np.mean(feature) for feature in librosa.feature.mfcc(x)]


def parse_audio(x):
    return x.flatten('F')[:x.shape[0]]


def predict_audio(file_name):
    samples = []
    x, sr = librosa.load(file_name, sr=None)
    if not len(x) == 0:
        x = parse_audio(x)
        samples.append(mean_mfccs(x))
    else:
        print(file_name)
    return np.array(samples)


def predict_knn(knn_model, file):
    print(file)
    x = predict_audio(file)
    result = knn_model.predict(x)
    return int(result[0])