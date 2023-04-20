from math import log2, ceil
from typing import Callable

# from functions.bits_crossover import homogeneous_crossover
# from functions.bits_mutation import edge_mutation
# from functions.selection import rank_selection

DEFAULT_SELECTION_PARAMS = {
    'rank': 0.3,
    'tournament': 3,
    'roulette': 3
}


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
    selection_params: dict[str, any]
    elite_strategy: bool
    optimization_mode: str

    def set_assumptions(self, min_value: float, max_value: float, bits_length: int = None, precision: int = None,
                        population_size: int = 10, epochs: int = 50, mutation_probability: float = 0.05,
                        mutation_func: Callable = None, crossover_probability: float = 0.75,
                        crossover_func: Callable = None, selection_func: Callable = None,
                        selection_params: dict[str, any] = None, goal_function: Callable = None, elite_strategy=True,
                        optimization_mode: str = 'max'):
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
        self.elite_strategy = elite_strategy
        self.optimization_mode = optimization_mode

        if selection_params is None:
            self.selection_params = DEFAULT_SELECTION_PARAMS.copy()
        else:
            self.selection_params = selection_params.copy()

        if precision:
            self.precision = precision
            self.bitsLength = ceil(log2((max_value - min_value) * 10 ** precision) + log2(1))
        elif bits_length:
            self.bitsLength = bits_length
        else:
            raise Exception("Value of bits_length or precision must be provided.")

    def set_selection_params(self, key, val):
        """
        rank_selection sets alpha, tournament_selection sets tourney size, roulette_wheel_selection sets amount of spins
        """
        self.selection_params[key] = val

    def set_precision_type(self, precision_type, val):
        if precision_type == 'precision':
            self.precision = val
            self.bitsLength = ceil(log2((self.minValue - self.maxValue) * 10 ** self.precision) + log2(1))
        elif precision_type == 'bits_length':
            self.bitsLength = val
        else:
            raise Exception("Value of bits_length or precision must be provided.")

    # TODO: new function, may be useful in metaheuristics
    def in_bounds(self, val: float):
        return self.minValue <= val <= self.maxValue
