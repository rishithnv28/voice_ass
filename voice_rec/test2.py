import speech_recognition as sr



recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Please speak something...")
    audio = recognizer.listen(source)
    try :
        text = recognizer.recognize_google(audio)
        k=format(text)
        print("You said : "+str(k))
    except:
        print("Sorry could not recognize your voice")

print(k)

