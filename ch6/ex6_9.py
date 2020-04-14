from etc import *
import matplotlib.pyplot as plt
import statistics

if __name__ == '__main__':
    trials = 10**1

    # Recreate figure 6.1
    # n = 1000
    # delta = [(i+1)/100 for i in range(100)]
    # regret = []
    # bounded_regret = []
    # for d in delta:
    #     if d % .1 == 0:
    #         print(d)
    #     res = []
    #     m = opt_m(n, d)
    #     bounded_regret.append(max_regret(d, n))
    #     for t in range(trials):
    #         bandit = GaussianBandit([0, -d])
    #         etc(bandit, n, m)
    #         res.append(bandit.regret())
    #     regret.append(sum(res)/len(res))
    # fig, ax = plt.subplots()
    # plt.plot(regret, label='ETC')
    # plt.plot(bounded_regret, label='Upper bound')
    # legend = ax.legend()
    # plt.show()

    # Part c
    d = 1/10
    n = 20000
    regretc = []
    error = []
    for m_base in range(1, 101):
        m = m_base*5
        print(m)
        res = []
        for t in range(trials):
            bandit = GaussianBandit([0, -d])
            etc(bandit, n, m)
            res.append(bandit.regret())
        regretc.append(sum(res)/len(res))
        error.append(statistics.variance(res)**.5)

    plt.plot(regretc, label='ETC regret')

    # Part d
    plt.plot(error, label='ETC regret standard deviation')
    plt.legend()
    plt.show()

    # Part e

    # All plots make sense.
    # We should see the regret find a minimum at m =
    # The standard deviation of the results should also decrease since as m increases, the chance of committing to the
    # wrong option goes towards 0, making our results the same.

    # Part f

    # I think it's better to find V[R_n] for each option and then compare that.
