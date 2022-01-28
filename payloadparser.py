
class PayloadParser:
    def parse_payload(self, payload, gamestate_manager):
        change_flags = {}
        # Parse round information
        if 'round' in payload and 'phase' in payload['round']:
            roundchanged = False
            if payload['round']['phase'] != gamestate_manager.gamestate.round_phase:
                gamestate_manager.gamestate.update_round_phase(payload['round']['phase'])
                roundchanged = True
            if payload['round']['phase'] != 'live' and not roundchanged:
                return None

        if 'round' in payload and 'bomb' in payload['round']:
            if payload['round']['bomb'] != gamestate_manager.gamestate.round_bomb:
                gamestate_manager.gamestate.update_round_bomb(payload['round']['bomb'])

        # Parse map information
        if 'map' in payload:
            map_info = payload['map']
            if 'mode' in map_info:
                gamestate_manager.gamestate.map.mode = map_info['mode']
            if 'name' in map_info:
                gamestate_manager.gamestate.map.name = map_info['name']
            if 'phase' in map_info:
                gamestate_manager.gamestate.map.phase = map_info['phase']
            if 'round' in map_info:
                gamestate_manager.gamestate.map.round = map_info['round']
                
            if 'team_ct' in map_info:
                ct_info = map_info['team_ct']
                if 'score' in ct_info:
                    gamestate_manager.gamestate.map.team_ct.score = ct_info['score']
                if 'timeouts_remaining' in ct_info:
                    gamestate_manager.gamestate.map.team_ct.timeouts_remaining = ct_info['timeouts_remaining']
                if 'matches_won_this_series' in ct_info:
                    gamestate_manager.gamestate.map.team_ct.matches_won_this_series = ct_info['matches_won_this_series']

            if 'team_t' in map_info:
                t_info = map_info['team_t']
                if 'score' in t_info:
                    gamestate_manager.gamestate.map.team_t.score = t_info['score']
                if 'timeouts_remaining' in t_info:
                    gamestate_manager.gamestate.map.team_t.timeouts_remaining = t_info['timeouts_remaining']
                if 'matches_won_this_series' in t_info:
                    gamestate_manager.gamestate.map.team_t.matches_won_this_series = t_info['matches_won_this_series']

            if 'num_matches_to_win_series' in map_info:
                gamestate_manager.gamestate.map.num_matches_to_win_series = map_info['num_matches_to_win_series']
            if 'current_spectators' in map_info:
                gamestate_manager.gamestate.map.current_spectators = map_info['current_spectators']
            if 'souvenirs_total' in map_info:
                gamestate_manager.gamestate.map.souvenirs_total = map_info['souvenirs_total']

        # Parse player information
        if 'player' in payload:
            player_info = payload['player']
            if 'steamid' in player_info:
                gamestate_manager.gamestate.player.steamid = player_info['steamid']
            if 'name' in player_info:
                gamestate_manager.gamestate.player.name = player_info['name']
            if 'observer_slot' in player_info:
                gamestate_manager.gamestate.player.observer_slot = player_info['observer_slot']
            if 'activity' in player_info:
                gamestate_manager.gamestate.player.activity = player_info['activity']

            if 'state' in player_info:
                state_info = player_info['state']
                if 'health' in state_info:
                    health = int(state_info['health'])
                    if gamestate_manager.gamestate.player.state.health != health:
                        gamestate_manager.gamestate.update_player_health(health)
                    gamestate_manager.gamestate.player.state.health = state_info['health']
                if 'armor' in state_info:
                    gamestate_manager.gamestate.player.state.armor = state_info['armor']
                if 'helmet' in state_info:
                    gamestate_manager.gamestate.player.state.helmet = state_info['helmet']
                if 'flashed' in state_info:
                    flashed = int(state_info['flashed'])
                    if gamestate_manager.gamestate.player.state.flashed != flashed:
                        gamestate_manager.gamestate.update_player_flashed(flashed)
                    gamestate_manager.gamestate.player.state.flashed = state_info['flashed']
                if 'smoked' in state_info:
                    gamestate_manager.gamestate.player.state.smoked = state_info['smoked']
                if 'burning' in state_info:
                    gamestate_manager.gamestate.player.state.burning = state_info['burning']
                if 'money' in state_info:
                    gamestate_manager.gamestate.player.state.money = state_info['money']
                if 'round_kills' in state_info:
                    gamestate_manager.gamestate.player.state.money = state_info['round_kills']
                if 'round_killhs' in state_info:
                    gamestate_manager.gamestate.player.state.round_killhs = state_info['round_killhs']
                if 'equip_value' in state_info:
                    gamestate_manager.gamestate.player.state.equip_value = state_info['equip_value']

            if 'weapons' in player_info:
                gamestate_manager.gamestate.player.weapons = player_info['weapons']
                if player_info['weapons'] != gamestate_manager.gamestate.player.weapons:
                    gamestate_manager.gamestate.player.weapons = player_info['weapons']

            if 'match_stats' in player_info:
                match_stats = player_info['match_stats']
                if 'kills' in match_stats:
                    gamestate_manager.gamestate.player.match_stats.kills = match_stats['kills']
                if 'assists' in match_stats:
                    gamestate_manager.gamestate.player.match_stats.assists = match_stats['assists']
                if 'deaths' in match_stats:
                    gamestate_manager.gamestate.player.match_stats.deaths = match_stats['deaths']
                if 'mvps' in match_stats:
                    gamestate_manager.gamestate.player.match_stats.mvps = match_stats['mvps']
                if 'score' in match_stats:
                    gamestate_manager.gamestate.player.match_stats.score = match_stats['score']
