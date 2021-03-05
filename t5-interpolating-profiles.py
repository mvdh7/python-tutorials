import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

# Import GLODAP dataset
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Select station to use for testing
fvar = "tco2"
L = (glodap.cruise == 387) & (glodap.station == 11) & ~np.isnan(glodap[fvar])

# Extract x and y variables
x_values = glodap[fvar][L].to_numpy()
depth_values = glodap.depth[L].to_numpy()

# Sort arrays by depth
depth_index = np.argsort(x_values)
x_values = x_values[depth_index]
depth_values = depth_values[depth_index]

# Do a PCHIP interpolation
interpolator = interpolate.pchip(depth_values, x_values)


# Basic plotting
fig, ax = plt.subplots(dpi=300)
glodap[L].plot.scatter(fvar, "depth", ax=ax)
glodap[L].plot(fvar, "depth", ax=ax, legend=False)
ax.set_ylim([1200, 0])
# ax.invert_yaxis()
