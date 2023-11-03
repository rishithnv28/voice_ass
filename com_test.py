from commands.commands import Commands

#testing
commands = Commands()

# Browser Commands
commands.execute_command("open browser")
commands.execute_command("close browser")
commands.execute_command("open firefox")
commands.execute_command("close firefox")

# Editor Commands
commands.execute_command("open editor")
commands.execute_command("close editor")
commands.execute_command("open github")
commands.execute_command("close github")
commands.execute_command("open VS code")
commands.execute_command("close VS code")
commands.execute_command("save VS code")
commands.execute_command("open libre office")
commands.execute_command("close libre office")
commands.execute_command("write to libre office Hello, World!")
commands.execute_command("save libre office")

# Mailing Commands
'''commands.execute_command("start writing mail")
commands.execute_command("open outlook")
commands.execute_command("close outlook")
commands.execute_command("open gmail")
commands.execute_command("close gmail")'''

# Network Config Commands
'''commands.execute_command("switch wifi on")
commands.execute_command("switch wifi off")
commands.execute_command("change wifi to MyWiFiNetwork")
commands.execute_command("switch bluetooth on")
commands.execute_command("switch bluetooth off")
commands.execute_command("change bluetooth to MyBluetoothDevice")'''

# Scripts Commands
commands.execute_command("execute terminal command ls -l")
#commands.execute_command("download+install+add to path")
commands.execute_command("minimize")
commands.execute_command("print system information")
commands.execute_command("cpu temp")

# System Commands
commands.execute_command("increase volume")
commands.execute_command("decrease volume")
commands.execute_command("increase brightness")
commands.execute_command("decrease brightness")
commands.execute_command("mute volume")
commands.execute_command("take screenshot")

# Wedges Commands
commands.execute_command("open calculator")
commands.execute_command("close calculator")
commands.execute_command("set alarm")
commands.execute_command("del alarm")

# Web Search Commands
commands.execute_command("what is Python programming language")

# Applications Commands
'''commands.execute_command("play music")
commands.execute_command("play playlist")
commands.execute_command("pause music")
commands.execute_command("next track")
commands.execute_command("previous track")'''

# File Manager Commands
'''commands.execute_command("open folder /path/to/folder")
commands.execute_command("folder /path/to/folder")
commands.execute_command("open file /path/to/file.txt")
commands.execute_command("close file /path/to/file.txt")
commands.execute_command("minimize")'''

# Processes Commands
'''commands.execute_command("open task manager")
commands.execute_command("close task manager")
commands.execute_command("show processes")
commands.execute_command("kill process process_name")
commands.execute_command("set alerts for process completion")'''

# Voice Assistant Commands
commands.execute_command("go to sleep")
commands.execute_command("sleep")
commands.execute_command("wake up")
commands.execute_command("awake")
commands.execute_command("trigger")
commands.execute_command("stop")