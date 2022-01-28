from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import payloadparser
import gamestate
import provider
import itertools, glob
import threading
import os

from SysTrayIcon import SysTrayIcon

class GSIServer(HTTPServer):
    def __init__(self, server_address, token, RequestHandler):
        self.provider = provider.Provider()
        self.auth_token = token
        self.gamestatemanager = gamestate.GameStateManager()

        super(GSIServer, self).__init__(server_address, RequestHandler)

     #   self.setup_log_file()
        self.payload_parser = payloadparser.PayloadParser()

   # def setup_log_file(self):
    #    self.log_file = logger.LogFile(time.asctime())

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length).decode('utf-8')

        payload = json.loads(body)
        # Ignore unauthenticated payloads
        if not self.authenticate_payload(payload):
            return None

        self.server.payload_parser.parse_payload(payload, self.server.gamestatemanager)

        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()

    def authenticate_payload(self, payload):
        if 'auth' in payload and 'token' in payload['auth']:
            return payload['auth']['token'] == server.auth_token
        else:
            return False

    def get_round_phase(self, payload):
        if 'round' in payload and 'phase' in payload['round']:
            return payload['round']['phase']
        else:
            return None

    def get_kill(self, payload):
        if 'player' in payload and 'state' in payload['player'] and 'rounds_kills' in payload['player']['state']:
                return payload['player']['rounds_kills']
        else:
            return None

    def get_state(self, payload):
        return payload

    def log_message(self, format, *args):
        """
        Prevents requests from printing into the console
        """
        return



def SysTrayIconCreate():
    settingsFile = open("settings.txt", "r")
    settings = json.loads(settingsFile.read().replace('\n', ''))
    settingsFile.close()
    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "Zero's CSGO Volume Fix"
    def nameroni(sysTrayIcon): pass
    def toggleFunc(sysTrayIcon): pass
    def switch_icon(sysTrayIcon):
        sysTrayIcon.icon = next(icons)
        sysTrayIcon.refresh_icon()
    menu_options = (("PatrikZero's CSGO Volume Fix", next(icons), nameroni), (f"Death volume: {float(settings['deathVolume'])*100}%", None, nameroni), (f"Flash volume: {float(settings['flashVolume'])*100}%", None, nameroni), (f"Bomb expl. volume: {float(settings['bombExplosionVolume'])*100}%", None, nameroni))
    def quitteroni(sysTrayIcon): os._exit(1)
    SysTrayIcon(next(icons), hover_text, menu_options, on_quit=quitteroni, default_menu_index=1)


thSysTray = threading.Thread(target=SysTrayIconCreate)
thSysTray.start()

server = GSIServer(('localhost', 3202), 'VALVEPLSSPAREMYEARS', RequestHandler)

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    pass

server.server_close()