import Assumptions
from Gene.RealRepresentationGene import RealRepresentationGene
from Gene.BinaryGene import BinaryGene


class Chromosome:
    x1: BinaryGene | RealRepresentationGene
    x2: BinaryGene | RealRepresentationGene

    def __init__(self, x1: BinaryGene | RealRepresentationGene, x2: BinaryGene | RealRepresentationGene):
        self.x1 = x1
        self.x2 = x2

    def get_goal_function_value(self):
        assumptions = Assumptions.Assumptions()
        return assumptions.goal_function(self.x1.decimalRepresentation, self.x2.decimalRepresentation)

    def __eq__(self, other):
        if not isinstance(other, Chromosome):
            return False
        return self.x1 == other.x1 and self.x2 == other.x2

    def __lt__(self, other):
        return self.get_goal_function_value() < other.get_goal_function_value()

    def __str__(self):
        return f'{self.x1.binaryRepresentation, self.x2.binaryRepresentation}'

    def as_decimal_pair(self):
        return self.x1.decimalRepresentation, self.x2.decimalRepresentation

    @staticmethod
    def generate_random_chromosome() -> 'Chromosome':
        assumptions = Assumptions.Assumptions()
        if assumptions.method == 'binary_representation':
            x1 = BinaryGene.generate_random_gene()
            x2 = BinaryGene.generate_random_gene()
        else:
            x1 = RealRepresentationGene.generate_random_gene()
            x2 = RealRepresentationGene.generate_random_gene()
        return Chromosome(x1, x2)
