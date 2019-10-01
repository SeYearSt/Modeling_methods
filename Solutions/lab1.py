import numpy as np
from scipy.stats import t as t_student
from scipy.stats import chi2
import matplotlib.pyplot as plt

def calc_stat(distr):
  mean = np.mean(distr)
  var = np.var(distr, ddof=1)
  std = np.sqrt(var)
  return mean, var, std


def print_stat(*info: tuple) -> None:
  template = '{}\n Mean: {} \n Deviation: {} \n Std: {}'
  print(template.format(*info))


def calc_intervals(distr):
  r = 1+int(3.322*np.log10(distr.shape[0]))
  distr_min = distr.min()
  distr_max = distr.max()
  h = (distr_max - distr_min)/(r-1)
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

  return intervals, freq, freq_rel, freq_cum, h, r, distr_min, distr_max


def print_intervals_info(intervals, freq, freq_rel, freq_cum, h, r, distr_min, distr_max):
  print("Intervals")
  print(intervals)
  print()
  print("Frequency")	
  print(freq)
  print()
  print("Frequency related")
  print(freq_rel)
  print()
  print("Frequency cumulative")
  print(freq_cum)
  print()
  print('h=', h)
  print('r=', r)
  print('min=', distr_min)
  print('max=', distr_max) 


def print_line(width=80):
	print("*"*width)

if __name__ == '__main__':
  n = 21387
  gamma = 0.95
  alpha = 1 - gamma
  std_norm_teor = 0.5
  mean_norm_teor = 10.0
  exp_mean_teor = 0.01
  std_exp_teor = exp_mean_teor

  distr_norm = np.random.normal(mean_norm_teor, std_norm_teor, n)
  print('Normal distribution')
  print(distr_norm)
  print('Size:', distr_norm.shape)
  print()

  distr_exp = np.random.exponential(exp_mean_teor, n)
  print('Exponential distribution')
  print(distr_exp)
  print('Size:', distr_exp.shape)
  print()

  mean_norm, dev_norm, std_norm = calc_stat(distr_norm)
  print_stat('Normal distribution stats', mean_norm, dev_norm, std_norm)
  print()

  mean_exp, dev_exp, std_exp = calc_stat(distr_exp)
  print_stat('Exponentional distribution stats', mean_exp, dev_exp,std_exp)
  print()

  t_gamma = t_student.ppf(1-alpha/2, n - 1)
  print('t_gamma', t_gamma)
  mean_norm_interv = mean_norm - t_gamma*std_norm/np.sqrt(n), mean_norm + t_gamma*std_norm/np.sqrt(n)
  print('Confidence Interval for mean: ({}, {})'.format(*mean_norm_interv))
  print()

  chi2_1 = chi2.isf(q=alpha/2, df=n-1)
  chi2_2 = chi2.isf(q=1-alpha/2, df=n-1)
  print("Chi1={}, Chi2={}".format(chi2_1, chi2_2))
  std_norm_interv = np.sqrt((n-1)*dev_norm/chi2_1), np.sqrt((n-1)*dev_norm/chi2_2)
  print('Confident interval for std: ({}, {})'.format(*std_norm_interv))
  print()


  interval_info_norm = calc_intervals(distr_norm)
  print("Normal distribution")
  print_intervals_info(*interval_info_norm)
  print()

  interval_info_exp = calc_intervals(distr_exp)
  print("Exponential distribution")
  print_intervals_info(*interval_info_exp)
  print()

  # plt.hist(distr_norm, bins=interval_info_norm[5])
  # plt.show()
  # plt.hist(distr_exp, bins=interval_info_exp[5])
  # plt.show()

  print("mean norm theoretical: {}, mean norm sample: {}".format(mean_norm_teor, mean_norm))
  print("std norm theoretical: {},std norm sample: {}".format(std_norm_teor, std_norm))
  print()


  print("mean exp theoretical: {}, mean exp sample: {}".format(exp_mean_teor, mean_exp))
  print("std exp theoretical: {},std exp sample: {}".format(std_exp_teor, std_exp))
  print()
