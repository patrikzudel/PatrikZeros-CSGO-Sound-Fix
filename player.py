class Player:
    def __init__(self):
        self.steamid = ''
        self.name = ''
        self.observer_slot = -1
        self.activity = ''
        self.state = State()
        self.weapons = {}   
        self.match_stats = MatchStats()

class State:
    def __init__(self):
        self.health = 0
        self.armor = 0
        self.helmet = False
        self.flashed = 0
        self.smoked = 0
        self.burning = 0
        self.money = 0
        self.round_kills = 0
        self.round_killhs = 0
        self.equip_value = 0

class MatchStats:
    def __init__(self):
        self.kills = 0
        self.assists = 0
        self.deaths = 0
        self.mvps = 0
        self.score = 0

