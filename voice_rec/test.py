import openai
import speech_recognition as sr
import base64


# Set your API key
openai.api_key = "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"
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Please speak something...")
    audio = recognizer.listen(source)

     # write audio
    with open("audio.mp3", "wb") as f:
        f.write(audio.get_wav_data())

# Read binary audio data from a file
with open("audio.mp3", "rb") as audio:
    binary_audio_data = audio.read()

# Encode the binary audio data to base64
base64_audio_data = base64.b64encode(binary_audio_data).decode("utf-8")


# Provide audio data (base64-encoded)
audio_data = base64_audio_data

# Make the API request to transcribe audio

audio_file= open('/home/lohit/Desktop/hackout /audio.wav', "rb")


response = openai.Audio.transcribe("whisper-1", audio_file,response_format="text")
# Print the transcribed text
print(response['text'])

