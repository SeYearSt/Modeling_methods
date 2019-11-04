if __name__ == '__main__':
  eps = 0.00001
  n = n_start = 10000
  step = 10000
  el_count = 7
  lambda_param = 1

  x = PrettyTable()
  x.field_names = ["Number of generations", "Mean Time"]

  history = []
  num_gen = []
  final_time = []

  i = 0
  while True:
    total_time = []
    for _ in range(n):
      tafs = [np.random.poisson(lambda_param) for k in range(el_count)]
      gamma = min(tafs[0], max(min(max(tafs[2], tafs[3]), tafs[5]), min(tafs[1], tafs[4])), tafs[6])
      total_time.append(gamma)

    mean_time = np.mean(total_time)
    history.append(mean_time)
    num_gen.append(n)

    if i > 1:
      if np.abs(history[-2] - history[-1])<=eps:
        break

    if i==10:
      step = 50000

    if i==15:
      step = 100000

    if n >= 400000:
      final_time.append(history[-1])

    if i >= 20:
      break

    n+=step
    i+=1

    print('num gen', num_gen[-1])
    print("Estimated time:", history[-1])

    
    x.add_row([num_gen[-1], history[-1]]) 

  print(x)
  print('Final time:', np.mean(final_time))

  plt.plot(num_gen, history)
  plt.savefig('estimation.png')
  plt.show()
