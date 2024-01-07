
from gtts import gTTS
from playsound import playsound
import time

#time.sleep(5)
time.sleep(0.1)
mytext= ".. "
myjob = gTTS(text = mytext)
myjob.save("welcome.mp3")
playsound("welcome.mp3")
'''
from playsound import playsound

# اسم الملف الصوتي الذي تريد تشغيله
audio_file = "sound.mp3"

# تشغيل الملف الصوتي
playsound(audio_file)
'''

x=5
x=2
z=x+3
print("z : ",z)
print("hellw")
