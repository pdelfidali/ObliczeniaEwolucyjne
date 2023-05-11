import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from functions.crossover import crossover_genes, crossover_chromosomes
from functions.mutation import mutate_chromosome


def init_random_population() -> list[Chromosome]:
    assumptions = Assumptions()
    population = [Chromosome.generate_random_chromosome() for _ in range(assumptions.population_size)]
    return population


def select_new_parents(population: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions()
    parents = assumptions.selection_func(population)

    return parents


def generate_children(parent_1: Chromosome, parent_2: Chromosome) -> (Chromosome, Chromosome):
    return crossover_chromosomes(parent_1, parent_2)


def crossover_population(parents: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions()
    children_size = assumptions.population_size
    children = []

    while len(children) < children_size:
        parent_1, parent_2 = random.sample(parents, k=2)
        child = generate_children(parent_1, parent_2)
        if isinstance(child, Chromosome):
            children.append(child)
        else:
            children.extend(child)

    if children_size % 2 == 1:
        parent_1, parent_2 = random.sample(parents, k=2)
        child_1, _ = generate_children(parent_1, parent_2)
        children.append(child_1)

    return children


def mutate_population(population: list[Chromosome]) -> list[Chromosome]:
    return list(map(mutate_chromosome, population))
