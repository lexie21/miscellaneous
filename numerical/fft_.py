import wave
file = wave.open('FFT.wav')
outs = file.readframes(5)
print(outs)
file.close()
import numpy as np
import matplotlib.pyplot as plt
audio_samples = np.frombuffer(outs, dtype=np.int16)
print(audio_samples)
plt.plot(audio_samples)