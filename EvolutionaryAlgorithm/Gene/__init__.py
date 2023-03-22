from EvolutionaryAlgorithm.Assumptions import Assumptions


class Gene:
    binaryRepresentation: str
    decimalRepresentation: float

    def __init__(self, binary_representation: str) -> object:
        assumptions = Assumptions()
        self.binaryRepresentation = binary_representation
        self.decimalRepresentation = assumptions.minValue + int(self.binaryRepresentation, 2) * (
                assumptions.maxValue - assumptions.minValue) / (2 ** assumptions.bitsLength - 1)
