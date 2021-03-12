import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
from sklearn.cluster import MeanShift

# Import GLODAP dataset
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv", na_values=-9999)

#%% Select station to use for testing
fvar = "tco2"  # dissolved inorganic carbon
L = (glodap.cruise == 387) & (glodap.station == 13) & ~np.isnan(glodap[fvar])

# Extract x and y variables
x_values = glodap[fvar][L].to_numpy()
depth_values = glodap.depth[L].to_numpy()


def cluster_profile(depth_values, x_values, bandwidth=10):
    """Cluster depth profile data with MeanShift and interpolate.
    
    Awesome.
    """
    # Clustering
    depth_values_v = np.vstack(depth_values)
    clustering = MeanShift(bandwidth=bandwidth).fit(depth_values_v)
    cluster_labels = clustering.labels_
    
    # Average by cluster
    depth_clusters = clustering.cluster_centers_.ravel()
    x_clusters = np.full_like(depth_clusters, np.nan)
    for i in range(len(depth_clusters)):
        x_clusters[i] = np.mean(x_values[cluster_labels == i])
    
    # Sort arrays by depth
    depth_index = np.argsort(depth_clusters)
    x_clusters = x_clusters[depth_index]
    depth_clusters = depth_clusters[depth_index]
    
    # # Average duplicate values
    # depth_unique = np.unique(depth_values)
    # x_unique = np.full_like(depth_unique, np.nan)
    # for i in range(len(depth_unique)):
    #     x_unique[i] = np.mean(x_values[depth_values == depth_unique[i]])
    
    # Do a PCHIP interpolation
    interpolator = interpolate.pchip(depth_clusters, x_clusters)
    depth_plotting = np.linspace(np.min(depth_values), np.max(depth_values),
                                 num=1000)
    x_plotting = interpolator(depth_plotting)
    
    return depth_clusters, x_clusters, depth_plotting, x_plotting

# Don't forget to run the function!
depth_clusters, x_clusters, depth_plotting, x_plotting = cluster_profile(
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
