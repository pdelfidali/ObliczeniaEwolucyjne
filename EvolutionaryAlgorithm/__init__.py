from Assumptions import Assumptions
from functions.population import select_new_parents, crossover_population, mutate_population, init_random_population

if __name__ == '__main__':
    # config program
    assumptions = Assumptions()
    assumptions.set_assumptions(-10, 10, precision=6, population_size=10, goal_function=lambda x, y: x+y)

    # init population
    population = init_random_population()

    # evaluate (is in selection algorithms)
    # selection of next parents
    parents = select_new_parents(population)

    # crossover of parents
    children = crossover_population(parents)

    # mutation of children
    children = mutate_population(children)

    # join together to form next population
    population = parents + children

    #TODO: missing elite strategy somewhre above

    # ending condition (e.g. run out of epoch) # yes -> end | no -> selection (with best dude strategy)

    print([p.as_decimal_pair() for p in population])
    print('end')
