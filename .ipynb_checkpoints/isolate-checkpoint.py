import librosa
from librosa import display
import numpy as np
import IPython.display as ipd
import matplotlib as plt

y, sr = librosa.load('test.wav')
ipd.Audio(data=y[90*sr:110*sr], rate=sr)
