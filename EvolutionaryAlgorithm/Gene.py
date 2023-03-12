from Assumptions import Assumptions


class Gene:
    binaryRepresentation: str
    decimalRepresentation: float
    assumptions: Assumptions

    def __init__(self, binary_representation: str, assumptions: Assumptions):
        self.binaryRepresentation = binary_representation
        self.assumptions = assumptions
        self.decimalRepresentation = self.assumptions.minValue + int(self.binaryRepresentation, 2) * (
                self.assumptions.maxValue - self.assumptions.minValue) / (2 ** self.assumptions.bitsLength - 1)

