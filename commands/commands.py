from .execution import Execution
execution = Execution()

class Commands:
    def __init__(self):
        self.is_awake = True

    def execute_command(self, command):
        if self.is_awake:
            # Browser
            if command == "open browser":
                execution.open_browser()
            elif command == "close browser":
                execution.close_browser()
            elif command == "open firefox":
                execution.open_firefox()
            elif command == "close firefox":
                execution.close_firefox()
            elif command == "start writing":
                execution.start_writing()
            elif command == "finish writing":
                execution.finish_writing()

            # Editor
            elif command == "open editor":
                execution.open_editor()
            elif command == "close editor":
                execution.close_editor()
            elif command == "open github":
                execution.open_github()
            elif command == "close github":
                execution.close_github()
            elif command == "open VS code":
                execution.open_vscode()
            elif command == "close VS code":
                execution.close_vscode()
            elif command == "save VS code":
                execution.save_vscode()
            elif command.startswith("open libre office"):
                execution.open_libre_office()
            elif command == "close libre office":
                execution.close_libre_office()
            elif command.startswith("write to libre office"):
                text = command[21:]
                execution.write_to_libre_office(text)
            elif command == "save libre office":
                execution.save_libre_office()

            # Mailing
            elif command == "start writing mail":
                execution.start_writing_mail()
            elif command == "open outlook":
                execution.open_outlook()
            elif command == "close outlook":
                execution.close_outlook()
            elif command == "open gmail":
                execution.open_gmail()
            elif command == "close gmail":
                execution.close_gmail()

            # Network Config
            elif command == "switch wifi on":
                execution.switch_wifi_on()
            elif command == "switch wifi off":
                execution.switch_wifi_off()
            elif command.startswith("change wifi to"):
                wifi = command[14:]
                execution(wifi)
            elif command == "switch bluetooth on":
                execution.switch_bluetooth_on()
            elif command == "switch bluetooth off":
                execution.switch_bluetooth_off()
            elif command.startswith("change bluetooth to"):
                bluetooth = command[18:]
                execution(bluetooth)

            # Scripts
            elif command.startswith("execute terminal command "):
                terminal_command = command[26:]
                execution.execute_terminal_command(terminal_command)
            elif command == "download+install+add to path":
                execution.download_install_add_to_path()
            elif command == "minimize":
                execution.minimize_window()
            elif command == "print system information":
                execution.print_system_information()
            elif command == "cpu temp":
                execution.get_cpu_temperature()

            # System
            elif command == "increase volume":
                execution.increase_volume()
            elif command == "decrease volume":
                execution.decrease_volume()
            elif command == "increase brightness":
                execution.increase_brightness()
            elif command == "decrease brightness":
                execution.decrease_brightness()
            elif command == "mute volume":
                execution.mute_volume()
            elif command == "take screenshot":
                execution.take_screenshot()  # Save to modify

            # Wedges
            elif command == "open calculator":
                execution.open_calculator()
            elif command == "close calculator":
                execution.close_calculator()
            elif command == "set alarm":
                execution.set_alarm()
            elif command == "del alarm":
                execution.del_alarm()

            # Web Search
            elif command.startswith("what is "):
                query = command[8:]
                execution.start_writing(query + " wiki")

            # Applications
            elif command == "play music":
                execution.play_music()  # Default
            elif command == "play playlist":
                execution.play_playlist()
            elif command == "pause music":
                execution.pause_music()
            elif command == "next track":
                execution.next_track()
            elif command == "previous track":
                execution.previous_track()

            # File Manager
            elif command.startswith("open folder "):
                folder_path = command[12:]
                execution.open_folder(folder_path)
            elif command.startswith("folder "):
                folder_path = command[7:]
                execution.open_folder(folder_path)
            elif command.startswith("open file "):
                file_path = command[10:]
                execution.open_file(file_path)
            elif command.startswith("close file "):
                file_path = command[11:]
                execution.close_file(file_path)
            elif command == "minimize":
                execution.minimize()

            # Processes
            elif command == "open task manager":
                execution.open_task_manager()
            elif command == "close task manager":
                execution.close_task_manager()
            elif command == "show processes":
                execution.show_processes()
            elif command.startswith("kill process "):
                process_name = command[13:]
                execution.kill_process(process_name)
            elif command == "set alerts for process completion":
                execution.set_alerts_for_process_completion()

            # Voice Assistant
            elif command == "go to sleep":
                self.is_awake = False
            elif command == "sleep":
                self.is_awake = False
            elif command == "wake up":
                self.is_awake = True
            elif command == "awake":
                self.is_awake = True
            elif command == "trigger":
                execution.trigger()
            elif command == "stop":
                execution.stop()

            else:
                print("Command not recognized")
        else:
            if command == "wake up":
                self.wake_up()
            else:
                print("I'm asleep. Say 'wake up' to activate me.")

