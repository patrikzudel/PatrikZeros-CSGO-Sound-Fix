import map
import player
import volume

class GameStateManager:
    def __init__(self):
        self.gamestate = GameState()

class GameState:
    def __init__(self):
        self.map = map.Map()
        self.player = player.Player()
        self.round_phase = ''

    def update_round_phase(self, phase):
        self.round_phase = phase
        #print('Round phase: ' + phase)
        if phase == "freezetime":
            volume.highVolume()
            #print("Setting volume to high")

    def update_player_health(self, health):
        if self.player.state.health != health:
            self.player.state.health = health
            #print(self.player.state.health)
        if health == 0:
            volume.lowVolume()
            #print("Setting volume to low")