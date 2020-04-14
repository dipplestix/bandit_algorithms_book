from numpy.random import normal
from math import log
from random import choice


class GaussianBandit:
    # Accepts a list of k >= 2 floats, each lying in [0, 1]
    def __init__(self, means):
        assert len(means) >= 2, 'Requires at least 2 arms'
        self.means = means
        self.k = len(means)
        self.actions = []
        self.rewards = []

    # Accepts a paramater 0 <= a <= K-1 and returns the
    # realization of random variable X with P(X=1) being
    # the mean of the (a+1)th arm
    def pull(self, a):
        assert 0 <= a <= self.k - 1, "0 <= a <= K-1"
        self.actions.append(a)
        result = normal(loc=self.means[a])
        self.rewards.append(result)
        return result

    def random_regret(self):
        opt = len(self.actions)*max(self.means)
        random_regret = opt - sum(self.rewards)
        return random_regret

    def regret(self):
        opt = len(self.actions)*max(self.means)
        regret = opt - sum([self.means[a] for a in self.actions])
        return regret


def opt_m(n, delta):
    m = int(4/(delta**2) * log(n*(delta**2)/4))
    return max(1, m)


def max_regret(delta, n):
    max1 = n*delta
    term = log(n*(delta**2)/4)
    term = max([0, term])
    max2 = delta + 4/delta * (1+term)
    return min(max1, max2)


def etc(bandit, n, m):
    k = bandit.k
    results = [0]*k
    for i in range(k):
        for j in range(m):
            results[i] += bandit.pull(i)
    options = [i for i, x in enumerate(results) if x == max(results)]
    opt = choice(options)
    for i in range(m*k, n):
        bandit.pull(opt)
