from Assumptions import Assumptions
from functions.population import select_new_parents, init_population, crossover_population, mutate_population

if __name__ == '__main__':
    # config program
    assumptions = Assumptions()
    assumptions.set_assumptions(-10, 10, precision=6)

    # init population
    population = init_population(10)

    # evaluate (is in selection algorithms)
    # selection
    population = select_new_parents(population)

    # crossover
    population = crossover_population(population)
    # mutation
    population = mutate_population(population)
    # ending condition (e.g. run out of epoch) # yes -> end | no -> selection (with best dude strategy)

    print('s')
