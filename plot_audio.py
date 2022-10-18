import wave
import matplotlib.pyplot as plt 
import numpy as np

obj = wave.open("wave/short1.WAV", "rb") # read binary
sample_freq = obj.getframerate()
n_samples = obj.getnframes() * obj.getnchannels()  # got a matplot error that X,Y axis didn't match. Had to multiply by number of channels. See wave-example.py notes
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_samples / sample_freq
print(t_audio) # length of audio

signal_array = np.frombuffer(signal_wave, dtype=np.int16) # getting the Y axis data
times = np.linspace(0, t_audio, num=n_samples) # getting the X axis info
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array) # plots X against Y
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio) # limit
plt.show()