x = 'Abcdefg'
y = "12345"

# \ as escape character
quote = 'The man said \'hello\''
quote = "The man said 'hello'"

# multi-line string
z = 'one\ntwo'
z2 = '''one
two'''

# look if one string appears in another
x_has_abc = 'abc' in x
y_has_abc = 'abc' in y
x_abc_at_start = x.startswith('abc')
x_abc_at_end = x.endswith('abc')
x_find_de = x.find('de')
y_find_de = y.find('de')

# convert case
x_upper = x.upper()
x_lower = x.lower()
x_abc_at_start_case = x.lower().startswith('abc')

# splitting
sample = 'DY33 3 11'
sample_split = sample.split()

sample2 = 'DY33-3-11'
sample2_split = sample2.split('-')
station, cruise, niskin = sample2_split

# splitting lines
z_lines = z.split('\n')
z_lines_auto = z.splitlines()

# joining
xy = x + y
xy_joined = '-'.join((x, y, 'penguin',
                            'rockhopper'))

# format
phrase = 'My name is {}.  {} {}.'.format(
    'Bond', 'James', 'Bond'
)
phrase = 'My name is {0}.  {1} {0}.'.format(
    'Bond', 'James'
)
phrase = 'My name is {surname}.  {firstname} {surname}.'.format(
    surname='Bond', firstname='James'
)
# print(phrase)

# format with numbers
import numpy as np

print('The value of pi is ' + str(np.pi))
print('The value of pi is {:10.3f}'.format(np.pi))
# Alignment
print('The value of pi is {:<10.3f}'.format(np.pi))
print('The value of pi is {:^10.3f}'.format(np.pi))
# Pad with zeros
print('The value of pi is {:^010.1f}'.format(np.pi))
print('The value of π is {:+.3f}'.format(np.pi))

# add strings to figures
from matplotlib import pyplot as plt

fig, ax = plt.subplots(dpi=300)

ax.set_title('$R^2$ = {r2:.3f}, $n$ = {n}'.format(r2=0.85215464575,
                                             n=50))

ax.set_xlabel("Molality of CO$_2$ / μmol kg$^{-1}$")

#%% string methods and pandas arrays
import pandas as pd

coccos = pd.read_csv('data/Poulton_v2.csv')

# find refs ending 2011
coccos['published_2011'] = coccos.Reference.str.endswith('2011')



















