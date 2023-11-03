import speech_recognition as sr

x= "something went wrong"
recognizer = sr.Recognizer()
def recognize():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Please speak something...")
        audio = recognizer.listen(source)
        try :
            text = recognizer.recognize_google(audio)
            y =format(text)
            return y
        except:
            return x

print(recognize())