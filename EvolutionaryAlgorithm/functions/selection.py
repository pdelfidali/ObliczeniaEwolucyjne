import math
import random

from EvolutionaryAlgorithm.Assumptions import Assumptions
from EvolutionaryAlgorithm.Chromosome import Chromosome
from EvolutionaryAlgorithm.Gene import Gene


def select_new_parents(population: list[Chromosome]) -> list[Chromosome]: # TODO add tests
    assumptions = Assumptions()
    parents = assumptions.selection_func(population)
    
    return parents

def rank_selection(population: list[Chromosome]): 
    alpha = 0.3  # TODO add config vars of selections
    population.sort(reverse=True)
    n_parents = math.floor(alpha * len(population))
    selected_parents = population[:n_parents]

    return selected_parents

def tournament_selection(population: list[Chromosome]):
    k = 3
    random.shuffle(population)
    new_parents = []

    while population: # TODO check for more pythonic approach
        tourney = []
        for _ in range(k):
            if population:
                tourney.append(population.pop())
        tourney.sort(reverse=True)
        winner = tourney[0]
        new_parents.append(winner)

    return new_parents


def roulette_wheel_selection(population: list[Chromosome]):
    pass
