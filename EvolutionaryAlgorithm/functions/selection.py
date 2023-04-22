import math
import random

import Assumptions
import Chromosome


def rank_selection(population: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions.Assumptions()
    alpha = assumptions.selection_params['rank']
    size = assumptions.population_size
    mode = assumptions.optimization_mode

    assert size == len(population), f'population of size {size} expected, got: {len(population)}'

    if mode == 'max':
        population.sort(reverse=True)
    else:
        population.sort(reverse=False)

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
    mode = assumptions.optimization_mode

    assert size == len(population), f'population of size {size} expected, got: {len(population)}'

    population = population.copy()  # avoids side effects
    random.shuffle(population)
    selected_parents = []

    while population:
        tourney = []
        for _ in range(int(tourney_size)):
            if population:
                tourney.append(population.pop())
        if mode == 'max':
            tourney.sort(reverse=True)
        else:
            tourney.sort(reverse=False)
        winner = tourney[0]
        selected_parents.append(winner)

    assert len(selected_parents) >= 2, f'number of selected parents >=2 expected, got: {len(selected_parents)}'
    return selected_parents


def roulette_wheel_selection(population: list[Chromosome]) -> list[Chromosome]:
    assumptions = Assumptions.Assumptions()
    spins = assumptions.selection_params['roulette']
    size = assumptions.population_size
    mode = assumptions.optimization_mode

    assert size == len(population), f'population of size {size} expected, got: {len(population)}'

    # Calculate the fitness values of each chromosome
    fitness_values = [c.get_goal_function_value() for c in population]

    if mode == 'max':
        min_fit = min(fitness_values)
        fitness_values = list(map(lambda x: x - min_fit, fitness_values))  # maximising
    else:
        max_fit = max(fitness_values)
        fitness_values = list(map(lambda x: max_fit - x, fitness_values))  # minimising

    total_fitness = sum(fitness_values)

    # Calculate the selection probabilities for each chromosome
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]

    # Select k chromosomes using roulette wheel selection
    selected_parents = []
    for _ in range(int(spins)):
        r = random.uniform(0, 1)
        cumulative_probability = 0
        for j, probability in enumerate(selection_probabilities):
            cumulative_probability += probability
            if cumulative_probability > r:
                selected_parents.append(population[j])
                break

    assert len(selected_parents) >= 2, f'number of selected parents >=2 expected, got: {len(selected_parents)}'
    return selected_parents
