import speech_recognition as sr
import re
import os


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
        print("Sorry, could not recognize your voice")



def open_file(file_path):
    try:
        os.system(f'open "{file_path}"')
    except Exception as e:
        print(f"Error: {e}")

def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            pass
    except Exception as e:
        print(f"Error: {e}")

def open_folder(folder_path):
    try:
        os.system(f'open "{folder_path}"')
    except Exception as e:
        print(f"Error: {e}")

def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
    except Exception as e:
        print(f"Error: {e}")





def process_command(text):
    if text:
        open_file_match = re.match(r"open file (.+)", text)
        create_file_match = re.match(r"create file (.+)", text)
        open_folder_match = re.match(r"open folder (.+)", text)
        create_folder_match = re.match(r"create folder (.+)", text)

        if open_file_match:
            file_path = open_file_match.group(1)
            open_file(file_path)
        elif create_file_match:
            file_path = create_file_match.group(1)
            create_file(file_path)
        elif open_folder_match:
            folder_path = open_folder_match.group(1)
            open_folder(folder_path)
        elif create_folder_match:
            folder_path = create_folder_match.group(1)
            create_folder(folder_path)
        else:
            print("Invalid command. Please try again.")
            

# ... (main loop)

while True:
    user_input = text
    if user_input == 'exit':
        break
    process_command(user_input)





    switch_var = ctk.StringVar(value="on")


