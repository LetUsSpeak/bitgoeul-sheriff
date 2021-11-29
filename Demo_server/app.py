from typing import Optional
from fastapi import File, UploadFile, FastAPI, HTTPException
import uvicorn
import shutil
import os
from predict import getAnalysisResult
import numpy as np
import librosa
import soundfile as sf


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "wwWorld"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q:Optional[str] = None):
    return {"item_id": item_id, "q":q}


@app.post("/v1/upload-analysis/")
async def upload_anal(file: UploadFile = File(...)):



    from knn_predict import get_knn_predict_result

    knn_result = get_knn_predict_result(
                        'knn_model.pkl', 
                        './AnnotatedAudioFiles/code0_injury_B25.wav'
                        )

    DIR = 'sounds/'
    #if "wav" not in file.filename[-3:]:
        #raise HTTPException(status_code=422, detail="File extension is not allowed")

    
    soundfile = os.path.join(DIR, file.filename)
    with open(soundfile, "wb") as buffer:
         shutil.copyfileobj(file.file, buffer)
         result = getAnalysisResult(soundfile)
    
    return {"file": file.filename, "result": knn_result}



if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=12345, reload=True)



