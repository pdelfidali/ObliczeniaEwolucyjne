from math import log2, ceil
from typing import Callable

from functions.bits_crossover import homogeneous_crossover
from functions.bits_mutation import edge_mutation
from functions.selection import rank_selection


class AssumptionsMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Assumptions(metaclass=AssumptionsMeta):
    minValue: float
    maxValue: float
    bitsLength: int
    mutation_func: Callable
    mutation_probability: float
    crossover_func: Callable
    crossover_probability: float
    precision: int
    goal_function: Callable
    selection_func = Callable
    population_size: int
    epochs: int

    # selection params somehow

    def set_assumptions(self, min_value: float, max_value: float, bits_length: int = None, precision: int = None,
                        population_size: int = 10, epochs: int = 50, mutation_probability: float = 0.05,
                        mutation_func: Callable = edge_mutation, crossover_probability: float = 0.75,
                        crossover_func: Callable = homogeneous_crossover, selection_func: Callable = rank_selection,
                        goal_function: Callable = None):
        self.maxValue = max_value
        self.minValue = min_value
        self.mutation_probability = mutation_probability
        self.mutation_func = mutation_func
        self.crossover_probability = crossover_probability
        self.crossover_func = crossover_func
        self.selection_func = selection_func
        self.goal_function = goal_function
        self.population_size = population_size
        self.epochs = epochs
        if precision:
            self.precision = precision
            self.bitsLength = ceil(log2((max_value - min_value) * 10 ** precision) + log2(1))
        elif bits_length:
            self.bitsLength = bits_length
        else:
            raise Exception("Value of bits_length or precision must be provided.")
