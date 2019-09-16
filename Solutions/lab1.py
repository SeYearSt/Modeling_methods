import numpy as np


def calc_stat(distr):
  mean = np.mean(distr)
  var = np.var(distr)
  std = np.sqrt(var)
  return mean, var, std


def print_stat(*info: tuple) -> None:
  template = '\t{}\n Mean: {} \t Deviation: {} \t Std: {}'
  print(template.format(*info))


def calc_intervals(distr):
  r = 1+int(3.322*np.log10(distr.shape[0]))
  distr_min = distr.min()
  h = (distr_min - distr.min())/r
  count = []
  beg = distr
  for 
  print('h', h, 'r', r)


if __name__ == '__main__':
  n = 21387
  std_norm_teor = 0.5

  distr_exp = np.random.exponential(0.01, n)
  distr_norm = np.random.normal(10.0, std_norm_teor, n)
  print('Exponential distribution:', distr_exp)
  print('Size:', distr_exp.shape)
  print('Normal distribution:', distr_norm)
  print('Size:', distr_norm.shape)

  mean_exp, dev_exp, std_exp = calc_stat(distr_exp)
  mean_norm, dev_norm, std_norm = calc_stat(distr_norm)
  print_stat('Exponentional distribution', mean_exp, dev_exp,std_exp)
  print_stat('Normal distribution', mean_norm, dev_norm, std_norm)

  gamma = 0.95
  t = 1.95
  mean_norm_interv = mean_norm - t*std_norm_teor/np.sqrt(n), mean_norm + t*std_norm_teor/np.sqrt(n)
  print('Interal: ({}, {})'.format(*mean_norm_interv))

  calc_intervals(distr_norm)
