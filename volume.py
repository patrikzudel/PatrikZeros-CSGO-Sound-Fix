from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

volFile = open("volume.txt", "r")
ivolume = volFile.readline()
volFile.close()

def lowVolume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "csgo.exe":
            volume.SetMasterVolume(float(ivolume), None)

def sLowVolume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "csgo.exe":
            volume.SetMasterVolume(float(0), None)

def highVolume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "csgo.exe":
            volume.SetMasterVolume(1, None)


if __name__ == "__main__":
    pass