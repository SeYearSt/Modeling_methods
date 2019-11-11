import numpy as np

class Interval:
  a = None
  b = None

  def __init__(self, a, b):
    if (a > b):
      raise ValueError('a cannot be greater than b')

    self.a = a
    self.b = b

  def __add__(self, o):
    a = self.a + o.a
    b = self.b + o.b
    return Interval(a, b)

  def __sub__(self, o):
    a = self.a - o.a
    b = self.b - o.b
    return Interval(a, b)

  def __mul__(self, o):
    a = min(self.a*o.a, self.a*o.b, self.b*o.a, self.b*o.b)
    b = max(self.a*o.a, self.a*o.b, self.b*o.a, self.b*o.b)
    return Interval(a, b)

  def __truediv__(self, o):
    if 0 in (o.a, o.b):
      raise_info = '{} interval contains zero'.format(o)
      raise ZeroDivisionError(raise_info)
    a = self.a/o.b
    b = self.b/o.a
    return Interval(a, b)

  def __abs__(self):
    return max(abs(self.a), abs(self.b))

  def __repr__(self):
    repr = '[{},{}]'.format(self.a, self.b)
    return repr

  def wid(self):
    return self.b - self.a

  def mid(self):
    return (self.b-self.a)/2

  def rad(self):
    return (self.a+self.b)/2


class Matrix:
  def __init__(self, A, n, m):
    if not all((isinstance(interv, Interval) for interv in A)):
      raise ValueErorr("All elements should hape Interval type")

    if len(A) < n*m:
      raise_info = "Cannot reshape matrix with {} elements into {}x{}".format(len(A), n, m)
      raise ValueErorr(raise_info)

    # debug here
    self.A = [[A[i+j] for j in range(m)] for i in range(n)]


  def __mul__(self, o):
    # TODO: check if possible to multiply
    pass

  def inverted(self):
    pass

  

def test_properties():
  a = Interval(0, 1)
  b = Interval(2, 3)

  c = a+b
  d = a-b
  e = a*b
  f = a/b

  print('a:', a)
  print('b:', b)

  print('a+b:', c)
  print('a-b', d)
  print('a*b', e)
  print('a/b', f)

  print('a width:', a.wid())
  print('b width:', b.wid())

  print('a mid:', a.mid())
  print('b mid:', b.mid())

  print('a rad:', a.rad())
  print('b rad:', b.rad())

  print('a abs:', abs(a))
  print('b abs:', abs(b))


def init_matrixes():
  a = Interval(2,2)
  b = Interval(-1,2)
  c = Interval(-1,1)
  d = Interval(2,4)
  b1 = Interval(-1,1)
  b2 = Interval(0,2)

  A = Matrix([a, b, c, d], 2, 2)
  b = Matrix([b1, b2], 2, 1)

  return A, b


def solve_equations(A, b):
  A_inv = A.inverted()
  x = A_inv*b
  return x


if __name__ == '__main__':
  # test_properties()

  A, b = init_matrixes()
  x = solve_equations(A, b)
