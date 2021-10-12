import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/ArrowheadAnalytics/next-gen-scrapy-2.0/master/pass_and_game_data.csv', index_col=0)
df.head()
