from GameTheory import GameTheory
import itertools

class ForceNim(GameTheory):
    def __init__(self, max_stack, stack_count, to_move, terminus_win = True):
        self.max_stack = max_stack
        self.stack_count = stack_count
        self.to_move = to_move
        terminuses = self._calc_terminuses(max_stack, stack_count, to_move)
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
    
    def _calc_terminuses(self, max_stack, stack_count, to_move):
        vals = [[0]] * (stack_count - to_move) + [range(max_stack)] * to_move
        prods = itertools.product(*vals)
        prods_sorted = [tuple(sorted(x)) for x in prods]
        return frozenset(prods_sorted)

    def legal_from(self, state):
        s = set()
        sl = list(state)
        for comb in itertools.combinations(range(self.stack_count), self.to_move):
            vals = [range(0, state[i]) if i in comb else [state[i]] for i in range(self.stack_count)]
            prods = itertools.product(*vals)
            prods_sorted = [tuple(sorted(x)) for x in prods]
            s.update(prods_sorted)
        states = frozenset(s)
        return states

    def legal_to(self, state):
        s = set()
        sl = list(state)
        for comb in itertools.combinations(range(self.stack_count), self.to_move):
            vals = [range(state[i] + 1, self.max_stack + 1) if i in comb else [state[i]] for i in range(self.stack_count)]
            prods = itertools.product(*vals)
            prods_sorted = [tuple(sorted(x)) for x in prods]
            s.update(prods_sorted)
        states = frozenset(s)
        return states