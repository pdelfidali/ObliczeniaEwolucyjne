import random

# Bazując na implementacji algorytmów krzyżowania w Deap zaimplementuj algorytm
# krzyżowania arytmetycznego, linearnego, mieszającego typu alfa, mieszającego typu alfa
# i beta oraz uśredniającego


minValue = -10
maxValue = 10


def fitness_function(_individual):
    x1, x2 = _individual[0], _individual[1]
    result = (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2
    return result,


def cxArithmetic(ind1, ind2):
    k = random.random()
    dec1 = ind1[0]
    dec2 = ind2[0]

    dec3 = ind1[1]
    dec4 = ind2[1]

    crossed_decs1, crossed_decs2 = None, None
    crossed_decs3, crossed_decs4 = None, None

    # while not (crossed_decs1 and (minValue <= crossed_decs1 <= maxValue) and (minValue <= crossed_decs2 <= maxValue)):
    crossed_decs1 = k * dec1 + (1 - k) * dec2
    crossed_decs2 = (1 - k) * dec1 + k * dec2

    # while not (crossed_decs3 and (minValue <= crossed_decs3 <= maxValue) and (minValue <= crossed_decs4 <= maxValue)):
    crossed_decs3 = k * dec3 + (1 - k) * dec4
    crossed_decs4 = (1 - k) * dec3 + k * dec4

    ind1[0], ind1[1] = crossed_decs1, crossed_decs3
    ind2[0], ind2[1] = crossed_decs2, crossed_decs4

    return ind1, ind2


def cxLinear(ind1, ind2):
    mode = 'min'

    gene_x1_z = (ind1[0] / 2 + ind2[0] / 2)
    gene_x2_z = (ind1[1] / 2 + ind2[1] / 2)
    chromosome_z = [gene_x1_z, gene_x2_z]

    gene_x1_v = (ind1[0] * 3 / 2 - ind2[0] / 2)
    gene_x2_v = (ind1[1] * 3 / 2 - ind2[1] / 2)
    chromosome_v = [gene_x1_v, gene_x2_v]

    gene_x1_w = (-ind1[0] / 2 + ind2[0] * 3 / 2)
    gene_x2_w = (-ind1[1] / 2 + ind2[1] * 3 / 2)
    chromosome_w = [gene_x1_w, gene_x2_w]

    crossover_rank_selection = [chromosome_z, chromosome_v, chromosome_w]

    if mode == 'max':
        crossover_rank_selection.sort(key=fitness_function, reverse=True)
    else:
        crossover_rank_selection.sort(key=fitness_function, reverse=False)

    selected_children = crossover_rank_selection[:2]

    # return selected_children[0], selected_children[1]
    return selected_children


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
    return new_gene_value


def generate_blend_individual(alpha, beta, ind1, ind2):
    new_chromosome1 = [
        generate_blend_gene(alpha, beta, ind1[0], ind2[0]),
        generate_blend_gene(alpha, beta, ind1[1], ind2[1])
    ]
    new_chromosome2 = [
        generate_blend_gene(alpha, beta, ind1[0], ind2[0]),
        generate_blend_gene(alpha, beta, ind1[1], ind2[1])
    ]
    return new_chromosome1, new_chromosome2


def cxBlendAlpha(ind1, ind2):
    alpha = random.random()

    ind1, ind2 = generate_blend_individual(alpha, alpha, ind1, ind2)
    return ind1, ind2


def cxBlendAlphaBeta(ind1, ind2):
    alpha, beta = random.random(), random.random()
    ind1, ind2 = generate_blend_individual(alpha, beta, ind1, ind2)

    return ind1, ind2


def cxAverage(ind1, ind2):
    gene_x1 = (ind1[0] + ind2[0]) / 2
    gene_x2 = (ind1[1] + ind2[1]) / 2
    ind_avg = [gene_x1, gene_x2]
    return ind1, ind_avg
    # return ind_avg

