import sys, os
from api_communication import *

#filename = sys.argv[1]
audioFile = '24min.WAV'
waveDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'wave')
filename = os.path.join(waveDir, audioFile)
print(filename)

audio_url = upload(filename)
save_transcript(audio_url, filename)









