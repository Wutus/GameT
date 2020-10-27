from GameTheory import GameTheory
import itertools

class ForceNim(GameTheory):
    def __init__(self, stacks, to_move, terminus_win = True):
        self.org_stacks = list(stacks)
        self.to_move = to_move
        terminuses = self._calc_terminuses(stacks, to_move)
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
    
    def _calc_terminuses(self, stacks, to_move):
        s = set()
        s.add(tuple([0] * len(stacks)))
        for itm in range(1, to_move):
            for comb in itertools.combinations(range(len(stacks)), itm):
                vals = [range(1, stacks[i] + 1) if i in comb else [0] for i in range(len(stacks))]
                prods = itertools.product(*vals)
                s.update(prods)
        return frozenset(s)

    def legal_from(self, state):
        s = set()
        sl = list(state)
        for comb in itertools.combinations(range(len(self.org_stacks)), self.to_move):
            vals = [range(0, state[i]) if i in comb else [state[i]] for i in range(len(self.org_stacks))]
            prods = itertools.product(*vals)
            s.update(prods)
        states = frozenset(s)
        return states

    def legal_to(self, state):
        s = set()
        sl = list(state)
        for comb in itertools.combinations(range(len(self.org_stacks)), self.to_move):
            vals = [range(state[i] + 1, self.org_stacks[i] + 1) if i in comb else [state[i]] for i in range(len(self.org_stacks))]
            prods = itertools.product(*vals)
            s.update(prods)
        states = frozenset(s)
        return states