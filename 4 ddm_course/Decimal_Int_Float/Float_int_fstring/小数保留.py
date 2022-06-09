#Python 内置的 round() 函数使用了哪种四舍五入策略？
#How to Round Half to Even 一文中提到：
#round() 函数使用 了 "round half to even" 策略。


print('-2.546保留2位 :',round(-2.546,2))
#-2.55

print('-2.535保留2位 :',round(-2.535,2))
#-2.54

print('-2.545保留2位 :',round(-2.545,2))
#-2.54

print('-2.575保留2位 :',round(-2.575,2))
#-2.58

print('-2.595保留2位 :',round(-2.595,2))
#-2.6

print(round(-1.225, 2))

print(round(1.74,1))
print(round(1.75,1))
print(round(1.74))

print(round(-2.961,2))
print(round(-2.961,1))
print(round(-2.961))

print(round(-2.541,2))
print(round(-2.545,2))
print('-2.535,2:',round(-2.535,2))
print(round(-2.546,2))
print(round(-2.441,1))
print(round(-2.941))


import decimal
def __init__(self, min_value=None, max_value=None, force_string=False,
             precision=2, rounding=decimal.ROUND_HALF_UP, **kwargs):
  """
  :param min_value: Validation rule for the minimum acceptable value.
  :param max_value: Validation rule for the maximum acceptable value.
  :param force_string: Store as a string.
  :param precision: Number of decimal places to store.
  :param rounding: The rounding rule from the python decimal library:

      - decimal.ROUND_CEILING (towards Infinity)
      - decimal.ROUND_DOWN (towards zero)
      - decimal.ROUND_FLOOR (towards -Infinity)
      - decimal.ROUND_HALF_DOWN (to nearest with ties going towards zero)
      - decimal.ROUND_HALF_EVEN (to nearest with ties going to nearest even integer)
      - decimal.ROUND_HALF_UP (to nearest with ties going away from zero)
      - decimal.ROUND_UP (away from zero)
      - decimal.ROUND_05UP (away from zero if last digit after rounding towards zero would have been 0 or 5; otherwise towards zero)

      Defaults to: ``decimal.ROUND_HALF_UP``

  """
  self.min_value = min_value
  self.max_value = max_value
  self.force_string = force_string
  self.precision = precision
  self.rounding = rounding

  super(DecimalField, self).__init__(**kwargs)


def round_half_towards_zero(n, decimals=0):
  rounded_abs = round_half_down(abs(n), decimals)
  return math.copysign(rounded_abs, n)

# Also acceptable:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  rounded_abs = round_half_down(abs(n), decimals)
  return sign * rounded_abs

# Without `round_half_down()`:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  multiplier = 10 ** decimals
  rounded_abs = math.ceil(abs(n)*multiplier - 0.5) / multiplier
  return sign * rounded_abs


def round_half_towards_zero(n, decimals=0):
  rounded_abs = round_half_down(abs(n), decimals)
  return math.copysign(rounded_abs, n)

# Also acceptable:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  rounded_abs = round_half_down(abs(n), decimals)
  return sign * rounded_abs

# Without `round_half_down()`:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  multiplier = 10 ** decimals
  rounded_abs = math.ceil(abs(n)*multiplier - 0.5) / multiplier
  return sign * rounded_abs


import math
def round_half_towards_zero(n, decimals=0):
  rounded_abs = round_half_down(abs(n), decimals)
  return math.copysign(rounded_abs, n)

# Also acceptable:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  rounded_abs = round_half_down(abs(n), decimals)
  return sign * rounded_abs

# Without `round_half_down()`:
def round_half_towards_zero(n, decimals=0):
  sign = 1 if n >= 0 else -1
  multiplier = 10 ** decimals
  rounded_abs = math.ceil(abs(n)*multiplier - 0.5) / multiplier
  return sign * rounded_abs


