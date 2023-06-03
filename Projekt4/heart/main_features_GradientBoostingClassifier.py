import pandas as pd

df=pd.read_csv("heart.csv",sep=',')
df.head()

y=df['target']
df.drop('target',axis=1,inplace=True)
numberOfAtributtes= len(df.columns)
# print(numberOfAtributtes) 

from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier

# GradientBoostingClassifier


mms = MinMaxScaler()
df_norm = mms.fit_transform(df)
clf = GradientBoostingClassifier()
scores = model_selection.cross_val_score(clf, df_norm, y,
cv=5, scoring='accuracy',
n_jobs=-1)
# print(scores.mean()) 

import random

def GBCParametersFeatures(numberFeatures,icls):
    genome = list()

    # n_estimators
    learning_rate = random.uniform(0.0, 1)
    genome.append(learning_rate)

    # criterion
    loss = ["log_loss","exponential"]
    genome.append(loss[random.randint(0, 1)])

    # max_depth
    n_estimators = random.randint(10,100)
    genome.append(n_estimators)
    
    # max_features
    max_depth = random.randint(2,6)
    genome.append(max_depth)
    
    # for i in range(0,numberFeatures):
    #     genome.append(random.randint(0, 1))

    return icls(genome)


import math
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold

def GBCDefault(y,df):
    split=5
    cv = StratifiedKFold(n_splits=split)
    mms = MinMaxScaler()
    df_norm = mms.fit_transform(df)

    estimator = GradientBoostingClassifier()
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected,predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn) #w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrixterminology/
    resultSum = resultSum + result #zbieramy wyniki z poszczególnychetapów walidacji krzyżowej
    return resultSum / split,

def GBCParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = StratifiedKFold(n_splits=split)
    mms = MinMaxScaler()
    df_norm = mms.fit_transform(df)

    estimator = GradientBoostingClassifier(learning_rate=individual[0],loss=individual[1],n_estimators=individual[2],max_depth=individual[3])
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected,predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn) #w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrixterminology/
    resultSum = resultSum + result #zbieramy wyniki z poszczególnychetapów walidacji krzyżowej
    return resultSum / split,

def GBCParametersFeatureFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = StratifiedKFold(n_splits=split)

    listColumnsToDrop=[] #lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0: #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = GradientBoostingClassifier(learning_rate=individual[0],loss=individual[1],n_estimators=individual[2],max_depth=individual[3]) 

    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected, predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn) #w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrixterminology/
        resultSum = resultSum + result #zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationGBC(individual):
    numberParamer= random.randint(0,len(individual)-1)

    if numberParamer==0:
        #learning_ratefloat
        learning_rate = random.uniform(0.0, 1)
        individual[0]=learning_rate
    elif numberParamer==1:
        # loss
        loss = ["log_loss","exponential"]
        individual[1] = loss[random.randint(0, 1)]
    elif numberParamer == 2:
        # max_depth
        n_estimators = random.randint(10,100)
        individual[2]=n_estimators
    elif numberParamer == 3:
        # max_features
        max_depth = random.randint(2,6)
        individual[3]= max_depth
    # else: #genetyczna selekcja cech
    #     if individual[numberParamer] == 0:
    #         individual[numberParamer] = 1
    #     else:   
    #         individual[numberParamer] = 0

import time 

import matplotlib.pyplot as plt
from deap import base
from deap import creator
from deap import tools

minValue = -10
maxValue = 10
bitsLength = 20
sizePopulation = 10
probabilityMutation = 0.2
probabilityCrossover = 0.8
numberIteration = 5

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register('individual',GBCParametersFeatures, numberOfAtributtes, creator.Individual) # PROJEKT 4
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", GBCParametersFitness,y,df,numberOfAtributtes) # PROJEKT 4

toolbox.register('select', tools.selWorst)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", mutationGBC) # PROJEKT 4

if __name__ == "__main__":  

    pop = toolbox.population(n=sizePopulation)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        print(ind)
        ind.fitness.values = fit


    g = 0
    min_data = []
    max_data = []
    avg_data = []
    std_data = []
    numberElitism = 1
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
        # print("  Min %s" % min(fits))
        # print("  Max %s" % max(fits))
        # print("  Avg %s" % mean)
        # print("  Std %s" % std)
    runtime = time.time() - t_start
    print(f"{runtime * 1000:.2f} ms & {min(fits):.5f} & {sum(std_data)/len(std_data):.2f}")
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    print("-- End of (successful) evolution --")
    plt.figure(figsize=(7, 7))
    plt.subplot(2,2,1)
    plt.plot(avg_data, label='Średnia')
    plt.title("Średnia")
    plt.subplot(2,2,2)
    plt.title("Wartość minimalna")
    plt.plot(min_data, label='Minimum')
    plt.subplot(2,2,3)
    plt.plot(max_data, label='Maksimum')
    plt.title("Wartość maksymalna")
    plt.subplot(2,2,4)
    plt.plot(std_data)
    plt.title("Wartość odchylenia standardowego")
    # plt.show()
