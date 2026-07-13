import pandas as pd

filename= "./housing_processed.csv"
df = pd.read_csv(filename) # read csv
df.shape # gives tuple of (row, col)

df.columns # gives pd.Index data type that contains the list of all the columns names

# we can create a subset of pandas dataframe by using the [] and giving the coln names: list of string
columns: list[str] = ["RM", "DIS", "INDUS"]
df_copy = df[columns]

# if we use string as the value, we get series
df_copy_series = df["MEDV"]

# indexing and selecting data using loc
columns: list[str] = ["RM", "DIS", "INDUS", "MEDV"]
df_1: pd.DataFrame = df.loc[df["DIS"] <= 3, columns] # df.loc[row condition, col condition]
# we select rows, that fullfil the cond of df["DIS"] <= 3 and columns that name matches columns

df_2: pd.DataFrame = df.loc[(5 <= df["RM"]) & (df["RM"] <= 8)] # we can use multiple conditions as row selector this way. remember that df["RM"] gives a series, and df["RM"] <= 8 gives a list of True/False per row indicating whether each row is <= 8 or not

df_3: pd.DataFrame = df.loc[0:14, columns] # row selector is just now the first 15 records

df_4 = df.loc[df.shape[0]-15:df.shape[0]-1, columns] # row selector is now the last 15 records, we use df.shape[0] to get the length of records (#rows)

df_5: pd.DataFrame = df.loc[0:df.shape[0]-1:2, columns] # can also use regular list indexer like start:end:step to filter the rows
