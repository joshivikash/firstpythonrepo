def factors(n):
  """
  Compute the set of factors of n

  Argument:
      n: integer
  Return:
      factors_of_n: set
  """
  factors_set = set()
  for i in range(1,n+1):
    if n % i == 0:
      factors_set.add(i)
  return factors_set

def common_factors(a,b):
  """
  Compute the set of common factors of a and b

  Arguments:
      a, b: integers
  Return:
      factors_common: set
  """
  a_factors = factors(a)
  b_factors = factors(b)
  return a_factors.intersection(b_factors)

def factors_upto(n):
  """
  Get the factors up to n 

  Argument:
      n: integer
  Return:
      result: dict (keys: integers, values: sets)
  """
  factors_dict = {}
  for i in range(1,n+1):
    factors_dict[i] = factors(i)
  return factors_dict

print(factors_upto(10))