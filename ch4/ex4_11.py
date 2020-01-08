import matplotlib.pyplot as plt

from .ex4_7 import BernoulliBandit
from .ex4_8 import follow_the_leader

if __name__ == '__main__':
    results = []
    for i in range(1000):
        bandit = BernoulliBandit([.5, .6])
        follow_the_leader(bandit, 100)
        results.append(bandit.regret())
    plt.hist(results, bins=20)
    plt.show()
