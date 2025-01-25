import numpy as np
from GeneralFormulas.Constraints import Check_RG_First_Part, Check_QG_CS


def Hamming_distance(ind1, ind2):
    distance = 0
    # Initializing the distance to 0
    for i in range(len(ind1)):
        if ind1[i] != ind2[i]:
            distance += 1
    # Iterating through the individual and counting the
    # differences in correspondent bits
    return distance


def Sharing(ind, pop, mean_):
    if mean_:
        result = np.mean([Hamming_distance(ind, ind2) for ind2 in pop])
        return result
    # If the mean parameter is true, the mean hamming distance between
    # the indivdual and all other is calculated
    else:
        result = np.sum([Hamming_distance(ind, ind2) for ind2 in pop])
        return result
    # If the mean parameter is false, the sum of all hamming distances between
    # the indivdual and all other is calculated


def Fitness_individual(indi, pop, M, sharing_, sharing_mean):
    d = {'D': 0, 'FC': 1, 'G': 2, 'QS': 3, 'QG': 4,
         'CS': 5, 'KS': 6, 'RG': 7, 'DV': 8, 'SN': 9}
    # This dictionary is used to connect the solutions
    # to the Matrix of gains/losses
    ind = [bit for bit in indi if bit in d.keys()]
    lowest_value = abs(10*np.min(M)) + 1
    # Removing elements in lower case(to be ignored in our implementation)
    # The evaluation of whether to skip KS is performed in the population
    # fitness function
    if Check_RG_First_Part(ind) or Check_QG_CS(ind):
        # Checking constraints for infeasible solutions
        return 1
        # If the solution is infeasible its fitness is 1
        # More detailed explanation below
    else:
        if sharing_:
            # If fitness sharing is enabled the paramaters are passed through
            # and the regular fitness is multiplied by the sharing
            return Sharing(ind, pop, sharing_mean) *\
                (sum([M[d[ind[i]]][d[ind[i + 1]]]
                      for i in range(len(ind) - 1)])
                 + lowest_value)
        else:
            return sum([M[d[ind[i]]][d[ind[i + 1]]]
                        for i in range(len(ind) - 1)])\
                        + lowest_value
        # If the solution is feasible we use d to index the matrix to get the
        # gain/loss of moving from one area to another and then sum 10 times
        # the lowest geo loss in the matrix + 1, this way all individuals have
        # positive fitness (Essentially defining 10 times
        # the lowest geo loss in the matrix as the lowest fitness
        # (used for infeasible solutions) and then adding that value + 1 to the
        # fitness of all individuals, to keep the scale unchanged)


def Fitness_Population(sharing_, sharing_mean):
    def inner_FP(population, Mat):
        return [Fitness_individual(indi, population, Mat,
                sharing_, sharing_mean) if 'ks' not in indi else
                max(Fitness_individual(indi, population, Mat,
                    sharing_, sharing_mean),
                    Fitness_individual(list(map(str.upper, indi)), population,
                    Mat, sharing_, sharing_mean))
                for indi in population]
    return inner_FP
    # Iterating through the population and
    # calculating the fitness of each indivual
    # with the condition that if there is a lower case
    # 'ks' in an individual the options of skipping KS
    # and not skipping are both evaluated and the maximum value is
    # taken
