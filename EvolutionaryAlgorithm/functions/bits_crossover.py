import random


def homogeneous_crossover(bits1: str, bits2: str) -> (str, str):
    crossed_bits1 = ''
    crossed_bits2 = ''
    for n in range(len(bits1)):
        if n % 2:
            crossed_bits1 += bits2[n]
            crossed_bits2 += bits1[n]
        else:
            crossed_bits1 += bits1[n]
            crossed_bits2 += bits2[n]
    return crossed_bits1, crossed_bits2


def one_point_crossover(bits1: str, bits2: str) -> (str, str):
    n_split = random.randint(1, len(bits1) - 1)
    crossed_bits1 = bits1[:n_split] + bits2[n_split:]
    crossed_bits2 = bits2[:n_split] + bits1[n_split:]
    return crossed_bits1, crossed_bits2


def two_point_crossover(bits1: str, bits2: str) -> (str, str):
    n_split1, n_split2 = sorted(random.sample(range(1, len(bits1) - 1), 2))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:]
    return crossed_bits1, crossed_bits2


def three_point_crossover(bits1: str, bits2: str) -> (str, str):
    n_split1, n_split2, n_split3 = sorted(random.sample(range(1, len(bits1) - 1), 3))
    crossed_bits1 = bits1[:n_split1] + bits2[n_split1:n_split2] + bits1[n_split2:n_split3] + bits2[n_split3:]
    crossed_bits2 = bits2[:n_split1] + bits1[n_split1:n_split2] + bits2[n_split2:n_split3] + bits1[n_split3:]
    return crossed_bits1, crossed_bits2
