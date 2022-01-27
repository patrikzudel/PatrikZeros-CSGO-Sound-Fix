# PatrikZero's CS:GO Volume Fix

  Script that lowers volume when you die in CS:GO. Uses game state integration. Anti-cheat safe.

  #### This will not get you VAC banned 100%  as it does not hook into the game in any sort of way.

  ## Usage

  - Download from releases on the right side ->
  - Put "gamestate_integration_VolumeFix.cfg" into your "Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg"
  - Run the .exe
  - You can also change how much the volume gets lowered by changing the decimal in "volume.txt"

  ## How to autostart with Windows

  - Place the program folder where you will not delete it (e.g. C:/)
  - Create a shortcut of the executable
  - Press Win + R
  - Type "shell:startup"
  -  Place the shortcut in the "Startup" folder that opens up

  ## Reasonings

  Players play CS with dangerously high peak volumes because they want to hear steps correctly. The risk of hearing damage can be severely reduced if you limit your exposure by lowering your volume when you die. 

  Even if you think your volume doesn't hurt you trust me it might over a long period of time. It took me 9 years of playing to develop tinnitus and I was playing at a reasonable volume. *(Judged by multiple non-gamers and me)* 

  I am no expert but I suspect this is due to a build up of small periods of very high volume (Shooting, Flashes, Grenades, Bomb explosion, Dinks). When you spectate your teammates you get a multiple of the sound exposure you would normally get because on average you are going to have one duel and die, after that you don't need your full listening volume. 
  My limited testing so far showed that lowering volume after death can lower exposure by 50% even if you live most of the round because most of the fighting and loud noises happen late round. (Pro play)

  ## How it works

  Its simple, it lowers the volume when it detects a death and returns the volume when you get to freezetime. 
  This effectively means your volume will be low for everything (e.g. Deathmatch) except actual matches (competitive / casual) where there is freezetime.

  ## To be added

  - [ ] Flash volume reduction
  - [ ] Toggle for the app (On system tray)

  ## How to build to .exe

  - pip install pyinstaller
  - pyinstaller --onefile --noconsole --icon Icon.ico --name "PatrikZeros CSGO Sound Fix" main.py

## Sources

- In sources.txt
- Thanks to mdhedelund, Simon Brunning and Mark Hammond.
