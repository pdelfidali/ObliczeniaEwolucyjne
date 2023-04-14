from typing import Callable

import Assumptions
from Gene import Gene


class Chromosome:
    x1: Gene
    x2: Gene

    def __init__(self, x1: Gene, x2: Gene):
        self.x1 = x1
        self.x2 = x2

    def get_goal_function_value(self):
        assumptions = Assumptions.Assumptions()
        return assumptions.goal_function(self.x1.decimalRepresentation, self.x2.decimalRepresentation)

    def __lt__(self, other):  # TODO: check if we wanna this way
        return self.get_goal_function_value() < other.get_goal_function_value()

    def __str__(self):
        return f'{self.x1.binaryRepresentation, self.x2.binaryRepresentation}'

    def as_decimal_pair(self):
        return self.x1.decimalRepresentation, self.x2.decimalRepresentation

    @staticmethod
    def generate_random_chromosome() -> 'Chromosome':
        x1 = Gene.generate_random_gene()
        x2 = Gene.generate_random_gene()
        return Chromosome(x1, x2)
