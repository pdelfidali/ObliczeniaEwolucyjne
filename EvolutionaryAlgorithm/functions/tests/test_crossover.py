from unittest import TestCase

from EvolutionaryAlgorithm.Assumptions import Assumptions
from EvolutionaryAlgorithm.Gene import Gene
from EvolutionaryAlgorithm.functions.bits_crossover import homogeneous_crossover
from EvolutionaryAlgorithm.functions.crossover import crossover_genes


class TestCrossover(TestCase):
    def test_homogeneous_crossover_genes(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 12, crossover_probability=1, crossover_func=homogeneous_crossover)
        gene1 = Gene('111111111111')
        gene2 = Gene('000000000000')
        crossed_bits1, crossed_bits2 = crossover_genes(gene1, gene2)
        self.assertEqual('101010101010', crossed_bits1.binaryRepresentation)
        self.assertEqual('010101010101', crossed_bits2.binaryRepresentation)

    def test_crossover_genes_returns_genes_of_same_lengths_as_input(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, bits_length=21)
        gene1 = Gene('110010010010101011010')
        gene2 = Gene('110110110010101011010')
        new_gene1, new_gene2 = crossover_genes(gene1, gene2)
        self.assertEqual(len(new_gene1.binaryRepresentation), assumptions.bitsLength)
        self.assertEqual(len(new_gene2.binaryRepresentation), assumptions.bitsLength)

    def test_crossover_genes_returns_same_genes_when_crossover_prob_is_0(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, bits_length=21, crossover_probability=0)
        gene1 = Gene('110010010010101011010')
        gene2 = Gene('110110110010101011010')
        new_gene1, new_gene2 = crossover_genes(gene1, gene2)
        self.assertEqual(gene1.binaryRepresentation, new_gene1.binaryRepresentation)
        self.assertEqual(gene2.binaryRepresentation, new_gene2.binaryRepresentation)

    def test_crossover_genes_returns_changed_genes_when_crossover_prob_is_1(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, bits_length=21, crossover_probability=1)
        gene1 = Gene('110010010010101011010')
        gene2 = Gene('110110110010101011010')
        new_gene1, new_gene2 = crossover_genes(gene1, gene2)
        self.assertNotEqual(gene1.binaryRepresentation, new_gene1.binaryRepresentation)
        self.assertNotEqual(gene2.binaryRepresentation, new_gene2.binaryRepresentation)


class TestBitsCrossover(TestCase):
    def test_homogeneous_crossover(self):
        bits1 = '111111111111'
        bits2 = '000000000000'
        crossed_bits1, crossed_bits2 = homogeneous_crossover(bits1, bits2)
        self.assertEqual('101010101010', crossed_bits1)
        self.assertEqual('010101010101', crossed_bits2)
