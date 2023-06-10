from time import time

import pandas as pd
from mealpy.swarm_based.FOA import OriginalFOA


def himmelblau_function(solution):
    return (solution[0] ** 2 + solution[1] - 11) ** 2 + (solution[0] + solution[1] ** 2 - 7) ** 2


if __name__ == '__main__':
    problem_dict1 = {
        "fit_func": himmelblau_function,
        "lb": [-10, -10],
        "ub": [10, 10],
        "minmax": "min",
    }
    results = []
    for epoch in [10, 100, 250, 1000]:
        for pop_size in [10, 50, 100]:
            model = OriginalFOA(epoch, pop_size)
            t_start = time()
            best_position, best_fitness = model.solve(problem_dict1, mode='swarm')
            runtime = time() - t_start
            results.append({'rozwiązanie': best_position, 'funkcja celu': best_fitness, 'epoki': epoch, 'wielkość populacji': pop_size, 'czas': runtime})
    results = pd.DataFrame(results)
    results.to_csv('non_changed.csv')