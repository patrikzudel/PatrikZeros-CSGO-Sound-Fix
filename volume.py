import comtypes
from pycaw.pycaw import AudioUtilities, CLSID_MMDeviceEnumerator, IMMDeviceEnumerator, EDataFlow, ERole, IAudioSessionControl2, IAudioSessionManager2, AudioSession, ISimpleAudioVolume
import json

settingsFile = open("settings.txt", "r")
settings = json.loads(settingsFile.read().replace('\n', ''))
settingsFile.close()

# Edited pycaw to look through all active output devices' sessions not only the Default one
class EditAudioUtilities(AudioUtilities):
    @staticmethod
    def GetSpeakers():
        deviceEnumerator = comtypes.CoCreateInstance(
            CLSID_MMDeviceEnumerator,
            IMMDeviceEnumerator,
            comtypes.CLSCTX_INPROC_SERVER)
        speakers = deviceEnumerator.EnumAudioEndpoints(EDataFlow.eRender.value, 0x00000001) # ACTIVE_DEVICES = 0x00000001
        return speakers

    @staticmethod
    def GetAudioSessionManager(speaker):
        # win7+ only
        o = speaker.Activate(
            IAudioSessionManager2._iid_, comtypes.CLSCTX_ALL, None)
        mgr = o.QueryInterface(IAudioSessionManager2)
        return mgr

    @staticmethod
    def GetAllSessions(mgr):
        audio_sessions = []
        if mgr is None:
            return audio_sessions
        sessionEnumerator = mgr.GetSessionEnumerator()
        count = sessionEnumerator.GetCount()
        for i in range(count):
            ctl = sessionEnumerator.GetSession(i)
            if ctl is None:
                continue
            ctl2 = ctl.QueryInterface(IAudioSessionControl2)
            if ctl2 is not None:
                audio_session = AudioSession(ctl2)
                audio_sessions.append(audio_session)
        return audio_sessions


def changeVolume(vol : float):
    speakers = EditAudioUtilities.GetSpeakers()
    count = speakers.GetCount()
    for i in range(count):
        speaker = speakers.Item(i)
        mgr = EditAudioUtilities.GetAudioSessionManager(speaker)
        sessions = EditAudioUtilities.GetAllSessions(mgr)
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "csgo.exe":
                volume.SetMasterVolume(vol, None)


def deathVolume():
    changeVolume(float(settings['deathVolume']))


def bombVolume():
    changeVolume(float(settings['bombExplosionVolume']))


def flashVolume():
    changeVolume(float(settings['flashVolume']))


def highVolume():
    changeVolume(float(1))


if __name__ == "__main__":
    pass