import sys, os
import speedtest
from datetime import datetime
from api_communication import *

# test upload speed. Typically in Mbit/s
wifi = speedtest.Speedtest(secure=True)
#bestWifi = wifi.get_best_server()
#print(f"Found: {bestWifi['host']} located in {bestWifi['country']}")


#filename = sys.argv[1]
audioFile = 'short1.WAV'
waveDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'wave')
filename = os.path.join(waveDir, audioFile)
file_size = os.path.getsize(filename)
upload_speed = wifi.upload() # bit/sec

print(f"Upload speed is {upload_speed/1000000:.1f} Mbit/s")
print(f"File size is {file_size/1000000:.1f} Mbytes")
upload_time = file_size*8/upload_speed/60 # time in minutes
print(f"Will take approx {upload_time:.1f} min to upload the audio file to assemblyai")

print("{0} submitted {1}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), filename))
audio_url = upload(filename)
save_transcript(audio_url, filename)









