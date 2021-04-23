import xarray as xr, numpy as np
from matplotlib import pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
import cmocean

gebco = xr.open_dataset("data/gebco_2020_noordzee.nc")

#%% Visualise the dataset
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson())

vmin = -300
vmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, vmin, vmax, 0)

# Draw bathymetry data
bathymetry = (
    gebco.elevation
    # .coarsen(lat=10, lon=10, boundary="trim").mean()
    .plot(
        add_colorbar=False,
        ax=ax,
        # cmap="Blues_r",
        cmap=cmap,
        transform=ccrs.PlateCarree(),
        vmin=vmin,
        vmax=vmax,
    )
)
cbar = plt.colorbar(bathymetry)
cbar.set_label("Depth / m")
ticks = np.array(list(range(vmin, vmax + 1, 50)))
cbar.set_ticks(ticks)
cbar.set_ticklabels(-ticks)

# Add land areas
ax.add_feature(
    cfeature.NaturalEarthFeature(
        "physical", "land", "10m"
    ),
    facecolor="xkcd:dark grey",
    edgecolor="none",
)
ax.add_feature(
    cfeature.NaturalEarthFeature(
        "physical", "lakes", "10m"
    ),
    facecolor=cmap(1.0),
    edgecolor="none",
)

# Axis settings
ax.set_extent([0, 8, 50, 60])
plt.savefig("figures/maps-with-bathymetry.png")
