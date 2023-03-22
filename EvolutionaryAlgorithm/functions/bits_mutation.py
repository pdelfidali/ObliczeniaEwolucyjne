import random


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
