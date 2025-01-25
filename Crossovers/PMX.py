import random


def PMX(parent1, parent2):

    p1 = parent1[1:-1].copy()
    p2 = parent2[1:-1].copy()
    # copy of the parent without first an last element

    i_start = random.randint(0, len(p1) - 2)
    # Randomizing the start of the section to cut
    i_end = random.randint(i_start + 1, len(p1) - 1)
    # Randomizing the end of the section to cut
    of1 = [0]*i_start + p2[i_start:i_end] + [0]*(len(p1)-i_end)
    of2 = [0]*i_start + p1[i_start:i_end] + [0]*(len(p2)-i_end)
    # swap one part between ofsrpint

    for indexx in range(len(p1)):
        # consider only the part that is not swaped
        if indexx not in range(i_start, i_end):

            # If the value is not in the swaped part
            if p1[indexx] not in of1:
                of1[indexx] = p1[indexx]

            # Else, see the correspondence
            else:
                keep_1 = True
                index_1 = indexx
                while keep_1:
                    if p1[p2.index(p1[index_1])] not in of1:
                        of1[indexx] = p1[p2.index(p1[index_1])]
                        keep_1 = False
                
                    else:
                        index_1 = p2.index(p1[index_1])

            # If the value is not in the swaped part
            if p2[indexx] not in of2: 
                of2[indexx] = p2[indexx]

            # Else, see the correspondence
            else:
                keep_2 = True
                index_2 = indexx
                while keep_2:
                    if p2[p1.index(p2[index_2])] not in of2:
                        of2[indexx] = p2[p1.index(p2[index_2])]
                        keep_2 = False

                    else:
                        index_2 = p1.index(p2[index_2])
                # fill the ofsprint with the value of the parent if alreday
                # have that value, put the correspondence of the swap
                # in the offspring

    return ['D'] + of1 + ['D'], ['D'] + of2 + ['D']
