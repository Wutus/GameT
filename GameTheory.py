from functools import reduce
from GameInstance import GameInstance
from enum import Enum

class Position(Enum):
    P = 1
    N = 0

class GameTheory:
    def __init__(self, terminuses, get_legal_moves_from, get_legal_moves_to, terminus_win = True):
        self.terminuses = terminuses
        self.terminus_win = terminus_win
        self.get_legal_moves_from = get_legal_moves_from
        self.get_legal_moves_to = get_legal_moves_to
        self.last_reach_ended_with = None

    def reach(self, state):
        if self.terminus_win:
            self.p_states = set(self.terminuses)
            self.new_p_states = set(self.terminuses)
            self.n_states = set()
            self.new_n_states = set()
            self._process_new_p(state)
        else:
            self.p_states = set()
            self.new_p_states = set()
            self.n_states = set(self.terminus_win)
            self.new_n_states = set(self.terminus_win)
            self._process_new_n(state)

    def re_reach(self, state):
        if self.last_reach_ended_with is None:
            return reach(self, state)
        else:
            if state in self.n_states:
                return Position.N
            elif state in self.p_states:
                return Position.P
            if self.last_reach_ended_with == Position.N:
                self._process_new_n(state)
            else:
                self._process_new_p(state)

    def get_instance(self, start_state):
        return GameInstance(self.terminuses, self.start_state, self.get_legal_moves_from, self.terminus_win)

    def _process_new_p(self, state):
        self.new_n_states = reduce(lambda a,x: a.union(x), {self.get_legal_moves_to(x) for x in self.new_p_states}, set())
        self.n_states.update(self.new_n_states)
        if state in self.new_n_states:
            self.last_reach_ended_with = Position.N
            return self.last_reach_ended_with
        self._process_new_n(state)

    def _process_new_n(self, state):
        potiential_new_p_states = set(reduce(lambda a,x: a.union(x), {self.get_legal_moves_to(x) for x in self.new_n_states}, set()))
        potiential_new_p_states.difference_update(self.n_states)
        potiential_new_p_states.difference_update(self.p_states)
        self.new_p_states = {x for x in potiential_new_p_states if potiential_new_p_states not in self.p_states and self.get_legal_moves_from(x).issubset(self.n_states)}
        self.p_states.update(self.new_p_states)
        if state in self.new_p_states:
            self.last_reach_ended_with = Position.P
            return self.last_reach_ended_with
        self._process_new_p(state)