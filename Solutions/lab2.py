import numpy as np


if __name__ == '__main__':
	n = 1000
	el_count = 7
	total_time = 0

	for i in range(n):
		tafs = [np.random.poisson() for k in range(el_count)]
		gamma = min(tafs[0], max(min(max(tafs[2], tafs[3]), tafs[5]), min(tafs[1], tafs[4])), tafs[6])
		total_time += gamma

	print("Estiamted time:", total_time/n)
