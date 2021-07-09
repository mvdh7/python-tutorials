import numpy as np
from matplotlib import pyplot as plt

# Scoring
# 3, 4 letter word = 1 point
# 5 letter word = 2 points
# 6             = 3
# 7             = 5
# 8+            = 11

# Define what appears on the dice
dice = [
    "AAEEGN",
    "ELRTTY",
    "AOOTTW",
    "ABBJOO",
    "EHRTVW",
    "CIMOTU",
    "DISTTY",
    "EIOSST",
    "DELRVY",
    "ACHOPS",
    "HIMNQU",
    "EEINSU",
    "EEGHNW",
    "AFFKPS",
    "HLNNRZ",
    "DEILRX",
]

# Initialise the random number generator (rng)
rng = np.random.default_rng()
# ^ can set seed for reproducibility

# Determine order of dice in the grid
rng.shuffle(dice)

# Initialise figure
fig, ax = plt.subplots(dpi=300)

# Loop through the dice
for i, die in enumerate(dice):
    
    # Determine which face is showing on each die
    face_index = rng.choice(range(6))
    face = die[face_index]
    
    # Turn Q into Qu
    if face == 'Q':
        face = 'Qu'
        
    # Unravel 0-15 index into a 4x4 grid
    x, y = np.unravel_index(i, (4, 4))
    
    # Draw the die
    ax.text(x, y, face, fontsize=45, ha='center', va='center')
    
# Tidy up figure appearance
ax.set_xlim([-0.5, 3.5])
ax.set_ylim([-0.5, 3.5])
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect(1)
