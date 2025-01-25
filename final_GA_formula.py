from GeneralFormulas.Generalform_GA import Genetic_Algorithm
from GeneralFormulas.Population import Random_Population
from GeneralFormulas.FitnessCalculation import Fitness_Population

from Selection.SelfAdaptiveTournament import Self_Adaptive_Tournament_Selection

from Crossovers.CX import CX

from Mutations.swap import swap


def Best_Path_In_Game(Input_your_matrix_here):

    # Calculate the best path using our GA
    best_individual, fitness_indivifual = Genetic_Algorithm(initializer=Random_Population,
                                        population_size=800,
                                        evaluator=[Fitness_Population(False, False), "No Sharing"],
                                        dataset=[Input_your_matrix_here, "Your Matrix"],
                                        generations=500,
                                        crossover_operator=[CX, "CX"],
                                        p_xo=0.5,
                                        mutation=[swap, "swap"],
                                        selection=[Self_Adaptive_Tournament_Selection(25), "Self_Adaptive_Tournament 25"],
                                        maximization=True,
                                        elitism=True,
                                        verbose=False,
                                        log=None,
                                        seed=23)

    # Diccionary of cities
    cities_dic = {'D': 'Dirtmouth (D)',
                  'FC': 'Forgotten Crossroads (FC)',
                  'G': 'Greenpath (G)', 
                  'QS': "Queen's Station (QS)", 
                  'QG': "Queen's Garden's (QG)", 
                  'CS': 'City Storerooms (CS)', 
                  'KS': "King's Station (KS)", 
                  'RG': 'Resting Grounds (RG)', 
                  'DV': 'Distant Village (DV)', 
                  'SN': 'Stag Nest (NS)'}

    # A nice print for the user
    print('Follow the following path (is the best one):')

    for city in best_individual:
        if city in cities_dic:
            print(f"{cities_dic[city]} ")

    # The solution and its fitness if is needed
    return best_individual, fitness_indivifual
