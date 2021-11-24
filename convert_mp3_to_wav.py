#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydub import AudioSegment


# In[ ]:


input_path = "./AnnotatedAudioFiles/*.mp3"  
for f in glob.glob(input_path):          # 코드간결화 작업전
    sound = AudioSegment.from_mp3(f)
    name = f.split('/')[2].split('.')[0]
    sound.export(f"./AnnotatedAudioFiles/{name}.wav", format="wav")

