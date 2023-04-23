import random

from Assumptions import Assumptions
from Gene.RealRepresentationGene import RealRepresentationGene


def uniform_mutation(gene: RealRepresentationGene) -> RealRepresentationGene:
    assumptions = Assumptions()
    new_decimal = random.uniform(assumptions.minValue, assumptions.maxValue)
    return RealRepresentationGene(new_decimal)


def gaussian_mutation(gene: RealRepresentationGene) -> RealRepresentationGene:
    assumptions = Assumptions()
    min_v = assumptions.minValue
    max_v = assumptions.maxValue
    is_valid = False
    new_decimal = None
    while not is_valid:
        new_decimal = gene.decimalRepresentation + random.gauss()
        if min_v <= new_decimal <= max_v:
            is_valid = True

    return RealRepresentationGene(new_decimal)
