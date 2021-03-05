import pandas as pd, numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate

# Import dataset
cal = pd.read_csv("cal.csv")


#%% Loop through variables
for element in cal.element.unique():
    L = cal.element == element
    
    # Interpolate the data
    interp_linear = interpolate.interp1d(cal[L].concentration, cal[L].counts)
    concentration_interp = np.linspace(np.min(cal[L].concentration), np.max(cal[L].concentration))
    counts_linear = interp_linear(concentration_interp)
    
    fig, axi = plt.subplots(dpi=300, figsize=(4, 6))

    cal[L].plot.scatter(
        "concentration",
        "counts",
        label=element,
        ax=axi,
    )
    
    # Draw interpolation line
    cal[L].plot(
        concentration_interp, counts_linear, label="Interpolation", ax=axi
    )
    
    axi.legend()

    # Settings and save
    axi.grid(alpha=0.3)
    axi.set_title(element)
    plt.tight_layout()
    plt.savefig("figures/homework/" + element + ".png")
    plt.show()
