import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from scipy import interpolate, stats

# Import titration file
file_to_use = "titration2"
data = np.genfromtxt('data/' + file_to_use + '.txt',
                     skip_header=2)
volume = data[::3, 0]
emf = data[::3, 1]
temperature = data[::3, 2]

# Interpolate the data - this function makes another function
interp_linear = interpolate.interp1d(volume, emf, kind='linear')
interp_nearest = interpolate.interp1d(volume, emf, kind='nearest')
interp_cubic = interpolate.interp1d(volume, emf, kind='cubic')
interp_pchip = interpolate.PchipInterpolator(volume, emf)
interp_spline = interpolate.UnivariateSpline(volume, emf,
                                             s=1000)
# ^ spline with smoothing

# Linear regression
slope, intercept, rv, pv, se = stats.linregress(volume, emf)

# Array to interpolate on to
volume_interp = np.linspace(np.min(volume), np.max(volume), num=500)

# Apply the interpolation
emf_linear = interp_linear(volume_interp)
emf_nearest = interp_nearest(volume_interp)
emf_cubic = interp_cubic(volume_interp)
emf_pchip = interp_pchip(volume_interp)
emf_spline = interp_spline(volume_interp)

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.scatter(volume, emf, s=35, c='xkcd:navy blue', zorder=10)
# ^ zorder controls which element appears on top
ax.plot(volume, emf, label="Direct plot")
ax.plot(volume_interp, emf_linear, label="interp1d linear",
        linestyle="--")
ax.plot(volume_interp, emf_nearest, label='interp1d nearest')
ax.plot(volume_interp, emf_cubic, label='interp1d cubic')
ax.plot(volume_interp, emf_pchip, label='PCHIP')
ax.plot(volume_interp, intercept + slope * volume_interp,
        label='Linear regression')
ax.plot(volume_interp, emf_spline, label='spline', zorder=11)
ax.set_xlabel('Volume / ml')
ax.set_ylabel('EMF / mV')
ax.grid(alpha=0.3)
ax.legend()

# Save to file
plt.savefig("figures/t2_" + file_to_use + ".png")
