import numpy as np
from numpy import random

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
    return solutions, scores


def random_sampling():
    assumptions = Assumptions()
    best = random.uniform(assumptions.minValue, assumptions.maxValue, 2)
    solutions = [best]
    scores = [assumptions.goal_function(*best)]

    for i in range(0, assumptions.epochs):
        tmp = random.uniform(assumptions.minValue, assumptions.maxValue, 2)
        solutions.append(tmp)
        scores.append(assumptions.goal_function(*tmp))
        if assumptions.goal_function(*tmp) < assumptions.goal_function(*best):
            best = tmp
    return solutions, scores


def random_walk():
    assumptions = Assumptions()
    best = random.uniform(assumptions.minValue, assumptions.maxValue, 2)
    step_size = assumptions.metaheuristics_params['step_size']
    solutions = [best]
    scores = [assumptions.goal_function(*best)]

    for x in range(0, assumptions.epochs):
        tmp = best + random.uniform(assumptions.minValue, assumptions.maxValue, 2) * step_size
        solutions.append(tmp)
        scores.append(assumptions.goal_function(*tmp))
        best = tmp
    return solutions, scores


def simulated_annealing():
    assumptions = Assumptions()
    objective = assumptions.goal_function
    bounds = np.array([[assumptions.minValue, assumptions.maxValue], [assumptions.minValue, assumptions.maxValue]])
    n_iterations = assumptions.epochs
    step_size = assumptions.metaheuristics_params['step_size']
    temp = assumptions.metaheuristics_params['temperature']
    # generate an initial point
    best = bounds[:, 0] + random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    best_eval = objective(*best)
    # current working solution
    curr, curr_eval = best, best_eval
    solutions = [curr]
    scores = [curr_eval]
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate = curr + random.randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective(*candidate)
        scores.append(candidate_eval)
        solutions.append(candidate)
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best, best_eval = candidate, candidate_eval
            # keep track of scores
            scores.append(best_eval)
            # report progress
            print('>%d f(%s) = %.5f' % (i, best, best_eval))
        # difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # calculate temperature for current epoch
        t = temp / float(i + 1)
        # calculate metropolis acceptance criterion
        metropolis = np.exp(-diff / t)
        # check if we should keep the new point
        if diff < 0 or random.rand() < metropolis:
            # store the new current point
            curr, curr_eval = candidate, candidate_eval
    return solutions, scores
