from Assumptions import Assumptions
from functions.population import select_new_parents, crossover_population, mutate_population, init_random_population


def goal_f(x, y):
    return x + y


if __name__ == '__main__':
    # config program
    assumptions = Assumptions()
    assumptions.set_assumptions(-10, 10, 4, precision=6, population_size=8, goal_function=goal_f, epochs=5)
    assumptions.set_selection_params('rank_selection', 0.3)
    epochs = assumptions.epochs

    # init population
    population = init_random_population()
    print(f'{population=}')

    for _ in range(epochs):
        print('# BEGIN GENERATION')
        # evaluate the best individual of this generation
        best_individual = max(population, key=lambda x: x.get_goal_function_value())  # TODO: max or min parameter?

        # selection of next parents
        parents = select_new_parents(population)

        # crossover of parents
        children = crossover_population(parents)

        # mutation of children
        children = mutate_population(children)

        # form next population
        population = children

        print(f'{best_individual.__repr__()=}')
        print(f'{population=}')

        # print([{p.as_decimal_pair(), f'__{p.get_goal_function_value()}__'} for p in population])
        # print(best_individual.as_decimal_pair(), best_individual.get_goal_function_value())

        print(best_individual not in population)
        # apply elitism strategy
        if best_individual not in population:
            population[-1] = best_individual



        print([{p.as_decimal_pair(), p.get_goal_function_value()} for p in population])

        # ending condition (e.g. run out of epoch) # yes -> end | no -> selection (with best dude strategy)
        print('end')
