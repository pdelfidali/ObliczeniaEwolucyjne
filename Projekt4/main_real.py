import random
import time

import matplotlib.pyplot as plt
from deap import base
from deap import creator
from deap import tools
import crossovers_real

minValue = -10
maxValue = 10
bitsLength = 20
sizePopulation = 100
probabilityMutation = 0.2
probabilityCrossover = 0.8
numberIteration = 100



def individual(icls):
    genome = list()
    genome.append(random.uniform(-10, 10))
    genome.append(random.uniform(-10, 10))
    return icls(genome)


def decode_ind(_individual):
    return _individual[0], _individual[1]


mutation_dict = {
    'gaussian': tools.mutGaussian,
    'uniformInt': tools.mutUniformInt,
}


def fitness_function(_individual):
    x1, x2 = decode_ind(_individual)
    result = (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2
    return result,


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register('individual', individual, creator.Individual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', fitness_function)

toolbox.register('select', tools.selWorst)
# toolbox.register('select', tools.selRoulette)
# toolbox.register('select', tools.selRoulette)

# toolbox.register("mate", crossovers_real.cxArithmetic)
toolbox.register("mate", crossovers_real.cxLinear)
# toolbox.register("mate", crossovers_real.cxBlendAlpha)
# toolbox.register("mate", crossovers_real.cxBlendAlphaBeta)
# toolbox.register("mate", crossovers_real.cxAverage)


# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=3, indpb=0.3)
toolbox.register("mutate", tools.mutUniformInt, low=minValue, up=maxValue, indpb=0.3)



pop = toolbox.population(n=sizePopulation)
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

g = 0
min_data = []
max_data = []
avg_data = []
std_data = []
numberElitism = 0
t_start = time.time()
while g < numberIteration:
    g = g + 1
    print("-- Generation %i --" % g)
    # Select the next generation individuals
    offspring = toolbox.select(pop, len(pop))
    # Clone the selected individuals
    offspring = list(map(toolbox.clone, offspring))

    listElitism = []
    for x in range(0, numberElitism):
        listElitism.append(tools.selBest(pop, 1)[0])

    # Apply crossover and mutation on the offspring
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        # cross two individuals with probability CXPB
        if random.random() < probabilityCrossover:
            toolbox.mate(child1, child2)
            # fitness values of the children
            # must be recalculated later
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        # mutate an individual with probability MUTPB
        if random.random() < probabilityMutation:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(invalid_ind))
    pop[:] = offspring + listElitism
    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5
    min_data.append(min(fits))
    max_data.append(max(fits))
    avg_data.append(mean)
    std_data.append(std)
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)
runtime = time.time() - t_start
print(f"{runtime * 1000:.2f} ms & {min(fits):.5f} & {sum(std_data) / len(std_data):.2f}")
best_ind = tools.selBest(pop, 1)[0]
print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
print("-- End of (successful) evolution --")
plt.figure(figsize=(7, 7))
plt.subplot(2, 2, 1)
plt.plot(avg_data, label='Średnia')
plt.title("Średnia")
plt.subplot(2, 2, 2)
plt.title("Wartość minimalna")
plt.plot(min_data, label='Minimum')
plt.subplot(2, 2, 3)
plt.plot(max_data, label='Maksimum')
plt.title("Wartość maksymalna")
plt.subplot(2, 2, 4)
plt.plot(std_data)
plt.title("Wartość odchylenia standardowego")
plt.show()
