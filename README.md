![](Logo.png)

Program that lowers volume when you die and get flashed in CS:GO.  
**It aims to lower the chance of hearing damage by significantly reducing overall sound exposure.**  
Uses game state integration. Anti-cheat safe. 

  #### This will not get you VAC banned 100%  as it does not hook into the game in any sort of way.

  ## 📖 Usage
  - Download from [Releases](https://github.com/patrikzudel/PatrikZeros-CSGO-Sound-Fix/releases/)
  - Chrome / Windows defender might flag it as a dangerous file because it doesn't know what it is but don't worry, as it is open source you can compile the code for yourself if you don't trust the `.exe`!
  - Put `gamestate_integration_VolumeFix.cfg` into your `Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`
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

## ⚡ Features
- Adjustable volume reduction (settings.txt)
  - When you die
  - When you get flashed (High pitched flash noise)
  - When bomb explodes
  
- System tray icon which shows settings

- Easy way to autostart with Windows

## 📖 How it works

Its simple, it lowers the csgo.exe volume when it detects a death and returns the volume when you get to freezetime. 
This effectively means your volume will be low for everything (e.g. Deathmatch) except actual matches (competitive / casual) where there is freezetime. **It also mutes the game when you get flashed** so you don't hear the **horrible high pitched noise**. (It only mutes it for the same duration as the game does so no disadvantage)

It is **VAC safe** because it uses game state integration and it only changes the Windows sound mixer settings for CS. So it doesn't touch the game at all. Game state integration is the same thing Steelseries for example uses for their mice to change color when you kill someone etc.

  ## 💬 Reasonings
  Players play CS with dangerously high peak volumes because they want to hear steps correctly. The risk of hearing damage can be severely reduced if you limit your exposure by lowering your volume when you die. 

  Even if you think your volume doesn't hurt you trust me it might over a long period of time. It took me 9 years of playing to develop tinnitus and I was playing at a reasonable volume. *(Judged by multiple non-gamers and me)* 

  I am no expert but I suspect this is due to a build up of small periods of very high volume *(Shooting, Flashes, Grenades, Bomb explosion, Dinks)*. 

**When you spectate your teammates you get a multiple of the sound exposure you would normally get because on average you are going to have one duel and die, after that you don't need your full listening volume.**
My limited testing so far showed that lowering volume after death can lower exposure by 50% even if you live most of the round because most of the fighting and loud noises happen late round. *(Pro play)*

## 🍀 Supporters

**[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/patrikzero)**
> If you like this project and would like to support me, feel free to buy me a coffee! ☕☕☕

  ## 📋 To be added

  - [x] Flash volume reduction
  - [x] Bomb volume reduction
  - [x] Settings for flash volume reduction
  - [x] Easy way to start with Windows
  - [x] Fix antiviruses flagging it as a virus
  - [ ] Keyboard toggle to switch between High / Low volume
  - [ ] Dink (Helmet Headshot) volume reduction
  - [ ] Toggle for the app (On system tray)
  - [x] Support for multiple sound devices (CS:GO on a non-default audio output)
  - [ ] Linux support

  ## 📃 How to build to .exe
  - `pip install pyinstaller`
  - `pyinstaller --onefile --noconsole --icon Icon.ico --name "PatrikZeros CSGO Sound Fix" main.py`

## 📃 Sources
- In `sources.txt`
- Thanks to mdhedelund, Andre Miras, Simon Brunning and Mark Hammond.

---

💻❤🍲 by [Patrik Žúdel](https://twitter.com/PatrikZero)