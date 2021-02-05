import numpy as np
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# Create some lists
x_list = [2, 3, 6, 2, 4, 7, 43, 21, 3, 5]
y_list = [1, 3, 6, 32, 6, 4, 2, 54, 2, 1]

# Try to add them together: z = x + y
z_list = x_list + y_list
# The pure Python solution is to use a comprehension
z_comp = [xi + yi for xi, yi in zip(x_list, y_list)]
# This is difficult to read and not intuitive
# And slower than numpy!  Use %timeit in the console

# Convert our lists into numpy arrays
x = np.array(x_list)
y = np.array(y_list)
z = x + y

# Other operators
a = x - y
b = x * y
c = x / y
d = x ** y  # to the power of

# Import titration file
file_to_use = "titration2"
data = np.genfromtxt('data/' + file_to_use + '.txt',
                     skip_header=2)
volume = data[:, 0]
emf = data[:, 1]
temperature = data[:, 2]

# Other calculations with numpy
emf_sqrt = np.sqrt(emf)
emf_log = np.log(emf)
emf_log10 = np.log10(emf)

# Summary statistics
emf_mean = np.mean(emf)
emf_median = np.median(emf)
emf_std = np.std(emf)

# Make a plot
fig, ax = plt.subplots(dpi=300)
ax.scatter(volume, emf, s=35, c='xkcd:dust')
ax.set_xlabel('Volume / ml')
ax.set_ylabel('EMF / mV')
ax.grid(alpha=0.3)

# Save to file
plt.savefig("figures/" + file_to_use + ".png")
plt.savefig("figures/" + file_to_use + ".pdf")
