import numpy as np
import librosa
from PIL import Image
import soundfile


m=Image.open("result.tif") 
img=np.array(m)
wav=librosa.feature.inverse.mel_to_audio(img)
soundfile.write("4.wav",wav,samplerate=22050)