import random


def rank_selection(pop, fitness, maximization):
    # Rank: order by fitness, define the rank,
    #       calculate probaility, choose individual

    # sum of ranks
    total_rank = len(pop) * (len(pop) + 1) / 2

    if maximization:
        # sort larger to smaller
        union = sorted(list(zip(fitness, pop)), reverse=True)
    else:
        # sort smaller to smaller
        union = sorted(list(zip(fitness, pop)), reverse=False)

    # define the probability list for each individual
    probabilities_list = [(index + 1) / total_rank for index, indi_fit in enumerate(union)]

    # chose one solution
    return random.choices(union, weights=probabilities_list)[0][1]
