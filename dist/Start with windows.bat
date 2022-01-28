@echo off

setlocal
:PROMPT
SET /P AREYOUSURE=Have you put the folder somewhere where you will not delete it (C:/ or Documents) (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Start Menu\Programs\Startup\PatrikZeros CSGO Sound Fix.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%cd%\PatrikZeros CSGO Sound Fix.exe" >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%

:END
endlocal