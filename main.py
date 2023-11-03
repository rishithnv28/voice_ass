from commands.commands import Commands
from voice_rec.speech_text import recognize

input = "open browser"

while(1):
    input = recognize()

    commands_instance = Commands()
    commands_instance.execute_command(input)
