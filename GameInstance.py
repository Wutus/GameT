class GameInstance:
    def __init__(self, terminuses, start_state, get_legal_moves_from, terminus_win = True):
        self.terminuses = terminuses
        self.start_state = start_state
        self.current_state = start_state
        self.current_player = 0
        self.winner = 0
        self.terminus_win = terminus_win
        self.get_legal_moves_from = get_legal_moves_from

    def make_move(self, new_state):
        if new_state not in self.get_legal_moves_from(self.current_state):
            return False
        if new_state in self.terminuses:
            self.winner = self.current_player if self.terminus_win else 1 - self.current_player
        else:
            self.current_player = 1 - self.current_player
        self.current_state = new_state
        return True