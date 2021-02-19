import pandas as pd


#%% Import data as a DataFrame
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Make a plot
L = glodap.depth < 20
glodap[L].plot.scatter("longitude", "latitude", c="temperature",
                    cmap='viridis')

# HOMEWORK
# with some spreadsheet file
# - import with pandas (read_csv, read_excel)
# - make a scatter plot of SOMETHING interesting
# - using a logical to subset part of the df
# extension:
# - use interpolation to join scattered points
