<img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/LogoLight.png?sanitize=true#gh-dark-mode-only" alt="Logo"><img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/LogoDark.png?sanitize=true#gh-light-mode-only" alt="Logo">

<a href="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/FaceitVerified.png">
<img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/FaceitVerified.png?sanitize=true#gh-light-mode-only" alt="Logo" width="150px" style="float: left"></a>

This is a Linux fork of the program that lowers volume when you are not alive and get flashed in CS:GO.  
**It aims to lower the chance of hearing damage and fatigue by significantly reducing overall sound exposure.**  
Uses game state integration. Anti-cheat safe. 

#### This will not get you VAC banned 100% as it does not hook into the game in any sort of way.

## 📖 Linux Specific Setup
For the basic setup, please refer to the original [README](https://github.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/blob/main/README.md). Once you have completed the basic setup, follow these Linux-specific steps:

1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the main script: `python main.py`
3. To edit the settings, run `python ui_settings.py` or modify the settings.txt file directly

### 🐧 Autostart on Linux
To have the script start automatically when you log in, follow these steps:

1. Create a new file called `csgo-sound-fix.desktop` in `~/.config/autostart/`.
2. Open the file in a text editor and paste the following:

`
[Desktop Entry]
Type=Application
Exec=python /path/to/main.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=CSGO Sound Fix
Name=CSGO Sound Fix
Comment[en_US]=Automatically start CSGO Sound Fix on login
Comment=Automatically start CSGO Sound Fix on login

`

3. Replace `/path/to/main.py` with the actual path to the `main.py` file in your project folder.
4. Save the file and restart your system. The script should now start automatically when you log in.

PLEASE NOTE AUTOSTART CAN BE DIFFERENT DEPENDING ON YOUR DISTRO!