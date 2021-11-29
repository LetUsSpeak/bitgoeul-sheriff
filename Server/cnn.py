import librosa
import numpy as np


def extract_feature(file_name):
    y, sr = librosa.load(file_name)
    start = int(0 * sr)
    end = int(30 * sr)
    y = y[start:end]
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return mfccs


def predict_cnn(cnn_model, file):
    x = extract_feature(file)
    x = np.array(x)
    x = x.reshape(-1, x.shape[0], x.shape[1], 1)
    y = cnn_model.predict(x)
    result = np.argmax(y)

    return int(result)