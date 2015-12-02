__author__ = 'bardia'

import matplotlib.pyplot as plt


class Drawer(object):
    def __init__(self, runs):
        self.runs = runs

    def draw(self):
        plt.hlines([e[0].index if e[0] is not None else 0 for e in self.runs],
                   [e[1] for e in self.runs],
                   [e[1] + 1 for e in self.runs]
                   , colors='k', linestyles='solid')
        plt.show()
