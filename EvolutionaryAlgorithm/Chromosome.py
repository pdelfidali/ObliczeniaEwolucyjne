from typing import Callable

from Gene import Gene


class Chromosome:
    x1: Gene
    x2: Gene
    goalFunction: Callable

    def __init__(self, x1: Gene, x2: Gene, goal_function: Callable):
        self.x1 = x1
        self.x2 = x2
        self.goalFunction = goal_function

    def get_goal_function_value(self):
        return self.goalFunction(self.x1.decimalRepresentation, self.x2.decimalRepresentation)


