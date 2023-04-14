from typing import Callable

from EvolutionaryAlgorithm.Assumptions import Assumptions
from EvolutionaryAlgorithm.Gene import Gene


class Chromosome:
    x1: Gene
    x2: Gene

    def __init__(self, x1: Gene, x2: Gene,):
        self.x1 = x1
        self.x2 = x2

    def get_goal_function_value(self):
        assumptions = Assumptions()
        return assumptions.goal_function(self.x1.decimalRepresentation, self.x2.decimalRepresentation)

    def __lt__(self, other): # TODO: check if we wanna this way
        return self.get_goal_function_value() < other.get_goal_function_value()
