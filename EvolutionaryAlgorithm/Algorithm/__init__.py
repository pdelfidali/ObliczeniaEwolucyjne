import datetime
import os
import time
import uuid

import numpy as np
import requests
from matplotlib import pyplot as plt

from Assumptions import Assumptions
from Chromosome import Chromosome
from functions.population import select_new_parents, crossover_population, mutate_population, init_random_population


class Algorithm:
    best_values: list[float]
    best_individuals: list[tuple[float, float]]
    population_values: list[list]
    time: float
    epoch: int
    filename: str
    assumptions_json: dict

    def __init__(self):
        self.use_metaheuristics = False
        self.process_id = None
        self.best_individuals = []
        self.population_values = []
        self.time = 0
        self.epoch = 0
        self.assumptions_json = dict()
        self.date = str(datetime.datetime.utcnow())
        self.best_values = []

    def set_date(self):
        self.date = str(datetime.datetime.utcnow())

    @staticmethod
    def get_goal_function():
        return Algorithm.himmelblau_function

    @staticmethod
    def himmelblau_function(x1, x2):
        return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2

    def append_individual(self, individual: Chromosome):
        self.best_individuals.append((individual.x1.decimalRepresentation, individual.x2.decimalRepresentation))

    def append_epoch_values(self, population: list[Chromosome]):
        epoch_values = list(map(lambda ch: ch.get_goal_function_value(), population))
        self.population_values.append(epoch_values)

    def run(self):
        self.set_date()
        assumptions = Assumptions()
        assumptions.set_goal_function(self.himmelblau_function)
        # start the timer
        st = time.time()
        population = init_random_population()

        self.process_id = f"{uuid.uuid1()}"
        print(assumptions.method)
        if assumptions.method == 'metaheuristics':
            self.use_metaheuristics = True
            solutions, scores = assumptions.metaheuristics_func()
            self.best_values = scores
            self.best_individuals = solutions

        else:
            for e in range(assumptions.epochs):
                print(f'BEGIN GENERATION #{e}')
                self.epoch = e
                # evaluate the best individual of this generation

                if assumptions.optimization_mode == 'max':
                    best_individual = max(population, key=lambda x: x.get_goal_function_value())
                else:
                    best_individual = min(population, key=lambda x: x.get_goal_function_value())

                # selection of next parents
                parents = select_new_parents(population)

                # crossover of parents
                children = crossover_population(parents)

                # mutation of children
                children = mutate_population(children)

                # form next population
                population = children

                # apply elitism strategy
                if assumptions.elite_strategy and best_individual not in population:
                    population[-1] = best_individual

                self.append_individual(best_individual)
                self.append_epoch_values(population)

                # print([{p.as_decimal_pair(), p.get_goal_function_value()} for p in population])
                et = time.time()
                self.time = et - st

        et = time.time()
        self.time = et - st
        print('FINISHED')
        self.create_plots()
        self.best_individuals = []
        self.use_metaheuristics = str(self.use_metaheuristics)
        res = requests.patch(
            "https://obliczenia-ewolucyjne-default-rtdb.europe-west1.firebasedatabase.app/algoruns.json",
            json={self.process_id: self.__dict__})
        self.use_metaheuristics = False

    def create_plots(self):
        path = os.path.join(os.path.pardir, "react-app", "public", "plots", self.process_id)
        os.mkdir(path)
        if self.use_metaheuristics:
            plt.plot(self.best_values)
            plt.xlabel('Epoka')
            plt.ylabel('Wartość funkcji')
            plt.title('Wartość funkcji celu dla najlepszego osobnika w kolejnych epokach')
            plt.savefig(os.path.join(path, 'best_individuals_plot.jpg'))
            plt.clf()

            data = np.array(self.best_individuals)

            plt.plot(data[:, 0], data[:, 1])
            plt.xlabel('x1')
            plt.ylabel('x2')
            plt.savefig(os.path.join(path, 'mean_plot.jpg'))
            plt.clf()
        else:
            plt.plot([self.himmelblau_function(x1, x2) for (x1, x2) in self.best_individuals])
            plt.xlabel('Epoka')
            plt.ylabel('Wartość funkcji')
            plt.title('Wartość funkcji celu dla najlepszego osobnika w kolejnych epokach')
            plt.savefig(os.path.join(path, 'best_individuals_plot.jpg'))
            plt.clf()

            X = np.array(self.population_values)

            plt.plot(X.mean(axis=1))
            plt.xlabel('Epoka')
            plt.ylabel('Średnia wartość funkcji')
            plt.title('Średnia wartość funkcji celu dla populacji')
            plt.savefig(os.path.join(path, 'mean_plot.jpg'))
            plt.clf()

            plt.plot(X.std(axis=1))
            plt.xlabel('Epoka')
            plt.ylabel('Odchylenie standardowe')
            plt.title('Wartość odchylenia standardowego funkcji celu dla populacji')
            plt.savefig(os.path.join(path, 'std_plot.jpg'))
            plt.clf()
