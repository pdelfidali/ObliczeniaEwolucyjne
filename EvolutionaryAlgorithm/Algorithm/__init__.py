import os
import time
import uuid

import numpy as np
from matplotlib import pyplot as plt
import math

from Assumptions import Assumptions
from Chromosome import Chromosome
from functions.bits_crossover import one_point_crossover, three_point_crossover, two_point_crossover, \
    homogeneous_crossover
from functions.bits_mutation import one_point_mutation, two_point_mutation, edge_mutation, inversion_mutation
from functions.population import select_new_parents, crossover_population, mutate_population, init_random_population
from functions.selection import rank_selection, tournament_selection, roulette_wheel_selection


class Algorithm:
    best_individuals: list[tuple[float, float]]
    population_values: list[list]
    time: float
    epoch: int
    filename: str
    assumptions_json: dict

    def __init__(self):
        self.process_id = None
        self.best_individuals = []
        self.population_values = []
        self.time = 0
        self.epoch = 0
        self.assumptions_json = None

    @staticmethod
    def get_goal_function():
        return Algorithm.himmelblau_function

    @staticmethod
    def himmelblau_function(x1, x2):
        return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2

    @staticmethod
    def mcCormick_function(x1, x2):
        return math.sin(x1 + x2) + (x1 - x2) ** 2 - 1.5 * x1 + 2.5 * x2 + 1

    @staticmethod
    def crossover_config(key: str):
        crossover_name_mapper = {
            'one': one_point_crossover,
            'two': two_point_crossover,
            'three': three_point_crossover,
            'homo': homogeneous_crossover
        }
        return crossover_name_mapper[key]

    @staticmethod
    def mutation_config(key: str):
        mutation_name_mapper = {
            'one': one_point_mutation,
            'two': two_point_mutation,
            'edge': edge_mutation,
            'inv': inversion_mutation
        }
        return mutation_name_mapper[key]

    @staticmethod
    def selection_config(key: str):
        selection_name_mapper = {
            'rank': rank_selection,
            'tournament': tournament_selection,
            'roulette': roulette_wheel_selection
        }
        return selection_name_mapper[key]

    def append_individual(self, individual: Chromosome):
        self.best_individuals.append((individual.x1.decimalRepresentation, individual.x2.decimalRepresentation))

    def append_epoch_values(self, population: list[Chromosome]):
        epoch_values = list(map(lambda ch: ch.get_goal_function_value(), population))
        self.population_values.append(epoch_values)

    @staticmethod
    def config_program(assumptions_config):
        assumptions = Assumptions()

        assumptions.set_assumptions(
            min_value=assumptions_config['minValue'],  # renamed
            max_value=assumptions_config['maxValue'],  # renamed
            bits_length=1,  # placeholder | this value has to be provided but is overriden below

            population_size=assumptions_config['populationSize'],
            epochs=assumptions_config['epochsAmount'],
            elite_strategy=assumptions_config['eliteStrategy'],  # added

            mutation_probability=assumptions_config['mutationProbability'],
            mutation_func=Algorithm.mutation_config(assumptions_config['mutationType']),

            crossover_probability=assumptions_config['crossoverProbability'],
            crossover_func=Algorithm.crossover_config(assumptions_config['crossoverType']),

            selection_func=Algorithm.selection_config(assumptions_config['selectionType']),

            goal_function=Algorithm.get_goal_function(),
            optimization_mode=assumptions_config['optimizationMode'],  # added maximising / minimising
        )
        assumptions.set_selection_params(assumptions_config['selectionType'], assumptions_config['selectionValue'])
        assumptions.set_precision_type(assumptions_config['precisionType'], assumptions_config['precisionVal'])

    def run(self):
        assumptions = Assumptions()

        # start the timer
        st = time.time()
        population = init_random_population()

        self.process_id = f"{uuid.uuid1()}"
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
        requests.post("https://obliczenia-ewolucyjne-default-rtdb.europe-west1.firebasedatabase.app/algoruns.json",
                      json={"algo": self.__dict__})

    def create_plots(self):
        path = os.path.join(os.path.pardir, "react-app", "public", "plots", self.process_id)
        os.mkdir(path)

        plt.plot(self.best_individuals)
        plt.xlabel('Epoka')
        plt.ylabel('Wartość funkcji')
        plt.title('Wartość funkcji celu dla najlepszego osobnika w kolejnych epokach')
        plt.savefig(os.path.join(path, 'best_individuals_plot.jpg'))
        plt.clf()

        X = np.array(self.population_values)

        plt.plot(X.mean(axis=1))
        plt.xlabel('Epoka')
        plt.ylabel('Średnia wartość funkcji')
        plt.title('Średnia wartość funkcji celu dla populacji w kolejnych epokach')
        plt.savefig(os.path.join(path, 'mean_plot.jpg'))
        plt.clf()

        plt.plot(X.std(axis=1))
        plt.xlabel('Epoka')
        plt.ylabel('Odchylenie standardowe')
        plt.title('Wartość odchylenia standardowego dla funkcji celu dla populacji w kolejnych epokach')
        plt.savefig(os.path.join(path, 'std_plot.jpg'))
        plt.clf()

    def set_assumptions_json(self, assumptions):
        self.assumptions_json = assumptions
