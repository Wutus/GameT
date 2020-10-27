from GameTheory import GameTheory

class Nim(GameTheory):
    def __init__(self, stacks, terminus_win = True):
        self.stacks = list(stacks)
        self.org_stacks = list(stacks)
        terminuses = set([tuple([0] * len(stacks))])
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
    
    def legal_from(self, state):
        s = set()
        sl = list(state)
        for (i, it) in enumerate(state):
            for j in range(it):
                s.add(tuple(sl[:i] + [j] + sl[i+1:]))
        states = frozenset(s)
        return states

    def legal_to(self, state):
        s = set()
        sl = list(state)
        for (i, it) in enumerate(state):
            for j in range(it + 1, self.org_stacks[i] + 1):
                s.add(tuple(sl[:i] + [j] + sl[i+1:]))
        states = frozenset(s)
        return states