import subprocess
import platform
import wikipedia
import tempfile
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyautogui
import shutil
import psutil

class Execution:

    # Browser:

    def open_browser(self):
        try:
            subprocess.Popen(["google-chrome"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_browser(self):
        try:
            subprocess.Popen(["pkill", "chrome"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def open_firefox(self):
        try:
            subprocess.Popen(["firefox"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_firefox(self):
        try:
            subprocess.Popen(["pkill", "firefox"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def start_writing(self):
        print("Starting writing...")  # Logic to start writing

    def finish_writing(self):
        print("Finishing writing...")  # Logic to finish writing

    # Editor:

    def open_editor(self):
        try:
            subprocess.Popen(["gedit"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_editor(self):
        try:
            subprocess.Popen(["pkill", "gedit"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def open_github(self):
        self.open_firefox()
        try:
            subprocess.Popen(["firefox", "https://github.com"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_github(self):
        self.close_firefox()

    def open_vscode(self):
        try:
            subprocess.Popen(["code"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_vscode(self):
        try:
            subprocess.Popen(["pkill", "code"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def save_vscode(self):
        try:
            pyautogui.hotkey('ctrl', 's')
        except Exception as e:
            self.error_message(e, 3)

    def open_libre_office(self):
        try:
            subprocess.Popen(["libreoffice"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_libre_office(self):
        try:
            subprocess.Popen(["pkill", "libreoffice"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def write_to_libre_office(self, text="Hello, World!"):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
                temp_file.write(text.encode('utf-8'))
                temp_file_path = temp_file.name
            subprocess.Popen(["libreoffice", "--writer", temp_file_path])
        except Exception as e:
            self.error_message(e, 3)

    def save_libre_office(self):
        try:
            subprocess.Popen(["libreoffice", "--writer", "--save"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    # Mailing:

    def start_writing_mail(self, subject, matter, to, attachment):
        print(f"Writing mail with subject: {subject}, matter: {matter}, to: {to}, attachment: {attachment}")

    def open_outlook(self):
        try:
            subprocess.Popen(["thunderbird"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_outlook(self):
        try:
            subprocess.Popen(["pkill", "thunderbird"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def open_gmail(self):
        self.open_browser()
        try:
            subprocess.Popen(["firefox", "https://mail.google.com"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_gmail(self):
        self.close_browser()

    # Network Config:

    def switch_wifi_on(self):
        try:
            subprocess.Popen(["nmcli", "radio", "wifi", "on"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def switch_wifi_off(self):
        try:
            subprocess.Popen(["nmcli", "radio", "wifi", "off"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def change_wifi_network(self, network_name):
        print(f"Changing wifi network to {network_name}")

    def switch_bluetooth_on(self):
        try:
            subprocess.Popen(["rfkill", "unblock", "bluetooth"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def switch_bluetooth_off(self):
        try:
            subprocess.Popen(["rfkill", "block", "bluetooth"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def change_bluetooth_device(self, device_name):
        print(f"Changing bluetooth device to {device_name}")

    # Scripts:

    def execute_terminal_command(self, command):
        try:
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", command])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def download_install_add_to_path(self, package_name):
        print(f"Downloading, installing {package_name}, and adding to path...")

    def minimize_window(self):
        try:
            pyautogui.hotkey('ctrl', 'm')
        except Exception as e:
            self.error_message(e, 3)

    def print_system_information(self):
        try:
            system_info = {
                "OS": platform.system(),
                "OS Version": platform.version(),
                "Architecture": platform.architecture(),
                "CPU Cores": os.cpu_count(),
                "Total RAM": round(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024. ** 3), 2),
                "Used RAM": round((os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') - os.sysconf('SC_AVPHYS_PAGES')) / (1024. ** 3), 2),
                "Disk Space": round(shutil.disk_usage("/").total / (1024 ** 3), 2),
                "CPU Temperature": self.get_cpu_temperature()
            }
            for key, value in system_info.items():
                print(f"{key}: {value}")
        except Exception as e:
            self.error_message(e, 3)

    def get_cpu_temperature(self):
        try:
            process = subprocess.Popen(["sensors"], stdout=subprocess.PIPE)
            output, _ = process.communicate()
            temperature_info = output.decode("utf-8")
            cpu_temperature = temperature_info.split("Core 0: +")[1].split("°C")[0].strip()
            return cpu_temperature
        except Exception as e:
            self.error_message(e, 3)
            return "N/A"

    # Processes:

    def open_task_manager(self):
        try:
            subprocess.Popen(["gnome-system-monitor"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_task_manager(self):
        print("Closing task manager...")  # Logic to close task manager

    def show_processes(self):
        print("Displaying running processes...")  # Logic to display processes

    def kill_process(self, process_name):
        try:
            for process in psutil.process_iter(attrs=['pid', 'name']):
                if process.info['name'] == process_name:
                    os.kill(process.info['pid'], 9)
                    print(f"Process {process_name} killed successfully.")
                    return
            print(f"No process with name {process_name} found.")
        except Exception as e:
            self.error_message(e, 3)

    def set_alerts_for_process_completion(self, process_name):
        print(f"Setting alerts for process {process_name} completion...")

    def trigger(self):
        print("Triggering...")  # Logic for trigger

    def stop(self):
        print("Stopping...")  # Logic for stopping

    # Wedges:

    def open_calculator(self):
        try:
            subprocess.Popen(["gnome-calculator"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_calculator(self):
        try:
            subprocess.Popen(["pkill", "gnome-calculator"])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def set_alarm(self):
        print("Setting alarm...")  # Logic for setting alarm

    def delete_alarm(self):
        print("Deleting alarm...")  # Logic for deleting alarm

    # Web Search:

    def web_search(self, query):
        try:
            result = wikipedia.summary(query)
            print(result)
        except Exception as e:
            self.error_message(e, 3)
            print("Error: Unable to fetch search results.")

    # Application:

    def play_music(self):
        try:
            self.spotify.start_playback()
        except Exception as e:
            self.error_message(e, 3)

    def play_playlist(self, playlist_name):
        print(f"Playing playlist: {playlist_name}")  # Logic for playing playlist

    def pause_music(self):
        try:
            self.spotify.pause_playback()
        except Exception as e:
            self.error_message(e, 3)

    def next_track(self):
        try:
            self.spotify.next_track()
        except Exception as e:
            self.error_message(e, 3)

    def previous_track(self):
        try:
            self.spotify.previous_track()
        except Exception as e:
            self.error_message(e, 3)

    # File Manager:

    def open_folder(self, folder_path):
        try:
            subprocess.Popen(["xdg-open", folder_path])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_folder(self):
        print("Closing folder...")  # Logic for closing folder

    def open_file(self, file_path):
        try:
            subprocess.Popen(["xdg-open", file_path])
        except FileNotFoundError as e:
            self.error_message(e, 3)

    def close_file(self):
        print("Closing file...")  # Logic for closing file

    # System Config:

    def increase_volume(self):
        try:
            pyautogui.hotkey('fn', 'f8')
        except Exception as e:
            self.error_message(e, 3)

    def decrease_volume(self):
        try:
            pyautogui.hotkey('fn', 'f7')
        except Exception as e:
            self.error_message(e, 3)

    def increase_brightness(self):
        try:
            pyautogui.hotkey('fn', 'f3')
        except Exception as e:
            self.error_message(e, 3)

    def decrease_brightness(self):
        try:
            pyautogui.hotkey('fn', 'f2')
        except Exception as e:
            self.error_message(e, 3)

    def mute_volume(self):
        try:
            pyautogui.hotkey('fn', 'f6')
        except Exception as e:
            self.error_message(e, 3)

    def take_screenshot(self):
        try:
            screenshot = pyautogui.screenshot()
            temp_file = tempfile.mktemp(suffix=".png")
            screenshot.save(temp_file)
            print(f"Screenshot saved: {temp_file}")
        except Exception as e:
            self.error_message(e, 3)

    def open_ml_icon(self):
        print("Opening machine learning application icon...")  # Logic for opening ML icon

    def error_message(self, error, mode=0):
        if mode == 3:
            print(f"Command called but not executed. Error: {error}")

# Voice Assistant:

    def go_to_sleep(self):
        print("Going to sleep...")  # Logic for going to sleep

    def sleep(self):
        print("Sleeping...")  # Logic for sleeping

    def wake_up(self):
        print("Waking up...")  # Logic for waking up

    def awake(self):
        print("Awake...")  # Logic for being awake

    def trigger(self):
        print("Triggering...")  # Logic for triggering

    def stop(self):
        print("Stopping...")  # Logic for stopping
