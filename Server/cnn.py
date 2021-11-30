import librosa
import numpy as np


def extract_feature(file_name):
    y, sr = librosa.load(file_name)
    start = int(0 * sr)
    end = int(30 * sr)
    y = y[start:end]
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return mfccs


def print_situation(label):
    class_code = {'dating-violence': 0, 'injury': 1, 'office-violence': 2, 'rape': 3, 'robber': 4,
                  'sponsor': 5, 'violence': 6, 'candid-cam': 7, 'disorder': 8, 'drunken': 9,
                  'flasher': 10, 'inebriate': 11, 'invasion': 12, 'crying': 13, 'normal': 14}
    result = {v: k for k, v in class_code.items()}
    return result.get(label)


def predict_cnn(cnn_model, file):
    x = extract_feature(file)
    x = np.array(x)
    x = x.reshape(-1, x.shape[0], x.shape[1], 1)
    y = cnn_model.predict(x)
    result = np.argmax(y)
    situation = print_situation(result)
    return situation