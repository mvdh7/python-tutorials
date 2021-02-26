import pandas as pd
from matplotlib import pyplot as plt

# Import dataset
tm = pd.read_csv("data/TM_Med.csv")

# Rename depth column
tm = tm.rename(columns={"depth (m)": "depth", "sample": "sample_name"})
# tm.rename(columns={"depth (m)": "depth"}, inplace=True)  # equivalent

# # Pick out a row
# tm_row = tm.loc[43]

def get_station(tm_row):
    sname_split = tm_row.sample_name.split()
    station = int(sname_split[1])  # int converts string to integer
    return station


def get_bottle(tm_row):
    sname_split = tm_row.sample_name.split()
    bottle = int(sname_split[2])  # int converts string to integer
    return bottle

# Get station and bottle numbers
tm["station"] = tm.apply(get_station, axis=1)
tm["bottle"] = tm.apply(get_bottle, axis=1)



fvar = "Y89(LR)"
fstation = 1

# Get list of variables we want to plot
fvars = tm.columns
L = fvars.str.endswith("(LR)") | fvars.str.endswith("(MR)")
fvars = fvars[L]

#%% Loop through variables
for fvar in fvars:

    # Loop through stations
    for fstation in tm.station.unique():
    
        # Make a plot for one station, one variable
        fig, ax = plt.subplots(dpi=300, figsize=(4, 6))
        
        # tm.plot.scatter(fvar, "depth", ax=ax, c="Zr90(LR)", cmap="viridis")
        tm[tm.station == fstation].plot.scatter(fvar, "depth", ax=ax)
        ax.invert_yaxis()
        ax.set_ylabel("Depth / m")
        ax.grid(alpha=0.3)
        ax.set_title("Station " + str(fstation))
        
        plt.tight_layout()
        plt.savefig("figures/tut4/depth_" + fvar + "_" + str(fstation) + ".png")
        plt.show()

#%%
for i in [1, 3, 5, 7, 9]:
    print(i)
    print("ok")
print("done!")
