from GameTheory import GameTheory
import itertools

class SubstractLimited(GameTheory):
    def __init__(self, limit_list, terminus_win = True):
        self.limit_list = limit_list
        ranges = [range(i+1) for i in limit_list]
        terminuses = set(itertools.product([0],*ranges))
        terminuses.update(itertools.product([1],[0],range(5),range(5),range(5),range(5),range(5)))
        terminuses.update(itertools.product([2],[0],[0],range(5),range(5),range(5),range(5)))
        terminuses.update(itertools.product([3],[0],[0],[0],range(5),range(5),range(5)))
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
    
    def legal_from(self, state):
        state_list = list(state)
        states = frozenset([tuple([state_list[0] - i] + state_list[1:i] + [state_list[i] - 1] + state_list[i:7]) for i in range(1, min(6,state[0]) + 1) if state[i] > 0])
        return states

    def legal_to(self, state):
        state_list = list(state)
        states = frozenset([tuple([state_list[0] + i] + state_list[1:i] + [state_list[i] + 1] + state_list[i:7]) for i in range(1, 7) if state[i] < 4])
        return states