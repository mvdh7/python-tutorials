import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from cartopy import crs as ccrs, feature as cfeature

#%% Import data to plot
glodap = pd.read_csv("data/GLODAPv2.2020_Indian_Ocean.csv",
                     na_values=-9999)
stations = glodap.groupby(by=["cruise", "station"]).mean()
stations["longitude_radians"] = np.deg2rad(stations.longitude)

#%% Draw a map

# Set up figure
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(
    central_longitude=90))
# fig, ax = plt.subplots(dpi=300)  # alternative

ax.scatter("longitude", "latitude", data=stations,
           s=15, alpha=0.7, c="xkcd:strawberry",
           edgecolor="none",
           transform=ccrs.PlateCarree())

ax.plot([10, 150], [-20, -30], transform=ccrs.Geodetic(),
        c="xkcd:bright blue")

ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# ax.coastlines()

ax.gridlines(alpha=0.3, draw_labels=True)

extents = lon_min, lon_max, lat_min, lat_max = 100, 108, -8, -2
ax.set_extent(extents, crs=ccrs.PlateCarree())
# ax.set_global()

land = cfeature.LAND
land = cfeature.NaturalEarthFeature("physical", "land", "10m")
ax.add_feature(land, facecolor="xkcd:dark grey",
               edgecolor="none")

islands = cfeature.NaturalEarthFeature("physical",
                                       "minor_islands",
                                       "10m")
ax.add_feature(islands, facecolor="xkcd:dark grey",
               edgecolor="none")


# physical/ne_10m_rivers_lake_centerlines.zip
rivers = cfeature.NaturalEarthFeature("physical",
                                      "rivers_lake_centerlines",
                                      "10m")
ax.add_feature(rivers, facecolor="none", edgecolor="b")

plt.savefig("figures/t6-cartopy.png")

# ax.stock_img()

# ax.set_ylim([-90, 90])

# # Identical alternatives:
# stations.plot.scatter("longitude", "latitude", ax=ax)
# ax.scatter(data.longitude, data.latitude)
