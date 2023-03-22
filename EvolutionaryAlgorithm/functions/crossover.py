import random

from EvolutionaryAlgorithm.Assumptions import Assumptions
from EvolutionaryAlgorithm.Chromosome import Chromosome
from EvolutionaryAlgorithm.Gene import Gene


def crossover_genes(gene1: Gene, gene2: Gene) -> (Gene, Gene):
    assumptions = Assumptions()
    if assumptions.crossover_probability >= random.random():
        new_gene1_binary, new_gene2_binary = assumptions.crossover_func(gene1.binaryRepresentation,
                                                                        gene2.binaryRepresentation)
        return Gene(new_gene1_binary), Gene(new_gene2_binary)
    else:
        return gene1, gene2


def crossover_chromosomes(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    new1_x1, new2_x1 = crossover_genes(chromosome1.x1, chromosome2.x1)
    new1_x2, new2_x2 = crossover_genes(chromosome1.x2, chromosome2.x2)
    new_chromosome_1 = Chromosome(new1_x1, new1_x2)
    new_chromosome_2 = Chromosome(new2_x1, new2_x2)
    return new_chromosome_1, new_chromosome_2
