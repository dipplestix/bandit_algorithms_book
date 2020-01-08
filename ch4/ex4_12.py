import matplotlib.pyplot as plt
import statistics

from .ex4_7 import BernoulliBandit
from .ex4_8 import follow_the_leader

if __name__ == '__main__':
    trials = [i*100 for i in range(1, 11)]
    averaged_results = []
    error = []
    for k in trials:
        results = []
        for i in range(1000):
            bandit = BernoulliBandit([.5, .6])
            follow_the_leader(bandit, k)
            results.append(bandit.regret())
        averaged_results.append(statistics.mean(results))
        error.append(statistics.stdev(results)/len(results)**.5)

    plt.errorbar(x=trials, y=averaged_results, yerr=error, capsize=3)
    plt.show()
