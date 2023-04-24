from Gene.BinaryGene import BinaryGene
from functions.real_representation_crossover import *


def crossover_genes(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    assumptions = Assumptions()
    if assumptions.crossover_probability >= random.random():
        new_gene1, new_gene2 = assumptions.crossover_func(gene1, gene2)
        return new_gene1, new_gene2
    else:
        return gene1, gene2


def is_chromosome_based_crossover(crossover_func):
    return crossover_func in [average_crossover, linear_crossover, blend_crossover_alpha, blend_crossover_alpha_beta]


def crossover_chromosomes(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    if is_chromosome_based_crossover(assumptions.crossover_func):
        return  assumptions.crossover_func(chromosome1, chromosome2)
    else:
        new1_x1, new2_x1 = crossover_genes(chromosome1.x1, chromosome2.x1)
        new1_x2, new2_x2 = crossover_genes(chromosome1.x2, chromosome2.x2)
        new_chromosome_1 = Chromosome(new1_x1, new1_x2)
        new_chromosome_2 = Chromosome(new2_x1, new2_x2)
        return new_chromosome_1, new_chromosome_2
