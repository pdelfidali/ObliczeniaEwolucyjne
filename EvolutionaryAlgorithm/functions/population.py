import random

from Assumptions import Assumptions
from Chromosome import Chromosome
from functions.crossover import crossover_genes
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
    new_gene_x1_1, new_gene_x1_2 = crossover_genes(parent_1.x1, parent_2.x1)
    new_gene_x2_1, new_gene_x2_2 = crossover_genes(parent_1.x2, parent_2.x2)
    return Chromosome(new_gene_x1_1, new_gene_x2_1), Chromosome(new_gene_x1_2, new_gene_x2_2)


def crossover_population(parents: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions()
    children_size = assumptions.population_size
    children = []

    for _ in range(children_size // 2):
        parent_1, parent_2 = random.sample(parents, k=2)
        child_1, child_2 = generate_children(parent_1, parent_2)
        children.extend([child_1, child_2])

    if children_size % 2 == 1:
        parent_1, parent_2 = random.sample(parents, k=2)
        child_1, _ = generate_children(parent_1, parent_2)
        children.append(child_1)

    return children


def mutate_population(population: list[Chromosome]) -> list[Chromosome]:
    return list(map(mutate_chromosome, population))
