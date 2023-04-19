import random

from Assumptions import Assumptions
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
    min_v = assumptions.minValue
    max_v = assumptions.maxValue
    k = random.random()
    dec1 = gene1.decimalRepresentation
    dec2 = gene2.decimalRepresentation

    is_valid = False
    crossed_decs1, crossed_decs2 = None, None

    while not is_valid:
        print('d')
        crossed_decs1 = k * dec1 + (1 - k) * dec2
        crossed_decs2 = (1 - k) * dec1 + k * dec2
        if min_v <= crossed_decs1 <= max_v and min_v <= crossed_decs2 <= max_v:
            is_valid = True

            # 1) Pamiętajmy, że po procesie krzyżowania nasze
            # geny dalej muszą mieścić się w przedziałach – jeśli
            # tak nie jest musimy ponowić proces - TO CHYBA NIE BYLO DO TEGO ALE PRZYPADKIEM ZAIMPLEMENTOWALEM

    return Gene.createFromDecimalValue(crossed_decs1), Gene.createFromDecimalValue(crossed_decs2)  # TODO: do this


if __name__ == '__main__':
    a = Assumptions()
    a.set_assumptions(-5, 5, 3)
    g1, g2 = Gene("111"), Gene("111")
    arithmetic_crossover(g1, g2)
