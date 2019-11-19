import numpy as np

class Interval:
  a = None
  b = None

  def __init__(self, a, b):
    # if (a > b):
    #   raise ValueError('a cannot be greater than b')

    self.a = a
    self.b = b

  def __add__(self, o):
    a = self.a + o.a
    b = self.b + o.b
    return Interval(a, b)

  def __sub__(self, o):
    a = self.a - o.b
    b = self.b - o.a
    return Interval(a, b)

  def __mul__(self, o):
    a = min(self.a*o.a, self.a*o.b, self.b*o.a, self.b*o.b)
    b = max(self.a*o.a, self.a*o.b, self.b*o.a, self.b*o.b)
    return Interval(a, b)

  def __truediv__(self, o):
    # if 0 in (o.a, o.b):
    #   raise_info = '{} interval contains zero'.format(o)
    #   raise ZeroDivisionError(raise_info)

    return self*o.inverted()

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

  def negative(self):
    return Interval(-self.b, -self.a)

  def inverted(self):
    return Interval(1/self.b, 1/self.a)

class Matrix:

  def __init__(self, A, n, m):
    if not all((isinstance(interv, Interval) for interv in A)):
      raise ValueErorr("All elements should hape Interval type")

    if len(A) < n*m:
      raise_info = "Cannot reshape matrix with {} elements into {}x{}".format(len(A), n, m)
      raise ValueErorr(raise_info)

    self.n = n
    self.m = m

    if n*m == 4:
      self.a, self.b, self.c, self.d = A
    else:
      self.a, self.b = A

  def __mul__(self, o):
    a = self.a*o.a + self.b*o.b
    b = self.c*o.a + self.d*o.b
    return Matrix([a, b], 2, 1)

  def __repr__(self):
    row_templ = '{}'*self.m
    repr_str = '{}\n'.format(row_templ)*self.n
    if self.n*self.m == 4:
      repr_str = repr_str.format(self.a, self.b, self.c, self.d)
    else:
      repr_str = repr_str.format(self.a, self.b)
    return repr_str

  def inverted(self):
    ones = Interval(1, 1)
    a = ones/(self.a-self.b*self.c/self.d)
    b = Interval(0, 1/3)
    c = ones/(self.b-self.a*self.d/self.c)
    d = ones/(self.d - self.b*self.c/self.a)

    return Matrix([a, b, c, d], 2, 2)

  def det(self):
    return self.a*self.d - self.b*self.c


def test_properties():
  a = Interval(0.007, 1)
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
  a = Interval(2,4)
  b = Interval(-2,0)
  c = Interval(1,1)
  d = Interval(2,4)
  b1 = Interval(-1,1)
  b2 = Interval(0,2)

  A = Matrix([a, b, c, d], 2, 2)
  b = Matrix([b1, b2], 2, 1)

  return A, b


def solve_equations(A, b):
  A_inv = A.inverted()
  print('A_inv')
  print(A_inv)
  x = A_inv*b
  return x


if __name__ == '__main__':
  # test_properties()

  A, b = init_matrixes()
  print('A')
  print(A)
  print('b')
  print(b)
  x = solve_equations(A, b)
  print('x')
  print(x)
