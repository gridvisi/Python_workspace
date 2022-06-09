import speech Recognition as sr

r = sr.Recogizer()
with sr.Microphone() as source:
    print("Speak Anything:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:{}".format(text))
    except:
        print("Sorry could not recognize what yo said")
