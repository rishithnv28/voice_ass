#!/bin/bash

# Update package list
sudo apt update

# Install necessary packages and libraries
sudo apt install -y \
    firefox \
    libreoffice \
    thunderbird \
    gnome-terminal \
    gnome-system-monitor \
    python3 \
    python3-pip \
    python3-dev \
    libatk-adaptor \
    libcanberra-gtk-module \
    default-jre \
    pulseaudio \
    pavucontrol \
    xdotool \
    wmctrl \
    alsa-utils \
    xbacklight \
    git \
    curl \
    vim

# Install Python libraries
pip3 install pyautogui

# Additional installations and configurations specific to your use case
# ...

echo "Installation complete."
