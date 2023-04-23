import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene
from Gene.BinaryGene import BinaryGene
from Gene.RealRepresentationGene import RealRepresentationGene


def crossover_genes(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    assumptions = Assumptions()
    if assumptions.crossover_probability >= random.random():
        new_gene1, new_gene2 = assumptions.crossover_func(gene1, gene2)
        return new_gene1, new_gene2
    else:
        return gene1, gene2


def crossover_chromosomes(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    new1_x1, new2_x1 = crossover_genes(chromosome1.x1, chromosome2.x1)
    new1_x2, new2_x2 = crossover_genes(chromosome1.x2, chromosome2.x2)
    new_chromosome_1 = Chromosome(new1_x1, new1_x2)
    new_chromosome_2 = Chromosome(new2_x1, new2_x2)
    return new_chromosome_1, new_chromosome_2
