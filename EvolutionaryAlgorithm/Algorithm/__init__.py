from Assumptions import Assumptions
from Chromosome import Chromosome
from functions.bits_crossover import one_point_crossover, three_point_crossover, two_point_crossover, \
    homogeneous_crossover
from functions.bits_mutation import one_point_mutation, two_point_mutation, edge_mutation, inversion_mutation
from functions.population import select_new_parents, crossover_population, mutate_population, init_random_population
from functions.selection import rank_selection, tournament_selection, roulette_wheel_selection
import time


class Algorithm:
    best_individuals: list[tuple[float, float]]
    population_values: list[list]
    time: float

    def __init__(self):
        self.best_individuals = []
        self.population_values = []
        self.time = 0

    @staticmethod
    def goal_function(x1, x2):
        return x1 + x2

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

    def config_program(self, assumptions_config):
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

            goal_function=Algorithm.goal_function,
            optimization_mode=assumptions_config['optimizationMode'],  # added maximising / minimising
        )
        assumptions.set_selection_params(assumptions_config['selectionType'], assumptions_config['selectionValue'])
        assumptions.set_precision_type(assumptions_config['precisionType'], assumptions_config['precisionVal'])

    def run(self):
        assumptions = Assumptions()

        # start the timer
        st = time.time()
        population = init_random_population()

        for _ in range(assumptions.epochs):
            print(f'BEGIN GENERATION #{_}')
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

            print([{p.as_decimal_pair(), p.get_goal_function_value()} for p in population])

        et = time.time()
        self.time = et - st
        print('FINISHED')

    def execute(self, assumptions_config):
        self.config_program(assumptions_config)
        self.run()


if __name__ == '__main__':
    assumptions_payload = {
        'minValue': -10,
        'maxValue': 10,
        'precisionType': 'bits_length',
        'precisionVal': 20,
        'populationSize': 10,
        'epochsAmount': 10,
        'crossoverType': "one",
        'crossoverProbability': 0.5,
        'mutationType': "one",
        'mutationProbability': 0.5,
        'eliteStrategy': True,
        'selectionType': "rank",  # roulette | rank | tournament
        'selectionValue': 4,
        'optimizationMode': 'min'
    }

    algorithm = Algorithm()
    algorithm.execute(assumptions_payload)

    print(f'{algorithm.time=}')
    print(f'{algorithm.best_individuals=}')
    print(f'{algorithm.population_values=}')
    assumptions = Assumptions()
    print(assumptions.selection_params)
    print(assumptions.selection_func)
    print(f'{algorithm.best_individuals[-1]=}')
