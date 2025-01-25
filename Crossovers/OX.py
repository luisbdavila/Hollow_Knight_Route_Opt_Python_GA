import random


def OX(parent1, parent2):

    p1 = parent1[1:-1].copy()
    p2 = parent2[1:-1].copy()
    # copy of the parent without first an last element

    i_start = random.randint(0, len(p1) - 2)
    # Randomizing the start of the section to cut
    i_end = random.randint(i_start + 1, len(p1) - 1)
    # Randomizing the end of the section to cut

    of1 = [0]*i_start + p2[i_start:i_end] + [0]*(len(p1)-i_end)
    of2 = [0]*i_start + p1[i_start:i_end] + [0]*(len(p2)-i_end)
    # swicth the midel part between parents

    path1 = p1[i_end:] + p1[:i_end]
    path2 = p2[i_end:] + p2[:i_end]
    # have the predifined path

    counter1, counter2 = 0, 0
    # keep track of the element in the path to add

    for indexx in range(i_end, len(p1)):
        # start from the end

        while path1[counter1] in of1:
            counter1 += 1
        # if the element already exist them go to next one

        while path2[counter2] in of2:
            counter2 += 1
        # if the element already exist them go to next one

        of1[indexx] = path1[counter1]
        of2[indexx] = path2[counter2]
        # add the element of the path to the ofsrpint

    for indexx in range(i_start):
        # keep adding to the front

        while path1[counter1] in of1:
            counter1 += 1
        # if the element already exist them go to next one

        while path2[counter2] in of2:
            counter2 += 1
        # if the element already exist them go to next one

        of1[indexx] = path1[counter1]
        of2[indexx] = path2[counter2]
        # add the element of the path to the ofsrpint

    return ['D'] + of1 + ['D'], ['D'] + of2 + ['D']
