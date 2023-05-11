import math
from unittest import TestCase

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene
from functions.selection import rank_selection, tournament_selection, roulette_wheel_selection


class TestSelection(TestCase):
    population = None
    assumptions = None

    @classmethod
    def setUp(cls):
        cls.assumptions = Assumptions()
        cls.assumptions.set_assumptions(-10, 10, 4, population_size=10, goal_function=lambda x, y: x + y)

        cls.population = [
            Chromosome(Gene('1111'), Gene('1111')),
            Chromosome(Gene('1111'), Gene('1110')),
            Chromosome(Gene('1111'), Gene('1100')),
            Chromosome(Gene('1111'), Gene('1000')),
            Chromosome(Gene('1111'), Gene('0000')),
            Chromosome(Gene('1110'), Gene('0000')),
            Chromosome(Gene('1100'), Gene('0000')),
            Chromosome(Gene('1000'), Gene('0000')),
            Chromosome(Gene('0000'), Gene('0000')),
            Chromosome(Gene('0000'), Gene('0000'))
        ]

    @classmethod
    def tearDown(cls):
        cls.population = None
        cls.assumptions = None

    def test_rank_selection(self):
        alpha = 0.5
        self.assumptions.set_selection_params('rank', alpha)
        selected_parents = rank_selection(self.population)

        self.assertEqual(selected_parents, self.population[:int(alpha * len(self.population))])

    def test_tournament_selection(self):
        tourney_size = 4
        self.assumptions.set_selection_params('tournament', tourney_size)
        selected_parents = tournament_selection(self.population)

        self.assertEqual(len(selected_parents), math.ceil(len(self.population) / tourney_size))

    def test_roulette_wheel_selection(self):
        spins = 4
        self.assumptions.set_selection_params('roulette', spins)
        selected_parents = roulette_wheel_selection(self.population)

        self.assertEqual(len(selected_parents), spins)
