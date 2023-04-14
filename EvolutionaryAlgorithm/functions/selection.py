import math
import random

import Chromosome


def rank_selection(population: list[Chromosome]):
    alpha = 0.3  # TODO add config vars of selections

    population.sort(reverse=True)
    n_parents = math.floor(alpha * len(population))
    selected_parents = population[:n_parents]

    return selected_parents


def tournament_selection(population: list[Chromosome]):
    k = 3  # TODO add config vars of selections

    random.shuffle(population)
    new_parents = []

    while population:  # TODO check for more pythonic approach
        tourney = []
        for _ in range(k):
            if population:
                tourney.append(population.pop())
        tourney.sort(reverse=True)
        winner = tourney[0]
        new_parents.append(winner)

    return new_parents


def roulette_wheel_selection(population: list[Chromosome], k=3):  # TODO add config vars of selections

    # Calculate the fitness values of each chromosome
    fitness_values = [1 / c.get_goal_function_value() for c in population]
    total_fitness = sum(fitness_values)

    # Calculate the selection probabilities for each chromosome
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]

    # Select k chromosomes using roulette wheel selection
    selected = []
    for _ in range(k):
        r = random.uniform(0, 1)
        cumulative_probability = 0
        for j, probability in enumerate(selection_probabilities):
            cumulative_probability += probability
            if cumulative_probability > r:
                selected.append(population[j])
                break

    return selected
