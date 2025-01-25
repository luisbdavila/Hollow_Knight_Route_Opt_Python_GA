import random


def PBX(parent1, parent2):

    indexes_to_maintaing = random.sample(range(1, len(parent1) - 1), k=random.randint(2, len(parent1) - 2))
    # select k indexes not considering the first and last

    values_for_p1 = [parent2[indexx] for indexx in indexes_to_maintaing]
    values_for_p2 = [parent1[indexx] for indexx in indexes_to_maintaing]
    # have the elements to maintaing in each parent

    of1, of2 = [], []

    counter1, counter2 = 0, 0
    # to keep track of the parent index to add
    for indexx in range(len(parent1)):
        # if the index was selected is the value for the other parent
        if indexx in indexes_to_maintaing:
            of1.append(parent2[indexx])
            of2.append(parent1[indexx])

        else:
            # choose the next valid index of the parent to insert 
            while parent1[counter1] in values_for_p1:
                counter1 += 1

            # if the index was not selected and the value was not used
            # append the next value of the parent
            of1.append(parent1[counter1])
            # go to next value
            counter1 += 1

            # choose the next valid index of the parent to insert 
            while parent2[counter2] in values_for_p2:
                counter2 += 1

            # if the index was not selected and the value was not used
            # append the next value of the parent
            of2.append(parent2[counter2])
            # go to next value
            counter2 += 1

    return of1, of2
