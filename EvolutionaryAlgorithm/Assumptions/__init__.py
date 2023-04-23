from math import log2, ceil
from typing import Callable

DEFAULT_SELECTION_PARAMS = {
    'rank': 0.3,
    'tournament': 3,
    'roulette': 3
}


def himmelblau_function(x1, x2):
    return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2


class AssumptionsMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Assumptions(metaclass=AssumptionsMeta):
    method: str
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
    selection_param: float
    elite_strategy: bool
    optimization_mode: str
    metaheuristics_params: dict[str, any]
    metaheuristics_func: Callable

    def set_precision_type(self, precision_type, val):
        self.precision = None
        self.bitsLength = None
        if precision_type == 'precision':
            self.precision = val
            self.bitsLength = ceil(log2((self.maxValue - self.minValue) * 10 ** self.precision) + log2(1))
        elif precision_type == 'bits_length':
            self.bitsLength = val
        else:
            raise Exception("Value of bits_length or precision must be provided.")

    def in_bounds(self, val: float):
        if val:
            return self.minValue <= val <= self.maxValue
        else:
            return False

    def set_method(self, method: str):
        self.method = method

    def set_data_range(self, min_value, max_value):
        self.minValue = min_value
        self.maxValue = max_value

    def set_population(self, population_size):
        self.population_size = population_size

    def set_epochs(self, epochs):
        self.epochs = epochs

    def set_crossover(self, crossover_func, crossover_probability):
        self.crossover_func = crossover_func
        self.crossover_probability = crossover_probability

    def set_mutation(self, mutation_func, mutation_probability):
        self.mutation_func = mutation_func
        self.mutation_probability = mutation_probability

    def set_elite_strategy(self, elite_strategy):
        self.elite_strategy = elite_strategy

    def set_selection(self, selection_func, selection_param_value):
        self.selection_func = selection_func
        self.selection_param = selection_param_value

    def set_optimization_mode(self, optimization_mode):
        self.optimization_mode = optimization_mode

    def set_goal_function(self, goal_function):
        self.goal_function = goal_function

    def __init__(self):
        self.goal_function = himmelblau_function

    def set_metaheuristics(self, metaheuristics_func, metaheuristics_params=None):
        self.metaheuristics_func = metaheuristics_func
        self.metaheuristics_params = metaheuristics_params
