import random


def OBX(parent1, parent2):

    indexes_to_move = random.sample(range(1, len(parent1) - 1),
                                    k=random.randint(2, len(parent1) - 2))
    # select k indexes not considering the first and last
    indexes_to_move.sort()
    # Sorting the indexes to guarantee they are in order

    values_for_p1 = [parent2[indexx] for indexx in indexes_to_move]
    values_for_p2 = [parent1[indexx] for indexx in indexes_to_move]
    # have the elements to maintaing in each parent

    of1, of2 = [], []

    counter1, counter2 = 0, 0
    # keep track of the element indexes to add

    for indexx in range(len(parent1)):

        if parent1[indexx] in values_for_p1:
            of1.append(values_for_p1[counter1])
            counter1 += 1
            # If the element was chosen put it in the order of the other parent
        else:
            of1.append(parent1[indexx])
        # Else, put the element of the  parent

        if parent2[indexx] in values_for_p2:
            of2.append(values_for_p2[counter2])
            counter2 += 1
        # If the element was chosen put it in the order of the other parent
        else:
            of2.append(parent2[indexx])
        # Else, put the element of the  parent

    return of1, of2

