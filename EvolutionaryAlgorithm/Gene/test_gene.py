from unittest import TestCase

from Assumptions import Assumptions
from BinaryGene import Gene


class TestGene(TestCase):
    def test_converting_to_decimal(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25, mutation_probability=1)
        gene1 = Gene('110010010010101011010')
        gene2 = Gene('0100001000111111001001110')
        self.assertAlmostEqual(-9.0177380738, gene1.decimalRepresentation, places=6)
        self.assertAlmostEqual(-4.82447727573, gene2.decimalRepresentation, places=6)

    def test_generating_random(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25, mutation_probability=1)
        gene = Gene.generate_random_gene()
        self.assertEqual(len(gene.binaryRepresentation), assumptions.bitsLength)
