from GameTheory import GameTheory

class Substract(GameTheory):
    def __init__(self, allowed_set, terminus_win = True):
        self.allowed_set = allowed_set
        terminuses = set(range(min(allowed_set)))
        super().__init__(terminuses, self.legal_from, self.legal_to, terminus_win)
    
    def legal_from(self, number):
        return frozenset({number - x for x in self.allowed_set if number - x >= 0})

    def legal_to(self, number):
        return frozenset({number + x for x in self.allowed_set})