import random


def Fitness_Proportional_Selection(population, fitnesses, max_):
    # Fitness proportional: order by fitness, calculate probaility,
    #                       choose individual

    # sum fitness
    sum_fit = sum(fitnesses)

    if max_:
        # choose individual based on fitness
        return random.choices(population, weights=[fitness/sum_fit for fitness in fitnesses])[0]

    else:
        # choose individual based on fitness
        return random.choices(population, weights=[1 - (fitness/sum_fit) for fitness in fitnesses])[0]
