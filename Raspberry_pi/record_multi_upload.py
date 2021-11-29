import pyaudio
import wave
import requests
import threading
import os
import json


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 2048
RECORD_SECONDS = 6.1
N_WAV = 5

global FLAG
FLAG = 1


def recording(index, WAVE_OUTPUT_FILENAME):
    # start recording
    stream = audio.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True, 
                    input_device_index=1,
                    frames_per_buffer=CHUNK)

    print(f'recording {index}...', '\n')

    frames = []
    for j in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop recording
    stream.stop_stream()
    stream.close()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def uploading(index):
    global FLAG

    while FLAG != 1:
        time.sleep(2)
        print('sleeping...', '\n')
    
    # upload wav
    FLAG = 0
    print(f'uploading {index-4}~{index}...', '\n')

    url = 'http://f999-183-105-84-187.ngrok.io/multi_wav/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}       
    
    files = []
    for i in range(4, -1, -1):
        file = ('files', open(f'./audio/audio_{index-i}.wav', 'rb'))
        files.append(file)

    res = requests.post(url, headers=headers, files=files)
    print(res.text)

    result = json.loads(res.text)
    binary = result['binary']

    if binary == 1:
        print('!!!!! emergency !!!!!')
        os.system('aplay -d 5 siren.wav')
        print()
    else:
        print('not emergency', '\n')

    FLAG = 1


if __name__ == '__main__':
    audio = pyaudio.PyAudio()

    for i in range(N_WAV * 5):
        FILE_NAME = f'./audio/audio_{i+1}.wav'
        record = threading.Thread(target=recording, args=(i+1, FILE_NAME))
        upload = threading.Thread(target=uploading, args=(i+1,))

        record.start()
        record.join()

        if (i+1) % 5 == 0:
            upload.start()

    audio.terminate()