import subprocess
import wikipedia
import time
import subprocess
import os
import shutil
import psutil
import platform
import tempfile
import pyscreenshot as ImageGrab
import time
import wikipedia
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Execution:
    def __init__(self):
       self.is_awake = True
       self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                                client_secret='YOUR_CLIENT_SECRET',
                                                                redirect_uri='YOUR_REDIRECT_URI',
                                                                scope='user-library-read user-read-playback-state user-modify-playback-state'))
 
    def open_program(self, program_name):
        if program_name == "browser":
            subprocess.Popen(["google-chrome"])
        elif program_name == "editor":
            subprocess.Popen(["gedit"])
        elif program_name == "firefox":
            subprocess.Popen(["firefox"])
        elif program_name == "calculator":
            subprocess.Popen(["gnome-calculator"])
        else:
            print("Program not recognized")

    def close_program(self, program_name):
        if program_name == "browser":
            subprocess.Popen(["pkill", "chrome"])
        elif program_name == "editor":
            subprocess.Popen(["pkill", "gedit"])
        elif program_name == "firefox":
            subprocess.Popen(["pkill", "firefox"])
        elif program_name == "calculator":
            subprocess.Popen(["pkill", "gnome-calculator"])
        else:
            print("Program not recognized")

    def open_browser(self):
        subprocess.Popen(["google-chrome"])

    def start_editor(self):
        subprocess.Popen(["gedit"])

    def open_firefox(self):
        subprocess.Popen(["firefox"])

    def close_browser(self):
        subprocess.Popen(["pkill", "chrome"])

    def finish_editor(self):
        subprocess.Popen(["pkill", "gedit"])

    def close_calculator(self):
        subprocess.Popen(["pkill", "gnome-calculator"])

    def what_time_is_it(self):
        current_time = time.strftime("It is %H hours and %M minutes")
        print(current_time)
        return wikipedia.summary(current_time)

    def what_day_is_today(self):
        current_date = time.strftime("Today is %A, %d. %B %Y")
        print(current_date)
        return wikipedia.summary(current_date)

    def go_to_sleep(self):
        self.is_awake = False

    def sleep(self):
        self.is_awake = False

    def awake(self):
        self.is_awake = True

    def wake_up(self):
        self.is_awake = True

    def open_libre_office(self):
        self.open_program("libreoffice")

    def close_libre_office(self):
        self.close_program("libreoffice")

    def write_to_libre_office(self, text):
        try:
            subprocess.Popen(["libreoffice", "--writer", "--view", text])
        except Exception as e:
            print(f"Error: {e}")

    def save_libre_office(self):
        try:
            subprocess.Popen(["libreoffice", "--writer", "--save"])
        except Exception as e:
            print(f"Error: {e}")

    def open_outlook(self):
        self.open_program("thunderbird")  # Assuming Thunderbird is used as an email client on Ubuntu

    def close_outlook(self):
        self.close_program("thunderbird")

    def open_gmail(self):
        self.open_browser()
        try:
            subprocess.Popen(["firefox", "https://mail.google.com"])
        except Exception as e:
            print(f"Error: {e}")

    def close_gmail(self):
        self.close_browser()

    def send_email(self, recipient, subject, body):
        try:
            # Code to send email using a suitable email library (not provided in the snippet)
            print("email sent")
            pass
        except Exception as e:
            print(f"Error: {e}")

    def change_wifi_connectivity(self, status):
        try:
            if status == "on":
                subprocess.Popen(["nmcli", "radio", "wifi", "on"])
            elif status == "off":
                subprocess.Popen(["nmcli", "radio", "wifi", "off"])
            else:
                print("Invalid status. Use 'on' or 'off'.")
        except Exception as e:
            print(f"Error: {e}")

    def change_bluetooth_connectivity(self, status):
        try:
            if status == "on":
                subprocess.Popen(["rfkill", "unblock", "bluetooth"])
            elif status == "off":
                subprocess.Popen(["rfkill", "block", "bluetooth"])
            else:
                print("Invalid status. Use 'on' or 'off'.")
        except Exception as e:
            print(f"Error: {e}")

    def increase_volume(self):
        try:
            subprocess.Popen(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
        except Exception as e:
            print(f"Error: {e}")

    def decrease_volume(self):
        try:
            subprocess.Popen(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
        except Exception as e:
            print(f"Error: {e}")

    def increase_brightness(self):
        try:
            subprocess.Popen(["xbacklight", "-inc", "10"])
        except Exception as e:
            print(f"Error: {e}")

    def decrease_brightness(self):
        try:
            subprocess.Popen(["xbacklight", "-dec", "10"])
        except Exception as e:
            print(f"Error: {e}")

    def play_music(self):
        try:
            self.spotify.start_playback()
        except Exception as e:
            print(f"Error: {e}")

    def pause_music(self):
        try:
            self.spotify.pause_playback()
        except Exception as e:
            print(f"Error: {e}")

    def next_track(self):
        try:
            self.spotify.next_track()
        except Exception as e:
            print(f"Error: {e}")

    def previous_track(self):
        try:
            self.spotify.previous_track()
        except Exception as e:
            print(f"Error: {e}")
    
    def open_folder(self, folder_path):
        try:
            subprocess.Popen(["xdg-open", folder_path])
        except Exception as e:
            print(f"Error: {e}")

    def close_folder(self):
        # There is no direct command to close a folder, as folders are managed by the file manager.
        # You can implement your own logic based on the file manager being used.
        print("Cannot close folder.")

    def open_file(self, file_path):
        try:
            subprocess.Popen(["xdg-open", file_path])
        except Exception as e:
            print(f"Error: {e}")

    def close_file(self):
        # There is no direct command to close a file, as files are opened by associated applications.
        # You can implement your own logic based on the associated application being used.
        print("Cannot close file.")

    def execute_terminal_command(self, command):
        try:
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
        except Exception as e:
            print(f"Error: {e}")

    def print_system_information(self):
        system_info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.architecture(),
            "CPU Cores": psutil.cpu_count(logical=False),
            "Total RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # in GB
            "Used RAM": round(psutil.virtual_memory().used / (1024 ** 3), 2),  # in GB
            "Disk Space": round(shutil.disk_usage("/").total / (1024 ** 3), 2),  # in GB
            "CPU Temperature": self.get_cpu_temperature()
        }
        for key, value in system_info.items():
            print(f"{key}: {value}")

    def get_cpu_temperature(self):
        try:
            process = subprocess.Popen(["sensors"], stdout=subprocess.PIPE)
            output, _ = process.communicate()
            temperature_info = output.decode("utf-8")
            cpu_temperature = temperature_info.split("Core 0: +")[1].split("°C")[0].strip()
            return cpu_temperature
        except Exception as e:
            print(f"Error: {e}")
            return "N/A"

    def open_task_manager(self):
        try:
            subprocess.Popen(["gnome-system-monitor"])
        except Exception as e:
            print(f"Error: {e}")

    def close_task_manager(self):
        # There is no direct command to close task manager, as it is a system application.
        # You can implement your own logic based on the task manager being used.
        print("Cannot close Task Manager.")

    def kill_process(self, process_name):
        try:
            for process in psutil.process_iter(attrs=['pid', 'name']):
                if process.info['name'] == process_name:
                    os.kill(process.info['pid'], 9)
                    print(f"Process {process_name} killed successfully.")
                    return
            print(f"No process with name {process_name} found.")
        except Exception as e:
            print(f"Error: {e}")

    def take_screenshot(self):
        try:
            screenshot = ImageGrab.grab()
            temp_file = tempfile.mktemp(suffix=".png")
            screenshot.save(temp_file)
            print(f"Screenshot saved: {temp_file}")
        except Exception as e:
            print(f"Error: {e}")
        
    def execute_command(self, command):
        if self.is_awake:
            if command.startswith("open "):
                program_name = command[5:]
                self.open_program(program_name)
            elif command.startswith("close "):
                program_name = command[6:]
                self.close_program(program_name)
            elif command == "open browser":
                self.open_browser()
            elif command == "start editor":
                self.start_editor()
            elif command == "open firefox":
                self.open_firefox()
            elif command == "close browser":
                self.close_browser()
            elif command == "finish editor":
                self.finish_editor()
            elif command == "close calculator":
                self.close_calculator()
            elif command == "what time is it":
                return self.what_time_is_it()
            elif command == "what day is today":
                return self.what_day_is_today()
            elif command == "go to sleep":
                self.go_to_sleep()
            elif command == "sleep":
                self.sleep()
            elif command == "awake":
                self.awake()
            elif command == "wake up":
                self.wake_up()
            elif command.startswith("click "):
                icon_name = command[6:]
                self.click_icon(icon_name)
            elif command == "open libre office":
                self.open_libre_office()
            elif command == "close libre office":
                self.close_libre_office()
            elif command.startswith("write to libre office"):
                text = command[21:]
                self.write_to_libre_office(text)
            elif command == "save libre office":
                self.save_libre_office()
            elif command == "open outlook":
                self.open_outlook()
            elif command == "close outlook":
                self.close_outlook()
            elif command == "open gmail":
                self.open_gmail()
            elif command == "close gmail":
                self.close_gmail()
            elif command.startswith("send mail"):
                self.send_email(command[10:])
            elif command.startswith("click "):
                icon_name = command[6:]
                self.click_icon(icon_name)
            elif command == "switch wifi on":
                self.change_wifi_connectivity("on")
            elif command == "switch wifi off":
                self.change_wifi_connectivity("off")
            elif command == "switch bluetooth on":
                self.change_bluetooth_connectivity("on")
            elif command == "switch bluetooth off":
                self.change_bluetooth_connectivity("off")
            elif command == "increase brightness":
                self.increase_brightness()
            elif command == "decrease brightness":
                self.decrease_brightness()
            elif command == "increase volume":
                self.increase_volume()
            elif command == "decrease volume":
                self.decrease_volume()
            elif command == "play music":
                self.play_music()
            elif command == "pause music":
                self.pause_music()
            elif command == "next track":
                self.next_track()
            elif command == "previous track":
                self.previous_track()
            elif command.startswith("open folder "):
                folder_path = command[12:]
                self.open_folder(folder_path)
            elif command == "close folder":
                self.close_folder()
            elif command.startswith("open file "):
                file_path = command[10:]
                self.open_file(file_path)
            elif command == "close file":
                self.close_file()
            elif command.startswith("execute command "):
                terminal_command = command[16:]
                self.execute_terminal_command(terminal_command)
            elif command == "print system information":
                self.print_system_information()
            elif command == "open task manager":
                self.open_task_manager()
            elif command == "close task manager":
                self.close_task_manager()
            elif command.startswith("kill process "):
                process_name = command[13:]
                self.kill_process(process_name)
            elif command == "take screenshot":
                self.take_screenshot()
            else:
                print("Command not recognized")
        else:
            if command == "wake up":
                self.wake_up()
            else:
                print("I'm asleep. Say 'wake up' to activate me.")
