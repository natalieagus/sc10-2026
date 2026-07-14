import numpy as np
import pandas as pd


df = pd.read_csv("./housing_processed.csv")
columns: list[str] = ["RM", "DIS", "INDUS"]
# extract the respective columns from the data frame
# replace the None
df_features: pd.DataFrame = df[columns] # all rows, but just these 3 cols
df_target = df[["MEDV"]] # all rows, and this 1 col as DataFrame

# CONVERT pandas to numpy
features_np = df_features.to_numpy()
target_np = df_target.to_numpy()

# Get dimension
rows, cols = features_np.shape

# random seed
random_state = 0 # put any int
np.random.seed(random_state)

# np random choice
# generate random test indexes
test_index = np.random.choice(
    list(range(100)), # indexes contain e.g: [0, ... 99]
    20, # e.g: 20
    replace = True) # with replacement
# test_index will be a list of int: 20 of them and randomly selected from 0...99 with replacement, --> [3, 5, 9, 10, 23, 59, 78, 8, ..]

# getting subarray
array_feature_test = features_np[test_index, :] # select these rows matching train_index from the original array_features array, and then select all rows

# getting mean and std
# features_np is a numpy array, we can get the mean of each column in the array by specifying the axis
# axis 0 means across the columns (over all rows)
# .reshape means to get all elements in the array, and then create a new array with the same of (row, col)
# so if we have [[1,2],[3,4]] (2x2 matrix), and we want to reshape that into (1,-1)--> reshape this matrix, into a new array with 1 row and AUTO column (-1 means auto) --> [1,2,3,4]
columns_means = features_np.mean(axis=0).reshape(1, -1)
columns_std = features_np.std(axis=0).reshape(1, -1)
