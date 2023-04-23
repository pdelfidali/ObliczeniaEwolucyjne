import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene
from Gene.BinaryGene import BinaryGene
from Gene.RealRepresentationGene import RealRepresentationGene


def crossover_genes(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    assumptions = Assumptions()
    print(assumptions.crossover_func.__name__)
    if assumptions.crossover_probability >= random.random():
        new_gene1, new_gene2 = assumptions.crossover_func(gene1, gene2)
        return new_gene1, new_gene2
    else:
        return gene1, gene2


def is_chromosome_based_crossover(name: str):
    return name in ['average_crossover', 'linear_crossover', 'blend_crossover_alpha', 'blend_crossover_alpha_beta']


def crossover_chromosomes(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    print( is_chromosome_based_crossover(assumptions.crossover_func.__name__))
    if is_chromosome_based_crossover(assumptions.crossover_func.__name__):
        new_chromosome_1, new_chromosome_2 = assumptions.crossover_func(chromosome1, chromosome2)
        return new_chromosome_1, new_chromosome_2
    else:
        new1_x1, new2_x1 = crossover_genes(chromosome1.x1, chromosome2.x1)
        new1_x2, new2_x2 = crossover_genes(chromosome1.x2, chromosome2.x2)
        new_chromosome_1 = Chromosome(new1_x1, new1_x2)
        new_chromosome_2 = Chromosome(new2_x1, new2_x2)
        return new_chromosome_1, new_chromosome_2
