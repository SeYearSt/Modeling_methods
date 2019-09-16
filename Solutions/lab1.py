import numpy as np
from scipy.stats import t as t_student
import matplotlib.pyplot as plt

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
  distr_max = distr.max()
  print(r)
  print(distr_min, distr_max)
  h = (distr_max - distr_min)/r
  print(h)
  beg = distr_min - h/2
  intervals = []
  freq = []
  freq_rel = []
  freq_cum = []
  for i in range(r):
  	start = beg
  	end = beg+h
  	intervals.append((start, end))
  	freq.append(np.sum(np.logical_and(distr>start, distr<=end)))
  	freq_rel.append(freq[i]/distr.shape[0])
  	freq_cum.append(sum(freq))
  	beg += h

  return intervals, freq, freq_rel, freq_cum, h

if __name__ == '__main__':
  n = 21387
  gamma = 0.95
  std_norm_teor = 0.5
  mean_norm_teor = 10.0
  exp_norm_teor = 0.01

  distr_exp = np.random.exponential(exp_norm_teor, n)
  distr_norm = np.random.normal(mean_norm_teor, std_norm_teor, n)
  print('Exponential distribution:', distr_exp)
  print('Size:', distr_exp.shape)
  print('Normal distribution:', distr_norm)
  print('Size:', distr_norm.shape)

  mean_exp, dev_exp, std_exp = calc_stat(distr_exp)
  mean_norm, dev_norm, std_norm = calc_stat(distr_norm)
  print_stat('Exponentional distribution', mean_exp, dev_exp,std_exp)
  print_stat('Normal distribution', mean_norm, dev_norm, std_norm)

  t_gamma = t_student.ppf((1 + gamma) / 2, n - 1)
  mean_norm_interv = mean_norm - t_gamma*std_norm/np.sqrt(n), mean_norm + t_gamma*std_norm/np.sqrt(n)
  print('Interal: ({}, {})'.format(*mean_norm_interv))

  intervals_norm, freq_norm, freq_rel_norm, freq_cum_norm, h_norm = calc_intervals(distr_norm)
  intervals_exp, freq_exp, freq_rel_exp, freq_cum_exp, h_exp = calc_intervals(distr_exp)
  print('\tNormal distribution:\nFreq={}\nfreq_rel={}\npfreq_cum={}'.format(freq_norm, freq_rel_norm, freq_cum_norm))
  print('\tExponential distribution:\nFreq={}\nfreq_rel={}\npfreq_cum={}'.format(freq_exp, freq_rel_exp, freq_cum_exp))

  bins = 35
  plt.hist(distr_norm, bins)
  plt.show()
  plt.hist(distr_exp, bins)
  plt.show()

  print('mean norm theoretical: {}, mean norm sample: {}\n'+
  	'std norm theoretical: {} std norm sample: {}\n'.format(mean_norm_teor, mean_norm, std_norm_teor, std_norm))
# print('mean exp theoretical: {}, mean exp sample: {}\n'+
#   	'std exp theoretical: {} std exp sample: {}\n'.format(mean_exp_teor, mean_exp, std_exp_teor, std_exp))