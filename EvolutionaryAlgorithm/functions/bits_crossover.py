import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene


def homogeneous_crossover(bits1: str, bits2: str, crossover_prob: float = 0.5) -> (str, str):
    crossed_bits1 = ''
    crossed_bits2 = ''
    for n in range(len(bits1)):
        if random.random() <= crossover_prob:
            crossed_bits1 += bits2[n]
            crossed_bits2 += bits1[n]
        else:
            crossed_bits1 += bits1[n]
            crossed_bits2 += bits2[n]
    return crossed_bits1, crossed_bits2


def one_point_crossover(gene1: Gene, gene2: Gene) -> (Gene, Gene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split = random.randint(1, len(bits1) - 1)
    crossed_bits1 = bits1[:n_split] + bits2[n_split:]
    crossed_bits2 = bits2[:n_split] + bits1[n_split:]
    return Gene(crossed_bits1), Gene(crossed_bits2)


def two_point_crossover(gene1: Gene, gene2: Gene) -> (Gene, Gene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split1, n_split2 = sorted(random.sample(range(1, len(bits1) - 1), 2))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:]
    return Gene(crossed_bits1), Gene(crossed_bits2)


def three_point_crossover(gene1: Gene, gene2: Gene) -> (Gene, Gene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split1, n_split2, n_split3 = sorted(random.sample(range(1, len(bits1) - 1), 3))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:n_split3] + bits2[n_split3:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:n_split3] + bits1[n_split3:]
    return Gene(crossed_bits1), Gene(crossed_bits2)


def arithmetic_crossover(gene1: Gene, gene2: Gene) -> (Gene, Gene):
    assumptions = Assumptions()
    k = random.random()
    dec1 = gene1.decimalRepresentation
    dec2 = gene2.decimalRepresentation

    is_valid = False
    crossed_decs1, crossed_decs2 = None, None

    while not is_valid:
        crossed_decs1 = k * dec1 + (1 - k) * dec2
        crossed_decs2 = (1 - k) * dec1 + k * dec2

        if assumptions.in_bounds(crossed_decs1) and assumptions.in_bounds(crossed_decs2):
            is_valid = True

            # 1) Pamiętajmy, że po procesie krzyżowania nasze
            # geny dalej muszą mieścić się w przedziałach – jeśli
            # tak nie jest musimy ponowić proces - TO CHYBA NIE BYLO DO TEGO ALE PRZYPADKIEM ZAIMPLEMENTOWALEM

    return Gene.createFromDecimalValue(crossed_decs1), Gene.createFromDecimalValue(crossed_decs2)  # TODO: do this


# TODO: * this uses Chromosomes for crossover instead of genes (bcs it neads x1 and x2 of both simultanously)
#       * to address this we may want to do one of the following
#           - change the way the wrapper crossover chromosomes work and just use this function in case of assumption flag
def linear_crossover(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    mode = assumptions.optimization_mode

    gene_x1_z = Gene.createFromDecimalValue(
        chromosome1.x1.decimalRepresentation / 2 + chromosome2.x1.decimalRepresentation / 2)
    gene_x2_z = Gene.createFromDecimalValue(
        chromosome1.x2.decimalRepresentation / 2 + chromosome2.x2.decimalRepresentation / 2)
    chromosome_z = Chromosome(gene_x1_z, gene_x2_z)

    gene_x1_v = Gene.createFromDecimalValue(
        chromosome1.x1.decimalRepresentation * 3 / 2 - chromosome2.x1.decimalRepresentation / 2)
    gene_x2_v = Gene.createFromDecimalValue(
        chromosome1.x2.decimalRepresentation * 3 / 2 - chromosome2.x2.decimalRepresentation / 2)
    chromosome_v = Chromosome(gene_x1_v, gene_x2_v)

    gene_x1_w = Gene.createFromDecimalValue(
        -chromosome1.x1.decimalRepresentation / 2 + chromosome2.x1.decimalRepresentation * 3 / 2)
    gene_x2_w = Gene.createFromDecimalValue(
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
    gene_x1 = Gene.createFromDecimalValue(
        (chromosome1.x1.decimalRepresentation + chromosome2.x1.decimalRepresentation) / 2)
    gene_x2 = Gene.createFromDecimalValue(
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
    return Gene.createFromDecimalValue(new_gene_value)


# TODO: same as linear_crossover
def blend_crossover_alpha(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    #  TODO: do we want to randomly gen alpha or provide
    alpha = random.random()

    new_chromosome1 = Chromosome(
        generate_blend_gene(alpha, alpha, chromosome1.x1.decimalRepresentation, chromosome2.x1.decimalRepresentation),
        generate_blend_gene(alpha, alpha, chromosome1.x2.decimalRepresentation, chromosome2.x2.decimalRepresentation)
    )

    new_chromosome2 = Chromosome(
        generate_blend_gene(alpha, alpha, chromosome1.x1.decimalRepresentation, chromosome2.x1.decimalRepresentation),
        generate_blend_gene(alpha, alpha, chromosome1.x2.decimalRepresentation, chromosome2.x2.decimalRepresentation)
    )

    return new_chromosome1, new_chromosome2


def blend_crossover_alpha_beta(chromosome1: Chromosome, chromosome2: Chromosome) -> (Chromosome, Chromosome):
    assumptions = Assumptions()
    new_chromosome1, new_chromosome2 = None, None
    is_valid = False

    while not is_valid:
        #  TODO: do we want to randomly gen alpha and beta or provide
        alpha, beta = random.random(), random.random()

        new_chromosome1 = Chromosome(
            generate_blend_gene(alpha, beta, chromosome1.x1.decimalRepresentation,
                                chromosome2.x1.decimalRepresentation),
            generate_blend_gene(alpha, beta, chromosome1.x2.decimalRepresentation, chromosome2.x2.decimalRepresentation)
        )

        new_chromosome2 = Chromosome(
            generate_blend_gene(alpha, beta, chromosome1.x1.decimalRepresentation,
                                chromosome2.x1.decimalRepresentation),
            generate_blend_gene(alpha, beta, chromosome1.x2.decimalRepresentation, chromosome2.x2.decimalRepresentation)
        )

        is_valid = all(
            [assumptions.in_bounds(new_chromosome1.x1.decimalRepresentation),
             assumptions.in_bounds(new_chromosome1.x2.decimalRepresentation),
             assumptions.in_bounds(new_chromosome2.x1.decimalRepresentation),
             assumptions.in_bounds(new_chromosome2.x2.decimalRepresentation)]
        )

    return new_chromosome1, new_chromosome2


if __name__ == '__main__':
    a = Assumptions()
    a.set_assumptions(-5, 5, 3)
    g1, g2 = Gene("111"), Gene("110")
    g3, g4 = Gene("001"), Gene("100")
    c1, c2 = blend_crossover_alpha_beta(Chromosome(g1, g2), Chromosome(g3, g4))
