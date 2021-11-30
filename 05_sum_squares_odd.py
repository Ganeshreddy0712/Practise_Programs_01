import unittest

question_05 = ''' Python script that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.'''


def sum_squares_odd(n):
  if n%2==0:
    n=n-1
    i=1
    square=0
    while i<=n:
      square=(i*i)+square
      i=i+2
  else:
    square=0
    i=1
    while i<n:
      square=(i*i)+square
      i=i+2   
  return square
pass
        


class TestSumSquaresOdd(unittest.TestCase):
  def test_01(self):
    self.assertEqual(sum_squares_odd(4), 10)

  def test_02(self):
    self.assertEqual(sum_squares_odd(9), 84)
     
  def test_03(self):
    self.assertEqual(sum_squares_odd(1), 0)
   
  def test_04(self):
    self.assertEqual(sum_squares_odd(2), 1)
    
  def test_05(self):
    self.assertEqual(sum_squares_odd(100), 166650)
  
if _name_ == '_main_':
    unittest.main(verbosity=2)
