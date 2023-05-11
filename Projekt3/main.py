from random import randint

from deap import base
from deap import creator
from deap import tools


def individual(icls):
    genome = list()
    for x in range(0, 40):
        genome.append(randint(0, 1))
    return icls(genome)


def fitnessFunction(individual):
    # tutaj rozkoduj binarnego osobnika! Napisz funkcje decodeInd
    ind = decodeInd(individual)     
    result = (ind[0] + 2* ind[1] - 7)**2 + (2* ind[0] + ind[1] -5)**2
    return result,
