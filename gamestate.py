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
        self.round_bomb = ''
        self.alive = 1

    def update_round_phase(self, phase):
        self.round_phase = phase
        if phase == "freezetime":
            volume.highVolume()
            self.alive = 1

    def update_round_bomb(self, bomb):
        self.round_bomb = bomb
        if bomb == "exploded":
            volume.bombVolume()

    def update_player_health(self, health):
        if self.player.state.health != health:
            self.player.state.health = health
        if health == 0:
            self.alive = 0
            volume.deathVolume()

    def update_player_flashed(self, flashed):
        if self.player.state.flashed != flashed:
            if self.player.state.flashed < flashed:
                if flashed > 0:
                    volume.flashVolume()
            self.player.state.flashed = flashed
            if flashed < 200:
                if self.alive:
                    volume.highVolume()
                else:
                    volume.deathVolume()
