from gtts import gTTS

def make_aud(ttt, lan):
    tts = gTTS(text=ttt,lang=lan)
    tts.save("res/temp.mp3")