import random
import numpy as np


def Tournament_Selection(pool_size):
    # Tournament: select randon n individuals, choose the best

    def inner_TS(pop, fitness, max_):

        if max_:
            evaluators = np.argmax
        else:
            evaluators = np.argmin

        # select index to pick from population
        torunamet_pool_index = random.choices(range(len(pop)), k=pool_size)

        # calculate fitness of individuals
        pool_fit = [fitness[i] for i in torunamet_pool_index]

        # discover index of best individual of tournament
        index = torunamet_pool_index[evaluators(pool_fit)]

        # choose the best individual
        return pop[index]

    return inner_TS
