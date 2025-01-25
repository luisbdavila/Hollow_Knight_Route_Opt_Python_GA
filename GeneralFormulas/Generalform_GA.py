import random
import numpy as np
from copy import deepcopy
import csv
from GeneralFormulas.Constraints import Check_QS_DV_Not_KS


def Genetic_Algorithm(initializer,
                      population_size,
                      evaluator,
                      dataset,
                      generations,
                      crossover_operator,
                      p_xo,
                      mutation,
                      selection,
                      maximization,
                      elitism,
                      verbose,
                      log,
                      seed):

    # define randon seed
    random.seed(seed)

    # if the problem is a maximixation or minimization
    if maximization:
        evaluators = [max, np.argmax]
    else:
        evaluators = [min, np.argmin]

    # initialize the population
    population = initializer(population_size)
    # calculate the fitness
    fitnesses = evaluator[0](population, dataset[0])

    # if we want to print the generation and best individual
    if verbose:
        print('Initializing the population')
        print(0, evaluators[0](fitnesses))

    # start the GA algorithm
    for generation_index in range(generations):

        # if we use elitism or not
        if elitism:
            # initialize the offspring population
            # and save the best individual so far
            offspring_pop = [population[evaluators[1](fitnesses)]]
        else:
            # initialize the offspring population
            offspring_pop = []

        # keep adding individuals untill is full
        while len(offspring_pop) < len(population):

            # select parent1 and parent2
            p1 = selection[0](population, fitnesses, maximization)
            p2 = selection[0](population, fitnesses, maximization)

            # transform to upper case
            p1 = list(map(str.upper, p1))
            p2 = list(map(str.upper, p2))

            # choose if crosover is aplied
            if random.random() <= p_xo:
                o1, o2 = crossover_operator[0](p1, p2)

            # or reproduction is aplied
            else:
                o1, o2 = deepcopy(p1), deepcopy(p2)

            # aply mutation to the offsprings
            o1 = mutation[0](o1)
            o2 = mutation[0](o2)

            # check if Queen’s Station (QS) before Distant Village (DV)
            # change KS to ks
            Check_QS_DV_Not_KS(o1)
            Check_QS_DV_Not_KS(o2)

            # add the offsprings to the population
            offspring_pop.extend([o1, o2])

        # to have the same number of individuals as the parent population
        offspring_pop = offspring_pop[:population_size]

        # sustitute the parent population
        population = offspring_pop
        # evaluate the fitness of the new population
        fitnesses = evaluator[0](offspring_pop, dataset[0])

        # saving the results of each interation
        if log is not None:
            with open(log, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([seed,
                                 evaluator[1],
                                 generation_index,
                                 population_size,
                                 generations,
                                 elitism,
                                 dataset[1],
                                 crossover_operator[1],
                                 p_xo,
                                 mutation[1],
                                 selection[1],
                                 # best fitness
                                 evaluators[0](fitnesses),
                                 # best individual  
                                 population[evaluators[1](fitnesses)]])

        # if we want to print the generation and best individual
        if verbose:
            print(generation_index+1, evaluators[0](fitnesses))

    best_ind = population[evaluators[1](fitnesses)]
    best_ind_f = evaluators[0](fitnesses)

    # return the  best solution of the GA, with the fitness
    # If a lower case 'ks' is in the individual then we compare the
    # its fitness to its fitness with the 'KS', if they're equal
    # that means the skip is not performed and the best individual is
    # returned with an upper case 'ks', if it's different the skip is
    # performed and the indvidual is returned with a lower case 'ks'
    if 'ks' in best_ind:
        if evaluator[0](list(map(str.upper, best_ind)), dataset[0])[0] == best_ind_f:
            return list(map(str.upper, best_ind)), best_ind_f
        else:
            return best_ind, best_ind_f
    else:
        return best_ind, best_ind_f
