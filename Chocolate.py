from GameTheory import GameTheory
from functools import reduce

class Chocolate(GameTheory):
    def __init__(self, height, width, terminus_win = False):
        terminuses = {tuple([0]*height)}
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
        self.height = height
        self.width = width
    
    def get_start_state(self):
        return tuple([self.width]*self.height)

    def legal_from(self, state):
        allowed_points = reduce(lambda a,x: a + x, [[(x + 1, yi) for yi in range(1, y+1)] for (x, y) in enumerate(state)], [])
        states = frozenset({tuple([s if i + 1 < x else min(s, y) for (i,s) in enumerate(state)]) for (x,y) in allowed_points})
        return states

    def legal_to(self, state):
        states = frozenset(reduce(lambda a,x : a + x,
            [
                [
                    tuple([
                        yi if si == i else s for (si, s) in enumerate(state)
                    ]) for yi in (range(y + 1, self.width + 1) if i == 0 else range(y + 1, state[i - 1] + 1))
                ] for (i,y) in enumerate(state)
            ],
            []))
        return states
