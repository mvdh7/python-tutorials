import numpy as np, pandas as pd
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# Import titration file
file_to_use = "titration1"
data = np.genfromtxt('data/' + file_to_use + '.txt',
                     skip_header=2)
volume = data[:, 0]
emf = data[:, 1]
temperature = data[:, 2]

# combine the arrays into a dict
titration = {
    "volume": volume,
    "emf": emf,
    "temperature": temperature,
    }
titration = pd.DataFrame(titration)

# make a logical array
L = ((volume >= 3) & (emf < 460)) | (volume < 1)

# titration_L = {k: v[L] for k, v in titration.items()}
titration_L = titration[L]

# working with dataframes
vol = titration['volume']  # just like in a dict
vol = titration.volume  # dot notation - doesn't work for everything
# ^ access columns
titration['whatever'] = 15
titration['volume_squared'] = titration.volume ** 2
# ^ assign new columns - can't use dot notation
vol_L = titration[L]['volume']
vol_L = titration['volume'][L]
vol_L = titration[L].volume
vol_L = titration.volume[L]
# ^ these are all the same thing: column and rows together

# Make a plot
fig, ax = plt.subplots(dpi=300)

# ax.scatter(volume, emf, s=35, c='xkcd:navy')
sc_full = ax.scatter('volume', 'emf', data=titration,
           s=25, c='emf', cmap='plasma')

# ax.scatter(volume[L], emf[L], s=35, c='xkcd:tangerine',
#            alpha=0.9)
sc = ax.scatter('volume', 'emf', data=titration[L],
           s=25, c='emf')
plt.colorbar(sc)
plt.colorbar(sc_full)

ax.set_xlabel('Volume / ml')
ax.set_ylabel('EMF / mV')
ax.grid(alpha=0.3)
