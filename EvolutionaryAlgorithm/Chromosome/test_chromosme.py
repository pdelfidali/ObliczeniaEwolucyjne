from unittest import TestCase

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene


class TestChromosome(TestCase):
    def test_calculating_goal_func_value(self):
        def goal_fun(x1, x2):
            return 2 * x2 ** 2 + 5

        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25, goal_function=goal_fun)
        gene1 = Gene('110010010010101011010')
        gene2 = Gene('0100001000111111001001110')
        chromosome = Chromosome(gene1, gene2)
        self.assertAlmostEqual(51.551162, chromosome.get_goal_function_value(), places=6)

    def test_generating_random_chromosome(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25)
        chromosome = Chromosome.generate_random_chromosome()
        self.assertEqual(len(chromosome.x1.binaryRepresentation), assumptions.bitsLength)
        self.assertEqual(len(chromosome.x2.binaryRepresentation), assumptions.bitsLength)

