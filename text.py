
from gtts import gTTS
import os

mytext = 'Hello World. How Are you? My name is Vansh'

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("speech.mp3")
os.system("mpg321 welcome.mp3")
