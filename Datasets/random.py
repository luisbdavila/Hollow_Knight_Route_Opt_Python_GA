import random
import pandas as pd

random.seed(23)

places = ['D', 'FC', 'G', 'QS', 'QG', 'CS', 'KS', 'RG', 'DV', 'SN']
random_dataset = [[random.randint(-10, 100) if _ != __ else 0
                   for _ in range(10)] for __ in range(10)]
# Creating the dataset randomly
min_positive_geo = min([random_dataset[i][j] for j in range(10)
                        for i in range(10)
                        if random_dataset[i][j] > 0 and i != 2 and j != 1])
print(min_positive_geo)
if random_dataset[2][1] > min_positive_geo * 0.968:
    random_dataset[2][1] = int(min_positive_geo * 0.968)
# Calculating the minimum positive geo gain and evaluating
# whether the transition from  Greenpath (G) to Forgotten Crossroads (FC)
# is at least 3.2% lower than that minimum and if it isn't
# replacing it by the minimum - 3.2%
random_dataset_DF = pd.DataFrame(random_dataset, index=places, columns=places)
print(random_dataset_DF)
