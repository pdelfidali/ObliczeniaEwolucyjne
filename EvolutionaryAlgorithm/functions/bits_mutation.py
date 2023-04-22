import random

from Assumptions import Assumptions
from Gene import Gene

def reverse_bit(bit: str):
    if bit == '0':
        return '1'
    else:
        return '0'


def edge_mutation(binary_representation: str) -> str:
    new_binary_representation = binary_representation[:-1] + reverse_bit(binary_representation[-1])
    return new_binary_representation


def one_point_mutation(binary_representation: str) -> str:
    n_mutate = random.randint(0, len(binary_representation) - 1)
    new_binary_representation = binary_representation[:n_mutate] + reverse_bit(
        binary_representation[n_mutate]) + binary_representation[n_mutate + 1:]
    return new_binary_representation


def two_point_mutation(binary_representation: str) -> str:
    n_mutate1, n_mutate2 = sorted(random.sample(range(1, len(binary_representation) - 1), 2))
    new_binary_representation = binary_representation[:n_mutate1] + reverse_bit(
        binary_representation[n_mutate1]) + binary_representation[n_mutate1 + 1: n_mutate2] + reverse_bit(
        binary_representation[n_mutate2]) + binary_representation[n_mutate2 + 1:]
    return new_binary_representation


def inversion_mutation(binary_representation: str) -> str:
    n_split1, n_split2 = sorted(random.sample(range(1, len(binary_representation) - 1), 2))
    inversed_split = ''.join(map(reverse_bit, binary_representation[n_split1:n_split2]))
    new_binary_representation = binary_representation[:n_split1] + inversed_split + binary_representation[n_split2:]
    return new_binary_representation




if __name__ == '__main__':
    a = Assumptions()
    a.set_assumptions(-5, 5, 3)
    g1 = Gene("111")
    uniform_mutation(g1)

#  TODO: PROPOSITIONS
#   1. dont use binaryRepresentation field when dealing with real representation of a Gene (eliminates the need of
#       generating the field
#   2. if applied, use only this new methods together to eliminate the conflicts of missing representations (i.e. doing
#       uniform mutation but suddenly missing binaryRep for crossover - use real rep crossovers
