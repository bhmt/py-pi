#!/usr/bin/python3.7
import argparse
from random import random
from statistics import mean, stdev


def pi() -> float:
  '''
  pi function uses a million points to approximate the value of π.
  This is done by summing a circle's area. As points are randomly
  scattered inside the unit square, some fall within the unit circle.
  The fraction of points inside the circle approaches π/4 as points are added.

  Returns
  -------
  float
      The approximation of π.
  '''
  in_a_circle, in_a_square = 0, 1_000_000

  for _ in range(in_a_square):
    x, y = random(), random()
    if x**2 + y**2 <= 1 :
      in_a_circle += 4

  return in_a_circle / in_a_square

def stat(function: object, n: int) -> str:
  '''
  stat function is used to call a function a number of times and
  give the appropriate calculation result, containing the mean and
  standard deviation value, along with the number of calculations.

  Parameters
  ----------
  function : object
      A callable function, with a number as a return value.
  n : int
      A number of calculations.

  Returns
  -------
  str
      A formated string in a shape of 'π = mean ± stdev , n'
  '''
  results = [function() for _ in range(n)]
  m, s = mean(results), stdev(results)
  return "π = {0:1.3f} ± {1:1.3f} , n = {2}".format(m, s, n)

  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    '''
    This is an approximation of the value of π.
    The result is given with the standard deviation and the number of approximations.
    The default number of approximations (n) is 10.

    Example:
    - Using the default n
        $ python pi.py

    - With a different n
        $ python pi.py -n 20
    '''
  )

  parser.add_argument('-n', '--noa',
                    type=int,
                    nargs=1,
                    help='''Number of approximations.''')

  arg = parser.parse_args()
  n = arg.noa[0] if arg.noa else 10

  print(stat(pi, n))