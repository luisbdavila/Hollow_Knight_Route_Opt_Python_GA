import random
import numpy as np
from sklearn.preprocessing import normalize


def Self_Adaptive_Tournament_Selection(init_pool_size):
    # Tournament: select randon n individuals, choose the best
    #             (bigger n if fitnesses are alike, smaller otherwise)

    def inner_SATS(pop, fitness, max_):

        if max_:
            evaluators = np.argmax
        else:
            evaluators = np.argmin

        # fitness distribution will be between 0-1 (because is normalize)
        # standard deviation will be between 0 and 0.5
        # large std -> large pool -> large selection presure
        # small std -> small pool -> small selection presures
        pool_size = round((init_pool_size) * np.std(normalize([fitness])[0]), 0)

        # to have at least a tournament of 2 individuals.
        if pool_size < 2:
            pool_size = 2

        # select index to pick from population
        torunamet_pool_index = random.choices(range(len(pop)), k=pool_size)

        # calculate fitness of individuals
        pool_fit = [fitness[i] for i in torunamet_pool_index]

        # discover index of best individual of tournament
        index = torunamet_pool_index[evaluators(pool_fit)]

        # choose the best individual
        return pop[index]

    return inner_SATS
