# .mp3 compresses and can lose information
# .flac compresses without loss
# .wav uncompressed, audio quality is best (CD format)

import wave
# - number of channels
# - sample width (number of bytes/sample)
# - framerate or sample_rate (number of samples per sec. ie 44,100Hz is std rate for CD)
# - number of frames
# - values of a frame (binary format)

obj = wave.open("wave/short1.WAV", "rb") # read binary
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate() # how long the wave is
print(t_audio)

frames = obj.readframes(-1) # read all frames
print(type(frames), type(frames[0]))
print(len(frames) / (obj.getsampwidth() * obj.getnchannels())  # sample width was 2 or 2 bytes/sample. But still double what obj.getnframes says?? Because 2 channels?
obj.close()

obj_new = wave.open("wave/short1b_new.wav", "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000.0)
obj_new.writeframes(frames)
obj_new.close()

