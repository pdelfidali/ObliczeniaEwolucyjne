from Assumptions import Assumptions
from Chromosome import Chromosome


def init_population(size: int) -> list[Chromosome]:  # TODO: add init
    # init_populaion(n) -> return [Chromosome.random for _ in range(n)] # TODO: add randomizer
    return []


def select_new_parents(population: list[Chromosome]) -> list[Chromosome]:  # TODO add tests
    assumptions = Assumptions()
    parents = assumptions.selection_func(population)

    return parents


def crossover_population(population: list[Chromosome]) -> list[Chromosome]:  # TODO add tests
    assumptions = Assumptions()
    return list(map(assumptions.crossover_func, population))


def mutate_population(population: list[Chromosome]) -> list[Chromosome]:  # TODO add tests
    assumptions = Assumptions()
    return list(map(assumptions.mutation_func, population))
