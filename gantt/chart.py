__author__ = 'bardia'

import matplotlib.pyplot as plt


def draw(runs):
    plt.hlines([e[0].index if e[0] is not None else 0 for e in runs],
               [e[1] for e in runs],
               [e[1] + 1 for e in runs]
               , colors='k', linestyles='solid')
    plt.show()
