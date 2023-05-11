from unittest import TestCase

from Assumptions import Assumptions
from Chromosome import Chromosome
from Gene import Gene
from functions.bits_crossover import one_point_crossover
from functions.population import init_random_population, select_new_parents, crossover_population, generate_children, \
    mutate_population


def dummy_selection(population: list[Chromosome]):
    return population[:len(population) // 2]


class TestPopulationOperations(TestCase):
    def test_init_random_population(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25, population_size=2)
        population = init_random_population()

        self.assertEqual(len(population), assumptions.population_size)
        for p in population:
            self.assertIsInstance(p, Chromosome)

    def test_select_new_parents(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 25, population_size=9, selection_func=dummy_selection)
        population = init_random_population()
        new_parents = select_new_parents(population)
        for p in new_parents:
            self.assertIsInstance(p, Chromosome)
        self.assertEqual(new_parents, population[:len(population) // 2])

    def test_generate_children(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 4, crossover_probability=1, crossover_func=one_point_crossover)
        parent_1 = Chromosome(Gene('0000'), Gene('1111'))
        parent_2 = Chromosome(Gene('1111'), Gene('0000'))

        children = generate_children(parent_1, parent_2)
        for c in children:
            self.assertIsInstance(c, Chromosome)
            for p in [parent_1, parent_2]:
                self.assertNotEqual(c.x1.binaryRepresentation, p.x1.binaryRepresentation)
                self.assertNotEqual(c.x2.binaryRepresentation, p.x2.binaryRepresentation)

    def test_crossover_population(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 4, population_size=9)
        parents = [
            Chromosome.generate_random_chromosome(),
            Chromosome.generate_random_chromosome(),
            Chromosome.generate_random_chromosome(),
            Chromosome.generate_random_chromosome(),
        ]

        children = crossover_population(parents)
        self.assertEqual(len(children), assumptions.population_size)

    def test_mutate_population(self):
        assumptions = Assumptions()
        assumptions.set_assumptions(-10, 10, 4, mutation_probability=1)
        children = [
            Chromosome(Gene('0000'), Gene('1111')),
            Chromosome(Gene('1111'), Gene('0000'))
        ]
        children_mutated = mutate_population(children)

        self.assertEqual(len(children_mutated), len(children))
        for cm in children_mutated:
            self.assertIsInstance(cm, Chromosome)
            for c in children:
                self.assertNotEqual(cm.x1.binaryRepresentation, c.x1.binaryRepresentation)
                self.assertNotEqual(cm.x2.binaryRepresentation, c.x2.binaryRepresentation)
