import random
from GeneralFormulas.Constraints import Check_QS_DV_Not_KS


def Indiviual():
    places = ['FC', 'G', 'QS', 'QG', 'CS', 'KS', 'RG', 'DV', 'SN']
    indv = ['D'] + random.sample(places, k=len(places)) + ['D']
    # Randomly selecting the areas without replacement
    # to obtain a list of 11 areas where all areas appear
    # only once (except Dirtmouth)
    Check_QS_DV_Not_KS(indv)

    return indv


def Random_Population(length_population):
    return [Indiviual() for _ in range(length_population)]
    # Using list comprehension to create a list of individuas
    # of a specified length
