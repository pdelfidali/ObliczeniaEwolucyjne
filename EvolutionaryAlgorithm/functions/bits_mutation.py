import random

from Assumptions import Assumptions
from Gene import Gene
from Gene.BinaryGene import BinaryGene


def reverse_bit(bit: str):
    if bit == '0':
        return '1'
    else:
        return '0'


def edge_mutation(binary_gene: BinaryGene) -> BinaryGene:
    binary_representation = binary_gene.binaryRepresentation
    new_binary_representation = binary_representation[:-1] + reverse_bit(binary_representation[-1])
    return BinaryGene(new_binary_representation)


def one_point_mutation(binary_gene: BinaryGene) -> BinaryGene:
    binary_representation = binary_gene.binaryRepresentation
    n_mutate = random.randint(0, len(binary_representation) - 1)
    new_binary_representation = binary_representation[:n_mutate] + reverse_bit(
        binary_representation[n_mutate]) + binary_representation[n_mutate + 1:]
    return BinaryGene(new_binary_representation)


def two_point_mutation(binary_gene: BinaryGene) -> BinaryGene:
    binary_representation = binary_gene.binaryRepresentation
    n_mutate1, n_mutate2 = sorted(random.sample(range(1, len(binary_representation) - 1), 2))
    new_binary_representation = binary_representation[:n_mutate1] + reverse_bit(
        binary_representation[n_mutate1]) + binary_representation[n_mutate1 + 1: n_mutate2] + reverse_bit(
        binary_representation[n_mutate2]) + binary_representation[n_mutate2 + 1:]
    return BinaryGene(new_binary_representation)


def inversion_mutation(binary_gene: BinaryGene) -> BinaryGene:
    binary_representation = binary_gene.binaryRepresentation
    n_split1, n_split2 = sorted(random.sample(range(1, len(binary_representation) - 1), 2))
    inversed_split = ''.join(map(reverse_bit, binary_representation[n_split1:n_split2]))
    new_binary_representation = binary_representation[:n_split1] + inversed_split + binary_representation[n_split2:]
    return BinaryGene(new_binary_representation)
