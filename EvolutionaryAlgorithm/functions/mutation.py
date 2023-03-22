import random

from EvolutionaryAlgorithm.Assumptions import Assumptions
from EvolutionaryAlgorithm.Chromosome import Chromosome
from EvolutionaryAlgorithm.Gene import Gene


def mutate_gene(gene: Gene):
    assumptions = Assumptions()
    if random.random() <= assumptions.mutation_probability:
        bits = assumptions.mutation_func(gene.binaryRepresentation)
        return Gene(bits)
    else:
        return gene


def mutate_chromosome(chromosome: Chromosome):
    x1 = mutate_gene(chromosome.x1)
    x2 = mutate_gene(chromosome.x2)
    return x1, x2
