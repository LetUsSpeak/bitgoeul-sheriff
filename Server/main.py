import uvicorn
import os
import joblib
import wave

from fastapi import File, UploadFile, FastAPI
from typing import List
from keras.models import load_model
from knn import predict_knn
from cnn import predict_cnn


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = FastAPI()

# knn_binary = joblib.load('model/knn_binary_model (3).pkl')
knn_code = joblib.load('model/knn_code_model_code.pkl')
# cnn_code = load_model('model/CNN_code_model.h5')
# cnn_situation1 = load_model('model/CNN_all_model.h5')
# cnn_situation2 = load_model('model/CNN_all_model_final.h5')


@app.get('/')
def read_root():
    return 'Server is ready!'


@app.post('/multi_wav/')
async def upload_multi_wav(files: List[UploadFile] = File(...)):
    data = []
    for file in files:
        wf = wave.open(file.file, 'rb')
        data.append([wf.getparams(), wf.readframes(wf.getnframes())])
        wf.close()

    audio_path = os.path.join('audio/', files[-1].filename)

    output = wave.open(audio_path, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

    # binary = predict_knn(knn_binary, audio_path)
    knncode = predict_knn(knn_code, audio_path)
    # cnncode = predict_cnn(cnn_code, audio_path)
    # situation1 = predict_cnn(cnn_situation1, audio_path)
    # situation2 = predict_cnn(cnn_situation2, audio_path)

    # return {'binary': binary, 'knncode': knncode, 'cnncode': cnncode, 'ituation1': situation1, 'situation2': situation2}
    return knncode