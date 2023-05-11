import random

import Assumptions
from Gene import Gene


class BinaryGene(Gene):
    binaryRepresentation: str
    decimalRepresentation: float

    def __init__(self, binary_representation: str):
        assumptions = Assumptions.Assumptions()
        self.binaryRepresentation = binary_representation
        self.decimalRepresentation = assumptions.minValue + int(self.binaryRepresentation, 2) * (
                assumptions.maxValue - assumptions.minValue) / (2 ** assumptions.bitsLength - 1)

    def __eq__(self, other):
        if not isinstance(other, BinaryGene):
            return False
        return self.binaryRepresentation == other.binaryRepresentation

    @staticmethod
    def generate_random_gene() -> 'BinaryGene':
        assumptions = Assumptions.Assumptions()
        binary_representation = ''.join(random.choice(['0', '1']) for _ in range(assumptions.bitsLength))
        return BinaryGene(binary_representation)
