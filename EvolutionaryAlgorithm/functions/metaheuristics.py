from numpy import random
import numpy as np
from Assumptions import Assumptions


def hill_climbing():
    assumptions = Assumptions()
    bounds = np.array([[assumptions.minValue, assumptions.maxValue], [assumptions.minValue, assumptions.maxValue]])
    n_iterations = assumptions.epochs
    step_size = assumptions.metaheuristics_params['step_size']
    # TODO: adjust to our code?

    # generate an initial point
    solution = bounds[:, 0] + random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    solution_eval = assumptions.goal_function(*solution)
    # run the hill climb
    scores = list()
    solutions = []
    scores.append(solution_eval)
    solutions.append(solution)
    for i in range(n_iterations):
        # take a step
        candidate = solution + random.randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = assumptions.goal_function(*candidate)
        # check if we should keep the new point
        if candidate_eval <= solution_eval:
            # store the new point
            solution, solution_eval = candidate, candidate_eval
            # keep track of scores
        scores.append(solution_eval)
        solutions.append(solution)
    return [solutions, scores]


def random_sampling():
    assumptions = Assumptions()
    best = random.uniform(assumptions.minValue, assumptions.maxValue)
    X = []

    for x in range(0, assumptions.epochs):
        tmp = random.uniform(assumptions.minValue, assumptions.maxValue)
        X.append(tmp)
        if assumptions.goal_function(tmp) < assumptions.goal_function(best):
            best = tmp
    return X


def random_walk():
    print('test')


def simulated_annealing():
    pass
