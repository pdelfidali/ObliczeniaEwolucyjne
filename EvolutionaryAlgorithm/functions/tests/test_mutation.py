from unittest import TestCase

from Assumptions import Assumptions
from Gene import Gene
from functions.bits_mutation import edge_mutation, one_point_mutation, two_point_mutation, inversion_mutation
from functions.mutation import mutate_gene


def count_changes(bits, mutated):
    n_changes = 0
    for i in range(len(bits)):
        if bits[i] != mutated[i]:
            n_changes += 1
    return n_changes


class TestMutate(TestCase):
    def test_mutate_returns_gene_of_same_length(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25)
        gene = Gene('110010010010101011010')
        new_gene = mutate_gene(gene)
        self.assertEqual(len(gene.binaryRepresentation), len(new_gene.binaryRepresentation))

    def test_mutate_returns_gene_with_reversed_bits_if_probability_is_1(self):
        assumptions_mutation_prob_1 = Assumptions()
        assumptions_mutation_prob_1.set_assumptions(-10, 10, 25, mutation_probability=1)
        gene = Gene('110010010010101011010')
        new_gene = mutate_gene(gene)
        self.assertEqual(1, count_changes(new_gene.binaryRepresentation, '110010010010101011010'))

    def test_mutate_returns_gene_with_same_bits_if_probability_is_0(self):
        assumptions_mutation_prob_0 = Assumptions()
        assumptions_mutation_prob_0.set_assumptions(-10, 10, 25, mutation_probability=0)
        gene = Gene('110010010010101011010')
        new_gene = mutate_gene(gene)
        self.assertEqual(0, count_changes(new_gene.binaryRepresentation, '110010010010101011010'))


class TestBitsMutation(TestCase):
    def test_edge_mutation(self):
        bits = '101010'
        mutated = edge_mutation(bits)
        self.assertEqual(bits[:-1], mutated[:-1])
        self.assertEqual('1', mutated[-1])
        bits = '10111011'
        mutated = edge_mutation(bits)
        self.assertEqual(bits[:-1], mutated[:-1])
        self.assertEqual('0', mutated[-1])
        self.assertEqual(1, count_changes(bits, mutated))

    def test_one_point_mutation(self):
        bits = '101010'
        mutated = one_point_mutation(bits)
        self.assertEqual(len(bits), len(mutated))
        self.assertEqual(1, count_changes(bits, mutated))

    def test_two_point_mutation(self):
        bits = '101010'
        mutated = two_point_mutation(bits)
        self.assertEqual(len(bits), len(mutated))
        self.assertEqual(2, count_changes(bits, mutated))

    def test_inversion_mutation(self):
        bits = '101010'
        mutated = inversion_mutation(bits)
        self.assertEqual(len(bits), len(mutated))
        self.assertEqual(2, count_changes(bits, mutated))
        pass
