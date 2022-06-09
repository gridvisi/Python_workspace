import seaborn as sns
import scipy
import pandas as pd
import numpy as np
import matplotlib as plt
def get_p_win(elo_a, elo_b):
    diff = elo_a - elo_b
    return 1 / (10 ** (-diff / 400) + 1)

elo_brazil = 2155
elo_france = 2116
get_p_win(elo_brazil, elo_france)

#view rawprob_brazil_win.py hosted with ❤ by GitHub

b_sample = np.random.normal(elo_brazil, 20, 100_000)
f_sample = (scipy.stats.skewnorm.rvs(3, size=100_000) * 40) + elo_france

sns.kdeplot(b_sample, fill=True, label="Brazil", color="purple")
sns.kdeplot(f_sample, fill=True, label="France", color="darkgreen")
plt.legend()
plt.xlabel("Elo rating")
plt.show()