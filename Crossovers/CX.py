import random


def CX(parent1, parent2):

    # select the random index to start filling
    i_start = random.randint(1, len(parent1) - 2)

    # define each ofsrpint with same lenght as the parents
    of1, of2 = [0]*len(parent1), [0]*len(parent1)

    i_search = i_start

    # start filling the of1 with the values of parent1 until the cycle ends
    while parent1[i_search] not in of1:
        of1[i_search]= parent1[i_search]
        # look for the correspondence in parent2, then
        # search for the respective index in parent1
        i_search = parent1.index(parent2[i_search])

    i_search = i_start

    # start filling the of1 with the values of parent2 until the cycle ends
    while parent2[i_search] not in of2:
        of2[i_search] = parent2[i_search]
        # look for the correspondence in parent2, then
        # search for the respective index in parent1
        i_search = parent2.index(parent1[i_search])

    # fill the rest of the places with the oposite parent
    for indexx in range(len(parent1)):
        # fill if is still empty

        if of1[indexx] == 0:
            of1[indexx] = parent2[indexx]

        if of2[indexx] == 0:
            of2[indexx] = parent1[indexx]

    return of1, of2
