<img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/LogoLight.png?sanitize=true#gh-dark-mode-only" alt="Logo"><img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/LogoDark.png?sanitize=true#gh-light-mode-only" alt="Logo">

<a href="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/FaceitVerified.png">
<img src="https://raw.githubusercontent.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/main/Logos/FaceitVerified.png?sanitize=true#gh-light-mode-only" alt="Logo" width="150px" style="float: left"></a>

Program that lowers volume when you are not alive and get flashed in CS:GO.  
**It aims to lower the chance of hearing damage and fatigue by significantly reducing overall sound exposure.**  
Uses game state integration. Anti-cheat safe. 

  #### This will not get you VAC banned 100%  as it does not hook into the game in any sort of way.

  ## 📖 How to use
  - Download from [Releases](https://github.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/releases/)
  - Chrome / Windows defender might flag it as a dangerous file because it doesn't know what it is but don't worry, as it is open source you can compile the code for yourself if you don't trust the `.exe`!
	- CS2 - Put `gamestate_integration_VolumeFix.cfg` into your `Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg`
      - MAKE SURE TO PUT IT IN THE \game\csgo\cfg 
    - CS:GO - Put `gamestate_integration_VolumeFix.cfg` into your `Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`
  - Run the .exe
    - You can also change settings in `settings.txt`. If you want to disable a feature just put the value to `1.00`. 
    - For example `"flashVolume": 1.00` would not change the game volume when flashed. `"flashVolume": 0.30` will set the volume to 30% when flashed.
  - To turn it off just right click the icon in the system tray and `Quit`.
    - Right clicking the system tray icon also shows current settings.


  ## 🎯 How to autostart with Windows
### This is really simple and recommended!

  - **Place the main folder where you will not delete it (e.g. `C:/` or `Documents`)**
  - Open `Start with windows.bat`
  - Its done!
    - To remove it from autostart visit [here](https://github.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/wiki/%F0%9F%92%BE-How-to-remove-from-Windows-autostart)


## ⚡ Features
- Adjustable volume reduction (settings.txt)
  - When you die
  - When you get flashed (High pitched flash noise)
  - When bomb explodes
  
- System tray icon which shows settings

- Easy way to autostart with Windows

## 📖 How it works

Its simple, it lowers the csgo.exe/cs2.exe volume when it detects a death and returns the volume when you get to freezetime. 
This effectively means your volume will be low for everything (e.g. Deathmatch) except actual matches (competitive / casual) where there is freezetime. **It also mutes the game when you get flashed** so you don't hear the **horrible high pitched noise**. (It only mutes it for the same duration as the game does so no disadvantage)

It is **VAC safe** because it uses game state integration and it only changes the Windows sound mixer settings for CS. So it doesn't touch the game at all. Game state integration is the same thing Steelseries for example uses for their mice to change color when you kill someone etc.

  ## 💬 Reasonings
  Players play CS with dangerously high peak volumes because they want to hear steps correctly. The risk of hearing damage can be severely reduced if you limit your exposure by lowering your volume when you die. 

  Even if you think your volume doesn't hurt you trust me it might over a long period of time. It took me 9 years of playing to develop tinnitus and I was playing at a reasonable volume. *(Judged by multiple non-gamers and me)* 

  I am no expert but I suspect this is due to a build up of small periods of very high volume *(Shooting, Flashes, Grenades, Bomb explosion, Dinks)*. 

**When you spectate your teammates you get a multiple of the sound exposure you would normally get because on average you are going to have one duel and die, after that you don't need your full listening volume.**
My limited testing so far showed that lowering volume after death can lower exposure by 50% even if you live most of the round because most of the fighting and loud noises happen late round. *(Pro play)*

## 🍀 Supporters

**[!["Buy Me A Ramen"](https://raw.githubusercontent.com/patrikzudel/patrikzudel/main/ramen.png)](https://www.buymeacoffee.com/patrikzero)**

> If you like this project and would like to support me, feel free to buy me a ramen! 🍜🍜🍜

  ## 📋 To be added

  - [ ] Better flash volume reduction (That doesn't give a competitive disadvantage)
  - [ ] Keyboard toggle to switch back to High volume
  - [ ] Dink (Helmet Headshot) volume reduction
  - [ ] Linux support
  - [x] Flash volume reduction
  - [x] Bomb volume reduction
  - [x] Settings for flash volume reduction
  - [x] Easy way to start with Windows
  - [x] Fix antiviruses flagging it as a virus
  - [x] Support for multiple sound devices (CS:GO on a non-default audio output)

  ## 📃 How to build to .exe
  - `pip install pyinstaller`
  - `pyinstaller --onefile --noconsole --icon Icon.ico --name "PatrikZeros_CS_Sound_Fix" main.py`
- `pyinstaller --onefile --noconsole --icon settings.ico --name "Settings" Settings.py`

## 📃 Sources
- In `sources.txt`
- Thanks to mdhedelund, Andre Miras, Simon Brunning and Mark Hammond.

---

💻❤🍲 by [Patrik Žúdel](https://twitter.com/PatrikZero)
