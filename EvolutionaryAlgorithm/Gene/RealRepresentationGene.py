import random

import Assumptions
from Gene import Gene


class RealRepresentationGene(Gene):
    decimalRepresentation: float

    def __init__(self, decimal_representation: float):
        self.decimalRepresentation = decimal_representation

    def __eq__(self, other):
        if not isinstance(other, RealRepresentationGene):
            return False
        return self.decimalRepresentation == other.decimalRepresentation

    @staticmethod
    def generate_random_gene() -> 'RealRepresentationGene':
        assumptions = Assumptions.Assumptions()
        decimal_representation = random.uniform(assumptions.minValue, assumptions.maxValue)
        return RealRepresentationGene(decimal_representation)