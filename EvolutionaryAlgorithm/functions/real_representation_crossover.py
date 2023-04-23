import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene.RealRepresentationGene import RealRepresentationGene


def arithmetic_crossover(gene1: RealRepresentationGene, gene2: RealRepresentationGene) -> (
        RealRepresentationGene, RealRepresentationGene):
    assumptions = Assumptions()
    k = random.random()
    dec1 = gene1.decimalRepresentation
    dec2 = gene2.decimalRepresentation

    is_valid = False
    crossed_decs1, crossed_decs2 = None, None

    while not (assumptions.in_bounds(crossed_decs1) and assumptions.in_bounds(crossed_decs2)):
        crossed_decs1 = k * dec1 + (1 - k) * dec2
        crossed_decs2 = (1 - k) * dec1 + k * dec2

    return RealRepresentationGene(crossed_decs1), RealRepresentationGene(crossed_decs2)


# TODO: * this uses Chromosomes for crossover instead of genes (bcs it neads x1 and x2 of both simultanously)
#       * to address this we may want to do one of the following
#           - change the way the wrapper crossover chromosomes work and just use this function in case of assumption flag
def linear_crossover(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    mode = assumptions.optimization_mode

    gene_x1_z = RealRepresentationGene(
        chromosome1.x1.decimalRepresentation / 2 + chromosome2.x1.decimalRepresentation / 2)
    gene_x2_z = RealRepresentationGene(
        chromosome1.x2.decimalRepresentation / 2 + chromosome2.x2.decimalRepresentation / 2)
    chromosome_z = Chromosome(gene_x1_z, gene_x2_z)

    gene_x1_v = RealRepresentationGene(
        chromosome1.x1.decimalRepresentation * 3 / 2 - chromosome2.x1.decimalRepresentation / 2)
    gene_x2_v = RealRepresentationGene(
        chromosome1.x2.decimalRepresentation * 3 / 2 - chromosome2.x2.decimalRepresentation / 2)
    chromosome_v = Chromosome(gene_x1_v, gene_x2_v)

    gene_x1_w = RealRepresentationGene(
        -chromosome1.x1.decimalRepresentation / 2 + chromosome2.x1.decimalRepresentation * 3 / 2)
    gene_x2_w = RealRepresentationGene(
        -chromosome1.x2.decimalRepresentation / 2 + chromosome2.x2.decimalRepresentation * 3 / 2)
    chromosome_w = Chromosome(gene_x1_w, gene_x2_w)

    crossover_rank_selection = [chromosome_z, chromosome_v, chromosome_w]

    if mode == 'max':
        crossover_rank_selection.sort(reverse=True)
    else:
        crossover_rank_selection.sort(reverse=False)

    selected_children = crossover_rank_selection[:2]  # TODO: should I unpack to match the function def?

    # return selected_children[0], selected_children[1]
    return selected_children


# TODO: this one gives just one offspring (kinda hard to fit in our algo, but may actually work since in the
#  population.py we generate children from crossover unless we have population size
def average_crossover(chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
    gene_x1 = RealRepresentationGene(
        (chromosome1.x1.decimalRepresentation + chromosome2.x1.decimalRepresentation) / 2)
    gene_x2 = RealRepresentationGene(
        (chromosome1.x2.decimalRepresentation + chromosome2.x2.decimalRepresentation) / 2)
    chromosome = Chromosome(gene_x1, gene_x2)
    return chromosome


def generate_blend_gene(blend_ratio_alpha, blend_ratio_beta, gene_decimal_rep_1, gene_decimal_rep_2):
    lower_bound = min(gene_decimal_rep_1, gene_decimal_rep_2)
    upper_bound = max(gene_decimal_rep_1, gene_decimal_rep_2)

    # calculate the range for the gene value
    gene_range = upper_bound - lower_bound  # dx_i

    # calculate the lower and upper bounds for the gene value in the child chromosome
    gene_lower_bound = lower_bound - blend_ratio_alpha * gene_range
    gene_upper_bound = upper_bound + blend_ratio_beta * gene_range

    # generate a new gene value for the child chromosome
    new_gene_value = random.uniform(gene_lower_bound, gene_upper_bound)
    return RealRepresentationGene(new_gene_value)


def generate_blend_chromosme(alpha, beta, chromosome1, chromosome2):
    new_chromosome1 = Chromosome(generate_blend_gene(alpha, beta, chromosome1.x1.decimalRepresentation,
                                                     chromosome2.x1.decimalRepresentation),
                                 generate_blend_gene(alpha, beta, chromosome1.x2.decimalRepresentation,
                                                     chromosome2.x2.decimalRepresentation)

                                 )

    new_chromosome2 = Chromosome(
        generate_blend_gene(alpha, beta, chromosome1.x1.decimalRepresentation,
                            chromosome2.x1.decimalRepresentation),
        generate_blend_gene(alpha, beta, chromosome1.x2.decimalRepresentation, chromosome2.x2.decimalRepresentation)
    )
    return new_chromosome1, new_chromosome2


# TODO: same as linear_crossover
def blend_crossover_alpha(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    #  TODO: do we want to randomly gen alpha or provide
    alpha = random.random()

    new_chromosome1, new_chromosome2 = generate_blend_chromosme(alpha, alpha, chromosome1, chromosome2)
    return new_chromosome1, new_chromosome2


def blend_crossover_alpha_beta(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    new_chromosome1, new_chromosome2 = None, None
    is_valid = False

    while not is_valid:
        #  TODO: do we want to randomly gen alpha and beta or provide
        alpha, beta = random.random(), random.random()
        new_chromosome1, new_chromosome2 = generate_blend_chromosme(alpha, beta, chromosome1, chromosome2)
        is_valid = all(
            [assumptions.in_bounds(new_chromosome1.x1.decimalRepresentation),
             assumptions.in_bounds(new_chromosome1.x2.decimalRepresentation),
             assumptions.in_bounds(new_chromosome2.x1.decimalRepresentation),
             assumptions.in_bounds(new_chromosome2.x2.decimalRepresentation)]
        )
    return new_chromosome1, new_chromosome2
