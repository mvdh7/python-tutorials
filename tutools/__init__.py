import numpy as np, pandas as pd
from scipy import interpolate
from sklearn.cluster import MeanShift


def get_cluster_interp(depth_values, x_values, bandwidth=10):
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

    # Do a PCHIP interpolation
    interpolator = interpolate.pchip(depth_clusters, x_clusters)
    
    return depth_clusters, x_clusters, interpolator


def cluster_profile(depth_values, x_values, bandwidth=10):
    """Cluster depth profile data with MeanShift and interpolate.
    
    Awesome.
    """
    depth_clusters, x_clusters, interpolator = get_cluster_interp(
        depth_values, x_values, bandwidth=bandwidth
    )
    depth_plotting = np.linspace(np.min(depth_values), np.max(depth_values), num=1000)
    x_plotting = interpolator(depth_plotting)
    return depth_clusters, x_clusters, depth_plotting, x_plotting


def get_depth_interpolation(glodap_station):
    
    fvar = "tco2"
    depth = 500.0
    
    # Extract x and y variables
    x_values = glodap_station[fvar].to_numpy()
    depth_values = glodap_station.depth.to_numpy()
    
    # Don't use NaNs
    nans = np.isnan(x_values) | np.isnan(depth_values)
    x_values = x_values[~nans]
    depth_values = depth_values[~nans]
    
    if np.sum(~nans) > 2:
        # Get the interpolating function
        interpolator = get_cluster_interp(depth_values, x_values)[2]
        # Interpolate to the depth of interest
        x_interp = interpolator(depth)
    else:
        x_interp = np.nan
        
    print(x_interp)
        
    return pd.Series({"fvar_interpolated": x_interp})
