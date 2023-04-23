import random

from Gene.BinaryGene import BinaryGene


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
    return BinaryGene(crossed_bits1), BinaryGene(crossed_bits2)


def one_point_crossover(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split = random.randint(1, len(bits1) - 1)
    crossed_bits1 = bits1[:n_split] + bits2[n_split:]
    crossed_bits2 = bits2[:n_split] + bits1[n_split:]
    return BinaryGene(crossed_bits1), BinaryGene(crossed_bits2)


def two_point_crossover(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split1, n_split2 = sorted(random.sample(range(1, len(bits1) - 1), 2))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:]
    return BinaryGene(crossed_bits1), BinaryGene(crossed_bits2)


def three_point_crossover(gene1: BinaryGene, gene2: BinaryGene) -> (BinaryGene, BinaryGene):
    bits1 = gene1.binaryRepresentation
    bits2 = gene2.binaryRepresentation
    n_split1, n_split2, n_split3 = sorted(random.sample(range(1, len(bits1) - 1), 3))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:n_split3] + bits2[n_split3:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:n_split3] + bits1[n_split3:]
    return BinaryGene(crossed_bits1), BinaryGene(crossed_bits2)
