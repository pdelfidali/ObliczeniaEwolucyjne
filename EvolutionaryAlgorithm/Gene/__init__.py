import Assumptions
import random


class Gene:
    binaryRepresentation: str
    decimalRepresentation: float

    def __init__(self, binary_representation: str) -> object:
        assumptions = Assumptions.Assumptions()
        self.binaryRepresentation = binary_representation
        self.decimalRepresentation = assumptions.minValue + int(self.binaryRepresentation, 2) * (
                assumptions.maxValue - assumptions.minValue) / (2 ** assumptions.bitsLength - 1)

    @staticmethod
    def generate_random_gene() -> 'Gene':
        assumptions = Assumptions.Assumptions()
        binary_representation = ''.join(random.choice(['0', '1']) for _ in range(assumptions.bitsLength))
        return Gene(binary_representation)
