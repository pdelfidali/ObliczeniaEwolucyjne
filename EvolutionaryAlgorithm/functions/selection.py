import math
import random

import Assumptions
import Chromosome


def rank_selection(population: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions.Assumptions()
    alpha = assumptions.selection_params['rank']
    size = assumptions.population_size

    assert size == len(population), f'population of size {size} expected, got: {len(population)}'
    population.sort(reverse=True)  # TODO: determine in which way sort the list (maximize or minimize) | another param?
    n_parents = math.floor(alpha * size)
    assert n_parents >= 2, f'number of selected parents >=2 expected, got: {n_parents}'

    selected_parents = population[:n_parents]
    return selected_parents


def tournament_selection(population: list[Chromosome]) -> list[Chromosome]:
    """
    Divide population in tourneys of size k,
    best fitting chromosome is the winner
    and gets selected for next gen parents
    """

    assumptions = Assumptions.Assumptions()
    tourney_size = assumptions.selection_params['tournament']
    size = assumptions.population_size
    assert size == len(population), f'population of size {size} expected, got: {len(population)}'

    population = population.copy()  # avoid side effects
    random.shuffle(population)
    selected_parents = []

    while population:
        tourney = []
        for _ in range(tourney_size):
            if population:
                tourney.append(population.pop())
        tourney.sort(reverse=True)
        winner = tourney[0]
        selected_parents.append(winner)

    assert len(selected_parents) >= 2, f'number of selected parents >=2 expected, got: {len(selected_parents)}'
    return selected_parents


def roulette_wheel_selection(population: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions.Assumptions()
    spins = assumptions.selection_params['roulette']
    size = assumptions.population_size
    assert size == len(population), f'population of size {size} expected, got: {len(population)}'

    # Calculate the fitness values of each chromosome
    fitness_values = [1 / (c.get_goal_function_value() + 1e-6) for c in population]
    total_fitness = sum(fitness_values)

    # Calculate the selection probabilities for each chromosome
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]

    # Select k chromosomes using roulette wheel selection
    selected_parents = []
    for _ in range(spins):
        r = random.uniform(0, 1)
        cumulative_probability = 0
        for j, probability in enumerate(selection_probabilities):
            cumulative_probability += probability
            if cumulative_probability > r:
                selected_parents.append(population[j])  # TODO: do we want to draw with return? (multiple same parents)
                break

    assert len(selected_parents) >= 2, f'number of selected parents >=2 expected, got: {len(selected_parents)}'
    return selected_parents
