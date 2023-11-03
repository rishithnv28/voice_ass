#browser:
open browser
close browser
open firefox
close firefox
start writing
finish_writing
#edior:
open editor_(start writing)
close editor
open github (_in browser)
close github
open VS code
close VS code
save VS code
open libre office_(start writing)
close libre office
write to libre office Hello, World!
save libre office
#mailing:
start writing mail(subject, matter, to, attach)
open outlook_(start writing mail)
close outlook
open gmail_(start writing mail)
close gmail
#network_config:
switch wifi on
switch wifi off
change wifi to _(network)
switch bluetooth on
switch bluetooth off
change bluetooth to _(network)
#scripts:
execute terminal command "ls -l" _(start writing)
download+install+add to path
minimize
print system information
cpu temp
#system:
increase volume
decrease volume
increase brightness
decrease brightness
mute_volume
take screenshot (_save to modify)
#wedges:
open calculator
close calculator
set alarm
del alarm
#websearch:
what is _(start writing) wiki
#application:
play music (_default)
play playlist
pause music
next track
previous track
#filemanger:
open folder /path/to/folder
folder /path/to/folder
open file /path/to/file.txt
close file /path/to/file.txt
minimize
#processes:
open task manager
close task manager
show processes
kill process process_name
set alerts for process completion
#voice_ass:
go to sleep
sleep
wake up
awake
trigger
stop

click icon ML(AI)


usage:
from execution import Execution
from commands import Commands

# Make an object
execution = Execution()

# call
try:
    execution.execute_command("open browser")  # Opens the default web browser
except:
    print("unable to open browser")
