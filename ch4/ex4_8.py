import random


def follow_the_leader(bandit, n):
	# Choose each action once and then choose the action with the highest reward
	arms = bandit.k
	results = [0]*arms
	pulls = [0]*arms
	for a in range(arms):
		results[a] += bandit.pull(a)
		pulls[a] += 1
	for i in range(n - arms):
		averages = [results[i] / pulls[i] for i in range(arms)]
		options = [i for i, x in enumerate(averages) if x == max(averages)]
		action = random.choice(options)
		results[action] += bandit.pull(action)
		pulls[action] += 1
