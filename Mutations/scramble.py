import random


def scramble(ind):
    i_start = random.randint(1, len(ind) - 3)
    # Randomizing the start of the section to scramble
    i_end = random.randint(i_start + 1, len(ind) - 1)
    # Randomizing the end of the section to scramble
    scrambled = random.sample(ind[i_start:i_end], k=i_end - i_start)
    # Randomly sampling the scrambled portion to shuffle the order
    return ind[:i_start] + scrambled + ind[i_end:]
    # Rebuilding the individual with the scrambled section
