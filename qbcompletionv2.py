import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/ArrowheadAnalytics/next-gen-scrapy-2.0/master/pass_and_game_data.csv', index_col=0)
df.head()

def plot_passes(player_name='Patrick Mahomes', year=2019):

  plt.style.use('fivethirtyeight')

  player = df.loc[(df['season'] == year) & (df['name'] == player_name)]

  #grab completions, incompletions, interceptions, and tds separately
  complete = player.loc[player['pass_type'] == 'COMPLETE']
  incomplete = player.loc[player['pass_type'] == 'INCOMPLETE']
  interception = player.loc[player['pass_type'] == 'INTERCEPTION']
  touchdown = player.loc[player['pass_type'] == 'TOUCHDOWN']

  fig, ax = plt.subplots(figsize=(6, 10))

  # scatter plot completions as small green dots with some transparency
  ax.scatter(complete['x_coord'], complete['y_coord'], color='green', alpha=0.6, edgecolors='white')
  # scatter plot incompletions as small red dots with some transparency
  ax.scatter(incomplete['x_coord'], incomplete['y_coord'], color='red', alpha=0.6, edgecolors='white')
  # scatter plot touchdowns as big green dots with less transparency and larger white outline
  ax.scatter(touchdown['x_coord'], touchdown['y_coord'], color='green', alpha=0.8, edgecolors='white', linewidth=2, s=125)
  # scatter plot touchdowns as big red dots with less transparency and larger white outline
  ax.scatter(interception['x_coord'], interception['y_coord'], color='red', alpha=0.8, edgecolors='white', linewidth=2, s=125)


  ax.set_yticks(np.arange(-20, 60, 10));
  ax.set_xticks(np.linspace(-53.3/2, 53.3/2, 4))

  # style the ticks and the visualization border
  ax.tick_params(axis='x', colors="white", grid_alpha=0.4)
  ax.tick_params(axis='y', colors="white", grid_alpha=0.4)
  plt.setp(ax.spines.values(), color='white', alpha=0.2, linewidth=1)

  #line of scrimmage
  ax.hlines(0, -53.3/2, 53.3/2, color='white', linewidth=3, linestyles='dashed', alpha=0.4);

  # set the title of our plot (all caps)
  ax.set_title('\n'+ player_name.upper() + ' pass locations, '.upper() + str(year) + '\n', color='white', alpha=0.6, fontsize=18)

  # set the background color of our plot to a dark blue
  ax.set_facecolor('#233746')
  fig.set_facecolor('#233747')

  # set the legend off to the side
  ax.legend(['Complete Pass', 'Incomplete Pass', 'Touchdown', 'Interception', 'Line of Scrimmage'],
            ncol=1, loc='upper left', bbox_to_anchor=(1.05, 1), facecolor='#233746', prop={'size': 16})

plot_passes()
