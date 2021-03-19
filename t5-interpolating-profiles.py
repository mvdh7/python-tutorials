import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import tutools as tt

# Import GLODAP dataset
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Select station to use for testing
fvar = "tco2"  # dissolved inorganic carbon
L = (glodap.cruise == 387) & (glodap.station == 13) & ~np.isnan(glodap[fvar])

# Extract x and y variables
x_values = glodap[fvar][L].to_numpy()
depth_values = glodap.depth[L].to_numpy()

# Get the interpolating function
interpolator = tt.get_cluster_interp(depth_values, x_values)[2]

# glodap_station = glodap[L]
# test = get_depth_interpolation(glodap_station)

all_stations = glodap[:5000].groupby(by=["cruise", "station"]).apply(
    tt.get_depth_interpolation)


#%% Don't forget to run the function!
depth_clusters, x_clusters, depth_plotting, x_plotting = tt.cluster_profile(
    depth_values, x_values, bandwidth=8
)

# Basic plotting
fig, ax = plt.subplots(dpi=300)
glodap[L].plot.scatter(fvar, "depth", ax=ax, c="xkcd:blue", s=50)
# glodap[L].plot(fvar, "depth", ax=ax, legend=False)
ax.scatter(x_clusters, depth_clusters, c="xkcd:strawberry", s=10)
ax.plot(x_plotting, depth_plotting, c="xkcd:strawberry")
ax.set_ylim([1250, 0])
# ax.invert_yaxis()
