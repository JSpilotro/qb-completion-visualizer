import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/ArrowheadAnalytics/next-gen-scrapy-2.0/master/pass_and_game_data.csv', index_col=0)
df.head()

df_2019 = df.loc[df['season'] == 2019]

# Grabbing Patrick Mahomes 2019 data

mahomes = df_2019.loc[df_2019['name'] == 'Patrick Mahomes']

mahomes.head()

# filter out only complete passes
complete = mahomes.loc[mahomes['pass_type'] == 'COMPLETE']

# use the ggplot base styling for our visualization
plt.style.use('ggplot');

# set the fig size to look like a football field
fig, ax = plt.subplots(figsize=(6, 10))

# scatter plot the x_coord and y_coord
ax.scatter(x=complete['x_coord'], y=complete['y_coord'], color='green', alpha=0.4, edgecolors='white');

# a football field is roughly 53.3 yards wide.
ax.set_yticks(np.arange(-20, 60, 10));
ax.set_xticks(np.linspace(-53.3/2, 53.3/2, 10))

# the line of scrimmage is a line going across the field where x = 0
ax.hlines(0, -53.3/2, 53.3/2, color='grey', linestyles='dashed');
