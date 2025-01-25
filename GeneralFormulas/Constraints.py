def Check_QS_DV_Not_KS(indv):
    # If QS is followed by DV then the upper case 'KS'
    # is replaced by a lower case 'ks' which indicates
    # the possibility of skipping KS
    if indv[indv.index('QS') + 1] == 'DV':
        indv[indv.index('KS')] = "ks"


def Check_QG_CS(indv):
    # True if QG is right before CS
    # True if we have an unfeasible solution
    return indv[indv.index('QG') + 1] == 'CS'


def Check_RG_First_Part(indv):
    # True if RG is at the first part of the path
    # True if we have unfeasible solution
    return "RG" in indv[:len(indv)//2]
