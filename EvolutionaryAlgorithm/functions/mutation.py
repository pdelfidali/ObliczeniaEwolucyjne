import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene


def mutate_gene(gene: Gene) -> Gene:
    assumptions = Assumptions()
    if random.random() <= assumptions.mutation_probability:
        bits = assumptions.mutation_func(gene.binaryRepresentation)
        return Gene(bits)
    else:
        return gene


def mutate_chromosome(chromosome: Chromosome) -> Chromosome:
    x1 = mutate_gene(chromosome.x1)
    x2 = mutate_gene(chromosome.x2)
    return Chromosome(x1, x2)
