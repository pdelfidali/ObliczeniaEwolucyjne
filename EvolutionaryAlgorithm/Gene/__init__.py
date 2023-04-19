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

    def __eq__(self, other):
        if not isinstance(other, Gene):
            return False
        return self.binaryRepresentation == other.binaryRepresentation

    @staticmethod
    def generate_random_gene() -> 'Gene':
        assumptions = Assumptions.Assumptions()
        binary_representation = ''.join(random.choice(['0', '1']) for _ in range(assumptions.bitsLength))
        return Gene(binary_representation)

    @staticmethod
    def createFromDecimalValue(decimal: float) -> 'Gene':
        assumptions = Assumptions.Assumptions()
        # TODO: odtworzyc z przedzialu assumptions najblizsze reprezentacje dla podanego decimala
        # binary_representation = "????"
        # TODO zamiast tego mozna dodac konstruktor ktory przyjmie float
        # return Gene(binary_representation)
        return Gene("0101")
