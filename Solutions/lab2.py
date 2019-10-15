import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
  np.random.seed(0)
  
  step = 50000
  el_count = 7
  lambda_param = 1

  history_samples = []

  n_min = 1000
  n_max = 1200000

  for n in range(n_min, n_max, step):
  	  print(n)
  	  history_sample = []
  	  for j in range(n):
  	  	tafs = [np.random.poisson(lambda_param) for k in range(el_count)]
  	  	gamma = min(tafs[0], max(min(max(tafs[2], tafs[3]), tafs[5]), min(tafs[1], tafs[4])), tafs[6])
  	  	history_sample.append(gamma)
  	  history_samples.append(np.mean(history_sample))

  print(history_samples)
  plt.plot(range(len(history_samples)), history_samples)
  plt.show()