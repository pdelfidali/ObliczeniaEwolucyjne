from unittest import TestCase

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene


def goal_fun(x1, x2):
    return 2 * x2 ** 2 + 5


assumptions = Assumptions(-10, 10, 25)
gene1 = Gene('110010010010101011010', assumptions)
gene2 = Gene('0100001000111111001001110', assumptions)
chromosome = Chromosome(gene1, gene2, goal_fun)


class TestGene(TestCase):
    def test_converting_to_decimal(self):
        self.assertAlmostEqual(-9.0177380738, gene1.decimalRepresentation, places=6)
        self.assertAlmostEqual(-4.82447727573, gene2.decimalRepresentation, places=6)


class TestChromosome(TestCase):
    def test_calculating_goal_func_value(self):
        self.assertAlmostEqual(51.551162, chromosome.get_goal_function_value(), places=6)
